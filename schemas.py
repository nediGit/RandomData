

CUSTOMER_SCHEMA = [{
    "name": "Customer Id",
    "type": 'id'
}, {
    "name": "Person Id",
    "type": 'id'
}, {
    "name": "Shop Id",
    "type": "id"
}, {
    "name": "Email",
    "type": "email"
}]

PERSON_SCHEMA =[{
    "name": "Person Id",
    "type": 'id'
}, {
    "name": "Name",
    "type": 'full_name'
}, {
    "name": "Phone",
    "type": 'phone'
}]

BILL_SCHEMA = [{
    "name": "Bill Id",
    "type": 'id'
}, {
    "name": "Shop Id",
    "type": 'id'
}, {
    "name": "Client Id",
    "type": "id"
}, {
    "name": "Date",
    "type": "datetime"
}, {
    "name": "Total",
    "type": "total"
}]

PRODUCT_SCHEMA = [{
    "name": "Product Id",
    "type": 'id'
}, {
    "name": "Product name",
    "type": "product_name"
}, {
    "name": "Shop Id",
    "type": "id"
}, {
    "name": "Price",
    "type": "price"
}]


SHOP_SCHEMA = [{
    "name": "Shop Id",
    "type": "id"
}, {
    "name": "Shop name",
    "type": "store"
}, {
    "name": "Address",
    "type": "address"
}, {
    "name": "City",
    "type": "city"
}, {
    "name": "Store type",
    "type": "store_type"
}]

BILL_DETAIL_SCHEMA = [{
    "name": "Bill Id",
    "type": 'id'
}, {
    "name": "Product id",
    "type": 'id'
}, {
    "name": "Quantity",
    "type": "small_positive_int"
}, {
    "name": "Total",
    "type": "total"
}]

def schema_to_dict():
    SCHEMA_TO_DICT = {
        'customers': CUSTOMER_SCHEMA,
        'persons': PERSON_SCHEMA,
        'bills': BILL_SCHEMA,
        'products': PRODUCT_SCHEMA,
        'shops': SHOP_SCHEMA,
        'bill_details': BILL_DETAIL_SCHEMA
    }
    return SCHEMA_TO_DICT