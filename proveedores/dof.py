import requests
from bs4 import BeautifulSoup


def Dof():
    #Declaracion de variables
    lista = []
    #Conexion con get de la url
    r = requests.get('https://www.banxico.org.mx/tipcamb/tipCamMIAction.do')
    status_code = r.status_code
    #Si esiste conexion se realiza el procedimiento
    if status_code == 200:
        #Por medio de Beatifulsoap, se realiza un web scraping
        #Utilizando un parser html
        soup = BeautifulSoup(r.text, 'html.parser')
        
        formatos = soup.find_all('td', {'class':"b5"})
            #Se recorren todos los elementos html
        for tipo in formatos:
            #Se realizado otra busqueda de elementos tr
            t = tipo.find_all('tr', {"class":"renglonNon"})
           
            for texto in t:
                texto = [ele.text.strip() for ele in texto]
                lista.append(texto)
        
        datos = {'DOF':{
            'última actualización':lista[0][1],
            'valor': lista[0][5]
        }}     
            
        return datos
    
    
  



        
        



        