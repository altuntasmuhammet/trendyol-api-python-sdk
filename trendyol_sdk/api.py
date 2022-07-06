import requests
from trendyol_sdk.utils import json_encode
from trendyol_sdk.exceptions import TrendyolAPIError

class TrendyolApiClient:

    def __init__(self, api_key, api_secret, supplier_id, integrator_name="SelfIntegration", is_test=False):
        self.api_key = api_key
        self.api_secret = api_secret
        self.supplier_id = supplier_id
        self.integrator_name = integrator_name
        self.is_test = is_test
        self._session = TrendyolSession(api_key, api_secret)
    
    def call(self, method, url, params=None, headers=None, files=None):
        if not params:
            params = {}
        if not headers:
            headers = {}
        if not files:
            files = {}
        
        # set headers
        user_agent = "{} - {}".format(self.supplier_id, self.integrator_name)
        headers.update({
            "User-Agent": user_agent,
            "Content-Type": "application/json;charset=utf-8",
        })
        # call request
        if method in ('GET', 'DELETE'):
            response = self._session.requests.request(
                method,
                url,
                params=params,
                headers=headers,
                files=files,
                timeout=self._session.timeout
            )

        else:
            # Encode params
            params = json_encode(params)
            response = self._session.requests.request(
                method,
                url,
                data=params,
                headers=headers,
                files=files,
                timeout=self._session.timeout
            )
        
        if response.ok:
            return response.json()
        else:
            raise TrendyolAPIError("Call not successfull", response)

class TrendyolSession:
    
    def __init__(self, api_key, api_secret, timeout=None, http_adapter=None):
        self.api_key = api_key,
        self.api_secret = api_secret
        self.timeout=None
        self.http_adapter = http_adapter
        self.requests = requests.Session()
        self.requests.auth = (api_key, api_secret)
        if http_adapter:
            self.requests.mount("https://", http_adapter)