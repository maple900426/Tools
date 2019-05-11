#encoding: utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import requests

class RequestsManager():
    def __init__(self):

        self.headers = {
                        "pc":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36',
                        "phone":'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
                        }

    def send_get_requests( self, url, proxy = None, header_type = 'pc', time_out = 5, failed_file = None, retry = 5, counter = 1 ):

        if counter > retry:
            if failed_file is not None:
                with open(failed_file, 'w') as f:
                    f.write( url + '\n' )
            return None
        try:
            if proxy is None:
                resp = requests.get( url = url, headers = self.headers[header_type], time_out = time_out )
            else:
                resp = requests.get( url = url, headers = self.headers[header_type], time_out = time_out, proxies = proxy )
            if resp.status_code == 200:
                return resp

        except:
            pass

        return self.send_get_requests( url, proxy, header_type, time_out, failed_file, retry, counter + 1 )


