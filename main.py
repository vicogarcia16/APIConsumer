from fastapi import FastAPI, Depends, Body
from fastapi.encoders import jsonable_encoder
from proveedores import dof, fixerio_, banxico
from models.models import UserSchema, UserLoginSchema
from auth.auth_bearer import JWTBearer
from auth.auth_handler import signJWT

import json
app=FastAPI(
    title = "API Consumer",
    description = "API en FastAPI",

    docs_url='/',
    redoc_url='/redoc' 
    )   

#DOF-------------------------------------------------------------
@app.get('/datos/dof', tags=['Datos'],  dependencies=[Depends(JWTBearer())])
def datos_dof():
    valor = dof.Dof()
    json_compatible = jsonable_encoder(valor)
    
    return json_compatible

#Fixerio-------------------------------------------------------------    
@app.get('/datos/fixerio/{token}', tags=['Datos'],  dependencies=[Depends(JWTBearer())])
def datos_fixerio(token:str):
    #Recibe el token de autenticacion de la API
    client = fixerio_.Fixerio(token = token)
    data = json.loads(client.getSeriesLast())
       
    return data

#Banxico-------------------------------------------------------------
@app.get('/datos/banxico/{token}', tags=['Datos'],  dependencies=[Depends(JWTBearer())])
def datos_banxico(token: str):
    #Recibe entre sus argumentos la serie o series deseadas
    #y el token de acceso a la API
    client = banxico.ClienteSIE("SF43718", token = token)

    data = json.loads(client.getSeriesLast())

    return data

#Datos de los tres proveedores-------------------------------------------------------------
@app.get('/datos', tags=['Datos'],  dependencies=[Depends(JWTBearer())])
def datos(token_fixerio:str, token_banxico:str):
    
    valor = dof.Dof()
  
    json_compatible = jsonable_encoder(valor)
    
    datos = {"Tarifas":{
        "DOF":json_compatible["DOF"],
        "Fixerio": datos_fixerio(token_fixerio)},
        "Banxico": datos_banxico(token_banxico)["bmx"]
             
             }
    return datos

#Usuarios-------------------------------------------------------------
users=[]
def check_user(data: UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
    return False

@app.post("/usuario/registro", tags=["Usuarios"])
def registro_usuario(user: UserSchema = Body(...)):
    users.append(user) 
    return signJWT(user.email)


@app.post("/usuario/login", tags=["Usuarios"])
def login_usuario(user: UserLoginSchema = Body(...)):
    if check_user(user):
        return signJWT(user.email)
    return {
        "error": "Datos invalidos o no te encuentras registrado!"
    }