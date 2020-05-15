import requests


class Squarespace(object):

    def __init__(self, api_key, api_version, base_url):
        self.api_key = api_key
        self.api_version = api_version
        self.base_url = base_url

        self.headers = {"Authorization": "Bearer " + self.api_key}
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
            print("has cursor")
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


    def get_order(self,order_id):
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



def start():
    a = Squarespace('APIKEY', '1.0', 'https://api.squarespace.com/')
    print(a.api_key)
    print(a.headers)
    print(a.orders_url)
    print(a.inventory_url)
    print(a.transactions_url)
    response = a.get_orders()
    #response = a.get_order("5c9ee5bb0d92972348ba5fbf")
    response = a.get_order('5eb8888603feca74a92fa2d0')
    print(response)
