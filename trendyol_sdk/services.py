from urllib.parse import urljoin


class BaseService:

    def __init__(self, api):
        self._api = api
        if self._api.is_test:
            self.base_url = "https://stageapi.trendyol.com/stagesapigw/"
        else:
            self.base_url = "https://api.trendyol.com/sapigw/"


class ProductIntegrationService(BaseService):

    def __init__(self, api):
        super(ProductIntegrationService, self).__init__(api)

    def get_suppliers_addresses(self, supplier_id=None):
        if supplier_id:
            endpoint = "suppliers/{}/addresses".format(supplier_id)
        else:
            endpoint = "suppliers/{}/addresses".format(self._api.supplier_id)
        url = urljoin(self.base_url, endpoint)
        data = self._api.call("GET", url, params=None,
                              headers=None, files=None)
        return data

    def get_shipment_providers(self):
        endpoint = "shipment-providers"
        url = urljoin(self.base_url, endpoint)
        data = self._api.call("GET", url, params=None,
                              headers=None, files=None)
        return data

    def get_brands(self, page, size):
        endpoint = "brands"
        url = urljoin(self.base_url, endpoint)
        params = {
            "page": page,
            "size": size
        }
        data = self._api.call("GET", url, params=params,
                              headers=None, files=None)
        return data

    def get_brands_by_name(self, name):
        endpoint = "brands/by-name"
        url = urljoin(self.base_url, endpoint)
        params = {
            "name": name
        }
        data = self._api.call("GET", url, params=params,
                              headers=None, files=None)
        return data

    def get_categories(self):
        endpoint = "product-categories"
        url = urljoin(self.base_url, endpoint)
        data = self._api.call("GET", url, params=None,
                              headers=None, files=None)
        return data

    def get_category_attributes(self, category_id):
        endpoint = "product-categories/{}/attributes".format(category_id)
        url = urljoin(self.base_url, endpoint)
        params = {
            "category_id": category_id
        }
        data = self._api.call("GET", url, params=params,
                              headers=None, files=None)
        return data

    def get_products(self, filter_params=None, supplier_id=None):
        if supplier_id:
            endpoint = "suppliers/{}/products".format(supplier_id)
        else:
            endpoint = "suppliers/{}/products".format(self._api.supplier_id)
        if not filter_params:
            filter_params = {}
        params = {
            "approved": filter_params.get("approved", ""),
            "barcode": filter_params.get("barcode", ""),
            "startDate": filter_params.get("startDate", ""),
            "endDate": filter_params.get("endDate", ""),
            "page": filter_params.get("page", ""),
            "dateQueryType": filter_params.get("dateQueryType", ""),
            "size": filter_params.get("size", "")
        }
        url = urljoin(self.base_url, endpoint)
        data = self._api.call("GET", url, params=params,
                              headers=None, files=None)
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
        data = self._api.call("POST", url, params=params,
                              headers=None, files=None)
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
        data = self._api.call("PUT", url, params=params,
                              headers=None, files=None)
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
        data = self._api.call("GET", url, params=None,
                              headers=None, files=None)
        return data

    def update_price_and_stock(self, items, supplier_id=None):
        if supplier_id:
            endpoint = "suppliers/{supplier_id}/products/products/price-and-inventory".format(
                supplier_id=supplier_id
            )
        else:
            endpoint = "suppliers/{supplier_id}/products/batch-requests/{batch_request_id}".format(
                supplier_id=self._api.supplier_id
            )
        url = urljoin(self.base_url, endpoint)
        params = {
            "items": items
        }
        data = self._api.call("PUT", url, params=params,
                              headers=None, files=None)
        return data


