# trendyol-api-python-sdk
Unofficial Trendyol API Python SDK

## Installation

```sh
pip3 install trendyol-api-python-sdk
```

## Usage
```sh
from trendyol_sdk.api import TrendyolApiClient
from trendyol_sdk.services import ProductIntegrationService
api = TrendyolApiClient(api_key="<TRENDYOL_API_KEY>", api_secret="<TRENDYOL_API_SECRET>", supplier_id="<TRENDYOL_SELLER_ID>")
service = ProductIntegrationService(api)
products = service.get_products()
```

## Services Completion Status
- [x] Product Integration (Urun Entegrasyonu)
- [ ] Order Integration (Siparis Entegrasyonu)
- [ ] Common Label Integration (Ortak Etiken Entegrasyonu)
- [ ] Returned Orders Integration (Iade Entegrasyonu)
- [ ] Accounting And Finance Integration (Muhasebe ve Finans Entegrasyonu)
- [ ] Question And Answer Integration (Soru Cevap Entegrasyonu)
