import requests
import json
import datetime


class Squarespace(object):

    def __init__(self, api_key, api_version='1.0', base_url='https://api.squarespace.com/'):
        self.api_key = api_key
        self.api_version = api_version
        self.base_url = base_url

        self.headers = {"Authorization": "Bearer " + self.api_key, "Content-type": "application/json"}
        self.orders_url = self.base_url + self.api_version + "/commerce/orders"
        self.inventory_url = self.base_url + self.api_version + "/commerce/inventory"
        self.transactions_url = self.base_url + self.api_version + "/commerce/transactions"

    def get_orders(self, cursor=None, modified_after=None, modified_before=None, fulfillment_status=None):
        """Gets all orders via the Squarespace Order API endpoint.
        Options include:
            :param cursor: A string token, returned from the pagination.nextPageCursor of a previous response.
            :param modified_after: An ISO 8601 date and time string, e.g. 2016-04-10T12:00:00Z.
                            (required when modifiedBefore is present)
            :param modified_before = An ISO 8601 date and time string.
                            (required when modifiedAfter is present)
            :param fulfillment_status: An enumerated string value of PENDING, FULFILLED, or CANCELED.
        """
        url = self.orders_url + "?"

        if fulfillment_status is not None:
            url = url + fulfillment_status + "&"
        if cursor is not None:
            url = url + cursor + "&"
        if modified_after is not None and modified_before is not None:
            url = url + modified_after + "&"
            url = url + modified_before + "&"

        r = requests.get(url, headers=self.headers)
        try:
            if r.status_code == requests.codes.ok:
                return r.json()
            else:
                return r
        except requests.exceptions.RequestException as e:  # This is the correct syntax
            raise SystemExit(e)

    def get_order(self, order_id):
        """Gets single order via the Squarespace Order API endpoint.
            :param order_id: The ID of the order
         """
        url = self.orders_url + f"/{order_id}"
        print(url)
        r = requests.get(url, headers=self.headers)
        try:
            if r.status_code == requests.codes.ok:
                return r.json()
            else:
                return r
        except requests.exceptions.RequestException as e:  # This is the correct syntax
            raise SystemExit(e)

    def fulfill_order(self, order_id, send_notification=False, ship_date=None, tracking_number=None,
                      carrier_name=None, service=None, tracking_url=None):
        """You can post a fulfillment of an order, which will change its fulfillment state to FULFILLED
        and optionally trigger an email notification to the customer.
        It will update the order summary with the shipments sent during the fulfillment.
        When passing in shipment information, tracking_number, carrier_name, service, and tracking_url are required.
            :param order_id:
                The ID of the order
            :param send_notification:
                Indicates whether the customer should receive an email notification about the added shipments.
            :param ship_date:
            :param tracking_number:
                A string representing the carrier-generated tracking number.
            :param carrier_name:
                A string representing the parcel service transporting the shipment.
            :param service:
                A string representing the level of service, as offered by the carrier, used for this shipment.
            :param tracking_url:
                A string representing the level of service, as offered by the carrier, used for this shipment.
         """
        url = self.orders_url + f"/{order_id}/fulfillments"

        if ship_date is None:
            ship_date = datetime.datetime.now().isoformat()

        fulfilled_order = {
            "shouldSendNotification": json.dumps(send_notification),
            "shipments": []
        }

        if carrier_name and service and tracking_number and tracking_url:
            fulfilled_order["shipments"] = [
                    {
                        "shipDate": ship_date,
                        "carrierName": carrier_name,
                        "service": service,
                        "trackingNumber": tracking_number,
                        "trackingUrl": tracking_url
                    }
                ]

        r = requests.post(url, json=fulfilled_order, headers=self.headers)

        try:
            if r.status_code == 204:
                return r
            else:
                return r
        except requests.exceptions.RequestException as e:  # This is the correct syntax
            raise SystemExit(e)



