from requests import Request, Session

class Fixerio():
    def __init__(self, token=None, symbols = "MXN"):
        self.token = token
        self.symbols = symbols
        self.url = "http://data.fixer.io/api/"
        self.params = {}
        self.session = Session()
        

    def seriesLast(self):
        addition = "latest"
        url = self.url + addition
        return url
    
    def accessKey(self):
        url = self.seriesLast() + "?access_key=" + self.token
        return url
    
    def serieLatest(self):
        url = self.accessKey() + "&symbols=" + self.symbols
        return url
    
    def set_request(self, url):
        r = Request(method='GET', url = url, params=self.params)
        return r.prepare()
    
    def getSeriesLast(self):
        req = self.set_request(self.serieLatest())
        res = self.session.send(req)
        return res.text
    
