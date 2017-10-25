#coding=utf-8
import requests
import logging
import cfg
logger = logging.getLogger(__name__)

class Cc(object):

    def __init__(self,uri=None):
        self.serverURI=uri
        self.session=requests.session()

    def searchKB(self,key=None):
        key={'search':key}
        r=self.session.post(self.serverURI+'/wc/searchKB',data=key)
        return r




if __name__ == '__main__':
    cc=Cc(uri='http://localhost:8081')
    r=cc.searchKB(key='骷髅')
    l=r.json()
    x=l[0]
    print(x)
    print(x['scName'])
    print(x['id'])
    s='http://localhost:8081/'+'view?id='+str(x['id'])

    print(s)
