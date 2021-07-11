# trendyol-api-python-sdk
Unofficial Trendyol API Python SDK

## Installation

```sh
pip3 install -r requirements.txt
```

## Usage
```sh
from trendyol_sdk.api import TrendyolApi
from trendyol_sdk.services import ProductIntegrationService
api = TrendyolApi(api_key="<TRENDYOL_API_KEY>", api_secret="<TRENDYOL_API_SECRET>", supplier_id="<TRENDYOL_SELLER_ID>")
service = ProductIntegrationService(api)
products = service.get_products()
