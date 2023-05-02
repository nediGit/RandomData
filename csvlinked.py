import csv
import objects as objs
import schemas
import generators as gen
import os

from schemas import (
    CUSTOMER_SCHEMA,
    PERSON_SCHEMA,
    BILL_SCHEMA,
    PRODUCT_SCHEMA,
    SHOP_SCHEMA,
    BILL_DETAIL_SCHEMA
)

def write_file(headers,elements,file_name):

    file_path = os.getcwd() + '\\files'
    if not os.path.exists(file_path):
        os.mkdir(file_path)

    else:
        with open(file_path+'\\'+file_name,'w',newline='', encoding='utf-8') as csv_file:
            write = csv.writer(csv_file)
            write.writerow(headers)
            for elemen in elements:
                write.writerow(elemen.to_string())


def conected_files(records):
    person_headers = []
    customer_headers = []
    shop_headers = []
    product_headers = []
    bill_headers = []
    bill_details_headers = []
    customer = []
    person = []
    shop = []
    product = []
    bill = []
    bill_detail = []
    bill_total = 0
    total = 0
    
    schema_to_dict = schemas.schema_to_dict()
    print(schema_to_dict)
    #schema_dict = schema_to_dict[name]
    #Get headers
    schema = schema_to_dict['persons']
    for x in schema:
        person_headers.append(x['name'])
    schema = schema_to_dict['customers']
    for x in schema:
        customer_headers.append(x['name'])
    schema = schema_to_dict['shops']
    for x in schema:
        shop_headers.append(x['name'])
    schema = schema_to_dict['products']
    for x in schema:
        product_headers.append(x['name'])
    schema = schema_to_dict['bills']
    for x in schema:
        bill_headers.append(x['name'])
    schema = schema_to_dict['bill_details']
    for x in schema:
        bill_details_headers.append(x['name'])
    
    #Get id at the same time to get related data
    for i in range(records):
        person_name = gen.full_name()
        person_phone = gen.phone()
        person_id = gen.id()
        shop_id = gen.id()
        shop_name = gen.store()
        address = gen.address()
        city = gen.city()
        store_type = gen.store_type()
        person.append(objs.person(person_id,person_name,person_phone))
        shop.append(objs.shop(shop_id,shop_name,address,city,store_type))

    #To add clients to shops
    for i in range(records):
        customer_id = gen.id()
        email = gen.email()
        product_id = gen.id()
        prod_name = gen.product_name()
        prod_price = gen.price()
        person_index = gen.random_positive_int(len(person))
        shop_index = gen.random_positive_int(len(shop))
        product.append(objs.product(product_id,prod_name,shop[shop_index].shop_id,prod_price))
        customer.append(objs.customer(customer_id,person[person_index].person_id,shop[shop_index].shop_id,email))
    
    bill_id = gen.id()
    
    for i in range(records*2):
        quantity = gen.quantity()
        product_index = gen.random_positive_int(len(product))
        total = product[product_index].price*quantity
        bill_total += total
        bill_detail.append(objs.bill_detail(bill_id,product[product_index].product_id,quantity,total))
        if i%2 == 1:
            bill_date = gen.date_time()
            customer_index = gen.random_positive_int(len(customer))
            bill.append(objs.bill(bill_id,customer[customer_index].shop_id,customer[customer_index].customer_id,bill_date,bill_total))
            bill_id = gen.id()
            bill_total = 0

    print("Writing . . . . ")

    #Writing
    write_file(person_headers,person,'persons.csv')
    write_file(customer_headers,customer,'customers.csv')
    write_file(shop_headers,shop,'shops.csv')
    write_file(product_headers,product,'products.csv')
    write_file(bill_headers,bill,'bills.csv')
    write_file(bill_details_headers,bill_detail,'bill_details.csv')


    