from urllib.parse import urljoin
from trendyol_sdk import api

class BaseService:

    def __init__(self, api: 'api.TrendyolApiClient'):
        self._api = api
        if self._api.is_test:
            self.base_url = "https://stageapi.trendyol.com/stagesapigw/"
        else:
            self.base_url = "https://api.trendyol.com/sapigw/"


class ProductIntegrationService(BaseService):

    def __init__(self, api: 'api.TrendyolApiClient'):
        super(ProductIntegrationService, self).__init__(api)

    def get_suppliers_addresses(self, supplier_id=None):
        if supplier_id:
            endpoint = "suppliers/{}/addresses".format(supplier_id)
        else:
            endpoint = "suppliers/{}/addresses".format(self._api.supplier_id)
        url = urljoin(self.base_url, endpoint)
        data = self._api.call("GET", url, params=None, headers=None, files=None)
        return data

    def get_shipment_providers(self):
        endpoint = "shipment-providers"
        url = urljoin(self.base_url, endpoint)
        data = self._api.call("GET", url, params=None, headers=None, files=None)
        return data

    def get_brands(self, page, size):
        endpoint = "brands"
        url = urljoin(self.base_url, endpoint)
        params = {
            "page": page,
            "size": size
        }
        data = self._api.call("GET", url, params=params, headers=None, files=None)
        return data

    def get_brands_by_name(self, name):
        endpoint = "brands/by-name"
        url = urljoin(self.base_url, endpoint)
        params = {
            "name": name
        }
        data = self._api.call("GET", url, params=params, headers=None, files=None)
        return data

    def get_categories(self):
        endpoint = "product-categories"
        url = urljoin(self.base_url, endpoint)
        data = self._api.call("GET", url, params=None, headers=None, files=None)
        return data

    def get_category_attributes(self, category_id):
        endpoint = "product-categories/{}/attributes".format(category_id)
        url = urljoin(self.base_url, endpoint)
        params = {
            "category_id": category_id
        }
        data = self._api.call("GET", url, params=params, headers=None, files=None)
        return data

    def get_products(self, filter_params=None, supplier_id=None):
        if supplier_id:
            endpoint = "suppliers/{}/products".format(supplier_id)
        else:
            endpoint = "suppliers/{}/products".format(self._api.supplier_id)
        if not filter_params:
            filter_params = {}
        params = {
            "approved": filter_params.get("approved", None),
            "barcode": filter_params.get("barcode", None),
            "startDate": filter_params.get("startDate", None),
            "endDate": filter_params.get("endDate", None),
            "page": filter_params.get("page", None),
            "dateQueryType": filter_params.get("dateQueryType", None),
            "size": filter_params.get("size", None)
        }
        url = urljoin(self.base_url, endpoint)
        data = self._api.call("GET", url, params=params, headers=None, files=None)
        return data

    def create_products(self, items, supplier_id=None):
        if supplier_id:
            endpoint = "suppliers/{}/products".format(supplier_id)
        else:
            endpoint = "suppliers/{}/products".format(self._api.supplier_id)
        url = urljoin(self.base_url, endpoint)
        params = {
            "items": items
        }
        data = self._api.call("POST", url, params=params, headers=None, files=None)
        return data

    def update_products(self, items, supplier_id=None):
        if supplier_id:
            endpoint = "suppliers/{}/products".format(supplier_id)
        else:
            endpoint = "suppliers/{}/products".format(self._api.supplier_id)
        url = urljoin(self.base_url, endpoint)
        params = {
            "items": items
        }
        data = self._api.call("PUT", url, params=params, headers=None, files=None)
        return data

    def get_batch_requests(self, batch_request_id, supplier_id=None):
        if supplier_id:
            endpoint = "suppliers/{supplier_id}/products/batch-requests/{batch_request_id}".format(
                supplier_id=supplier_id,
                batch_request_id=batch_request_id
            )
        else:
            endpoint = "suppliers/{supplier_id}/products/batch-requests/{batch_request_id}".format(
                supplier_id=self._api.supplier_id,
                batch_request_id=batch_request_id
            )
        url = urljoin(self.base_url, endpoint)
        data = self._api.call("GET", url, params=None, headers=None, files=None)
        return data

    def update_price_and_stock(self, items, supplier_id=None):
        if supplier_id:
            endpoint = "suppliers/{supplier_id}/products/price-and-inventory".format(
                supplier_id=supplier_id
            )
        else:
            endpoint = "suppliers/{supplier_id}/products/price-and-inventory".format(
                supplier_id=self._api.supplier_id
            )
        url = urljoin(self.base_url, endpoint)
        params = {
            "items": items
        }
        data = self._api.call("POST", url, params=params, headers=None, files=None)
        return data
        

