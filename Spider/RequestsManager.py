#encoding: utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import requests

class RequestsManager():
    def __init__(self):

        self.phone = {'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
                    'referer': 'https://list.tmall.com/search_product.htm?q=nike&type=p&spm=a220m.6910245.a2227oh.d100&from=mallfp..m_1_searchbutton&style=w'}

        self.pc = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36',
                      'referer': 'https://list.tmall.com/search_product.htm?q=nike&type=p&spm=a220m.6910245.a2227oh.d100&from=mallfp..m_1_searchbutton&style=w'}

        self.headers = {
                        "pc": self.pc,
                        "phone": self.phone
                        }

    def send_get_requests( self, url, proxy = None, header_type = 'pc', timeout = 5, failed_file = None, retry = 5, counter = 1 ):

        if counter > retry:
            if failed_file is not None:
                with open(failed_file, 'w') as f:
                    f.write( url + '\n' )
            return None
        try:
            if proxy is None:
                resp = requests.get( url = url, headers = self.headers[header_type], timeout = timeout )
            else:
                resp = requests.get( url = url, headers = self.headers[header_type], timeout = timeout, proxies = proxy )
            if resp.status_code == 200:
                return resp

        except Exception as e:
            pass

        return self.send_get_requests( url, proxy, header_type, timeout, failed_file, retry, counter + 1 )


