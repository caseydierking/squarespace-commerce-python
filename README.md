# Squarespace_Commerce Python Module

The Squarespace_Commerce module attempts to provide easy access to [Squarespace's Commerce API](http://developers.squarespace.com/commerce-api
).

## Usage
````
#Instantiate the squarespace class to get access to your store:
#Version defaults to 1.5
order = Squarespace('APIKEY')

#Optional Parameters include:
order = Squarespace('APIKEY','APIVERSION','APIBASEURL')
````
## Orders API
````
#Get the first page of orders, returns 50:
order.get_orders()

#Optional Parameters include:
order.get_orders(cursor='{Token}',modified_after='{ISO 8601 Date}'',modified_before='{ISO 8601 Date}',fulfillment_status='{PENDING | FULFILLED | CANCELLED}')

#Get a specific order
order.get_order('order_id')

#Fulfill a specific order
order.fulfill_order('order_id')

#Optional Parameters include:
order.fulfill_order('order_id', send_notification={True | FALSE}, ship_date={ISO 8601 Date}, tracking_number='',
                      carrier_name='', service='', tracking_url='{valid_url}'):
````
## Transactions API
#WIP


## Inventory API
#WIP