class OrderIntegrationService(BaseService):

    def __init__(self, api):
        super(OrderIntegrationService, self).__init__(api)

    def get_shipment_packages(self, filter_params, supplier_id=None):
        if supplier_id:
            endpoint = "suppliers/{}/orders".format(supplier_id)
        else:
            endpoint = "suppliers/{}/orders".format(self._api.supplier_id)
        if not filter_params:
            filter_params = {}
        params = {
            "startDate": filter_params.get("startDate", None),
            "endDate": filter_params.get("endDate", None),
            "page": filter_params.get("page", None),
            "size": filter_params.get("size", None),
            "orderNumber": filter_params.get("orderNumber", None),
            "status": filter_params.get("status", None),
            "orderByField": filter_params.get("orderByField", None),
            "orderByDirection": filter_params.get("orderByDirection", None),
            "shipmentPackageIds": filter_params.get("shipmentPackageIds", None)
        }
        url = urljoin(self.base_url, endpoint)
        data = self._api.call("GET", url, params=params, headers=None, files=None)
        return data

    def get_awaiting_shipment_packages(self):
        pass

    def update_tracking_number(self, shipment_package_id, tracking_number, supplier_id=None):
        if supplier_id:
            endpoint = "suppliers/{supplier_id}/{shipment_package_id}/update-tracking-number".format(
                supplier_id=supplier_id,
                shipment_package_id=shipment_package_id
            )
        else:
            endpoint = "suppliers/{supplier_id}/{shipment_package_id}/update-tracking-number".format(
                supplier_id=self._api.supplier_id,
                shipment_package_id=shipment_package_id
            )
        url = urljoin(self.base_url, endpoint)
        params = {
            "trackingNumber": tracking_number
        }
        data = self._api.call("PUT", url, params=params, headers=None, files=None)
        return data

    def update_shipment_package(self, shipment_package_id, status, lines=None, params=None, supplier_id=None):
        if supplier_id:
            endpoint = "suppliers/{supplier_id}/shipment-packages/{shipment_package_id}".format(
                supplier_id=supplier_id,
                shipment_package_id=shipment_package_id
            )
        else:
            endpoint = "suppliers/{supplier_id}/shipment-packages/{shipment_package_id}".format(
                supplier_id=self._api.supplier_id,
                shipment_package_id=shipment_package_id
            )
        url = urljoin(self.base_url, endpoint)
        params = {
            "status": status
        }
        if lines:
            params["lines"] = lines
        if params:
            params["params"] = params
        data = self._api.call("PUT", url, params=params, headers=None, files=None)
        return data

    def update_package_as_unsupplied(self):
        pass

    def send_invoice_link(self):
        pass

    def split_multi_package_by_quantity(self):
        pass

    def split_shipment_package(self):
        pass

    def split_multi_shipment_package(self):
        pass

    def split_shipment_package_by_quantity(self):
        pass

    def update_box_info(self):
        pass

    def process_alternative_delivery(self):
        pass

    def change_cargo_provider(self):
        pass


class CommonLabelIntegrationService(BaseService):

    def __init__(self, api):
        super(CommonLabelIntegrationService, self).__init__(api)

    def create_common_label(self):
        pass

    def get_common_label(self):
        pass

    def get_common_label_v2(self):
        pass


class ReturnedOrdersIntegrationService(BaseService):

    def __init__(self, api):
        super(ReturnedOrdersIntegrationService, self).__init__(api)

    def get_shipment_packages(self):
        pass

    def create_claim(self):
        pass

    def approve_claim_line_items(self):
        pass

    def create_claim_issue(self):
        pass

    def get_claim_issue_reasons(self):
        pass

    def get_claim_audits(self):
        pass


class AccountingAndFinanceIntegrationService(BaseService):

    def __init__(self, api):
        super(AccountingAndFinanceIntegrationService, self).__init__(api)

    def filter_with_date_validation_constraint(self):
        pass

    def get_settlements(self):
        pass

    def get_other_financials(self):
        pass


class QuestionAndAnswerIntegrationService(BaseService):

    def __init__(self, api):
        super(QuestionAndAnswerIntegrationService, self).__init__(api)

    def get_question_filters(self):
        pass

    def get_question_filter_by_id(self):
        pass

    def create_answer(self):
        pass