class OrderIntegrationService(BaseService):

    def __init__(self, api):
        super(OrderIntegrationService, self).__init__(api)

    def get_shipment_packages(self, filter_params={}, supplier_id=None):
        if supplier_id:
            endpoint = "suppliers/{}/orders".format(supplier_id)
        else:
            endpoint = "suppliers/{}/orders".format(self._api.supplier_id)
        if not filter_params:
            filter_params = {}
        params = {
            "startDate": filter_params.get("startDate", ""),
            "endDate": filter_params.get("endDate", ""),
            "page": filter_params.get("page", ""),
            "size": filter_params.get("size", ""),
            "orderNumber": filter_params.get("orderNumber", ""),
            "status": filter_params.get("status", ""),
            "orderByField": filter_params.get("orderByField", ""),
            "orderByDirection": filter_params.get("orderByDirection", ""),
            "shipmentPackageIds": filter_params.get("shipmentPackageIds", "")
        }
        url = urljoin(self.base_url, endpoint)
        pass

    def get_awaiting_shipment_packages(self, supplier_id=None):
        filter_params = {
            "status": "Awaiting"
        }
        data = self.get_awaiting_shipment_packages(filter_params=filter_params)
        return data

    def update_tracking_number(self, shipment_package_id, supplier_id=None):
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
        data = self._api.call("PUT", url, params=None,
                              headers=None, files=None)
        return data

    def update_shipment_package(self, shipment_package_id, params, supplier_id=None):
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
        data = self._api.call("PUT", url, params=params,
                              headers=None, files=None)
        return data

    def update_package_as_unsupplied(self, reason_id, supplier_id=None):
        if supplier_id:
            url = "http://oms-seller-integration-api.trendyol.com/sellers/{supplier_id}/shipment-packages/unsupplied".format(
                supplier_id=supplier_id)
        else:
            url = "http://oms-seller-integration-api.trendyol.com/sellers/{supplier_id}/shipment-packages/unsupplied".format(
                supplier_id=self._api.supplier_id)
        params = {
            "lines": [
                {
                    "lineId": 0,
                    "quantity": 0
                }
            ],
            "reasonId": reason_id
        }
        data = self._api.call("PUT", url, params=params,
                              headers=None, files=None)
        return data

    def sent_invoice_link(self, params, supplier_id=None):
        if supplier_id:
            endpoint = "suppliers/{supplier_id}/supplier-invoice-links".format(
                supplier_id=supplier_id,
            )
        else:
            endpoint = "suppliers/{supplier_id}/supplier-invoice-links".format(
                supplier_id=self._api.supplier_id,
            )
        params = {}
        url = urljoin(self.base_url, endpoint)
        data = self._api.call("POST", url, params=params,
                              headers=None, files=None)
        return data

    def split_multi_package_by_quantity(self, shipment_package_id, params, supplier_id=None):
        if supplier_id:
            endpoint = "suppliers/{supplier_id}/shipment-packages/{shipment_package_id}/split-packages".format(
                supplier_id=supplier_id,
                shipment_package_id=shipment_package_id
            )
        else:
            endpoint = "suppliers/{supplier_id}/shipment-packages/{shipment_package_id}/split-packages".format(
                supplier_id=self._api.supplier_id,
                shipment_package_id=shipment_package_id
            )
        url = urljoin(self.base_url, endpoint)
        data = self._api.call("POST", url, params=params,
                              headers=None, files=None)
        return data

    def split_shipment_package(self, shipment_package_id, supplier_id=None):
        if supplier_id:
            endpoint = "suppliers/{supplier_id}/shipment-packages/{shipment_package_id}/split".format(
                supplier_id=supplier_id,
                shipment_package_id=shipment_package_id
            )
        else:
            endpoint = "suppliers/{supplier_id}/shipment-packages/{shipment_package_id}/split".format(
                supplier_id=self._api.supplier_id,
                shipment_package_id=shipment_package_id
            )
        url = urljoin(self.base_url, endpoint)
        data = self._api.call("POST", url, params=None,
                              headers=None, files=None)
        return data

    def multi_split_shipment_package(self, shipment_package_id, params, supplier_id=None):
        if supplier_id:
            endpoint = "suppliers/{supplier_id}/shipment-packages/{shipment_package_id}/multi-split".format(
                supplier_id=supplier_id,
                shipment_package_id=shipment_package_id
            )
        else:
            endpoint = "suppliers/{supplier_id}/shipment-packages/{shipment_package_id}/multi-split".format(
                supplier_id=self._api.supplier_id,
                shipment_package_id=shipment_package_id
            )
        url = urljoin(self.base_url, endpoint)
        data = self._api.call("POST", url, params=params,
                              headers=None, files=None)
        return data

    def split_shipment_package_by_quantity(self, shipment_package_id, params, supplier_id=None):
        if supplier_id:
            endpoint = "suppliers/{supplier_id}/shipment-packages/{shipment_package_id}/quantity-split".format(
                supplier_id=supplier_id,
                shipment_package_id=shipment_package_id
            )
        else:
            endpoint = "suppliers/{supplier_id}/shipment-packages/{shipment_package_id}/quantity-split".format(
                supplier_id=self._api.supplier_id,
                shipment_package_id=shipment_package_id
            )
        url = urljoin(self.base_url, endpoint)
        data = self._api.call("POST", url, params=params,
                              headers=None, files=None)
        return data

    def update_box_info(self, shipment_package_id, params, supplier_id=None):
        if supplier_id:
            endpoint = "suppliers/{supplier_id}/shipment-packages/{shipment_package_id}/box-info".format(
                supplier_id=supplier_id,
                shipment_package_id=shipment_package_id
            )
        else:
            endpoint = "suppliers/{supplier_id}/shipment-packages/{shipment_package_id}/box-info".format(
                supplier_id=self._api.supplier_id,
                shipment_package_id=shipment_package_id
            )
        url = urljoin(self.base_url, endpoint)
        data = self._api.call("PUT", url, params=params,
                              headers=None, files=None)
        return data

    def process_alternative_delivery(self, shipment_package_id, params, supplier_id=None):
        if supplier_id:
            endpoint = "suppliers/{supplier_id}/shipment-packages/{shipment_package_id}/alternate-delivery".format(
                supplier_id=supplier_id,
                shipment_package_id=shipment_package_id
            )
        else:
            endpoint = "suppliers/{supplier_id}/shipment-packages/{shipment_package_id}/alternate-delivery".format(
                supplier_id=self._api.supplier_id,
                shipment_package_id=shipment_package_id
            )
        url = urljoin(self.base_url, endpoint)
        data = self._api.call("PUT", url, params=params,
                              headers=None, files=None)
        return data

    def process_manual_delivery(self, cargo_tracking_number, params, supplier_id=None):
        if supplier_id:
            endpoint = "suppliers/{supplier_id}/manual-deliver/{cargo_tracking_number}".format(
                supplier_id=supplier_id,
                cargo_tracking_number=cargo_tracking_number
            )
        else:
            endpoint = "suppliers/{supplier_id}/manual-deliver/{cargo_tracking_number}".format(
                supplier_id=self._api.supplier_id,
                cargo_tracking_number=cargo_tracking_number
            )
        url = urljoin(self.base_url, endpoint)
        data = self._api.call("PUT", url, params=params,
                              headers=None, files=None)
        return data

    def change_cargo_provider(self, shipment_package_id, cargo_provider, supplier_id=None):
        if supplier_id:
            endpoint = "suppliers/{supplier_id}/shipment-packages/{shipment_package_id}/cargo-providers".format(
                supplier_id=supplier_id,
                shipment_package_id=shipment_package_id
            )
        else:
            endpoint = "suppliers/{supplier_id}/shipment-packages/{shipment_package_id}/cargo-providers".format(
                supplier_id=self._api.supplier_id,
                shipment_package_id=shipment_package_id
            )
        url = urljoin(self.base_url, endpoint)
        params = {
            "cargoProvider": cargo_provider
        }
        data = self._api.call("PUT", url, params=params,
                              headers=None, files=None)
        return data


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
