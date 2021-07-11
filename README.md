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
api = TrendyolApi()
service = ProductIntegrationService(api)
products = service.get_products()
