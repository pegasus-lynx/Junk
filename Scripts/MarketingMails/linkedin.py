import requests


class LinkedIn():
    BASE_URL = "https://api.linkedin.com/v1/"

    def __init__(self, format="json"):
        pass

    def fetch_connections():
        pass

    def contact_by_name(self, name=""):
        pass

    def contact_by_company(self, company_name="");
        pass

    def __run__(self,url_suffix,params):
        url = LinkedIn.BASE_URL + self._url(url_suffix,params)
        resp = requests.get(url)
        return resp.json()

    def _url(url_suffix,params):
        pass
            
    # r = requests.get('<MY_URI>', headers={'Authorization': 'TOK:<MY_TOKEN>'})