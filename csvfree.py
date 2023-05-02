import csv
import os
import schemas
from generators import TYPES_TO_GENERATORS


from schemas import (
    CUSTOMER_SCHEMA,
    PERSON_SCHEMA,
    BILL_SCHEMA,
    PRODUCT_SCHEMA,
    SHOP_SCHEMA,
    BILL_DETAIL_SCHEMA
)



def file_manager(count):
    generate_file('persons', count)
    generate_file('customers', count)
    generate_file('bills', count)
    generate_file('shops', count)
    generate_file('bill_details', count)
    generate_file('products', count)

def generate_file(name, count):
    schema_to_dict = schemas.schema_to_dict()
    schema_dict = schema_to_dict[name]
    data_generators = [TYPES_TO_GENERATORS[elem['type']] for elem in schema_dict]
    rows = []

    file_path = os.getcwd() + '\\files'
    file_name = file_path +'\\'+ name+'_free.csv'
    if not os.path.exists(file_path):
        os.mkdir(file_path)
    else:
        with open(file_name, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)

            # Headers
            headers = [elem['name'] for elem in schema_dict]
            headers.insert(0, "Index") # Add an Index header
            writer.writerow(headers)

            # Content
            data_generators = [TYPES_TO_GENERATORS[elem['type']] for elem in schema_dict]

            rows = []
            for index in range(1, count+1):
                row = [gen() for gen in data_generators]
                row.insert(0, index)
                rows.append(row)

                if index % 1000 == 0:
                    writer.writerows(rows)
                    rows = []

                if index % 10000 == 0:
                    print("{}/{}".format(index, count))

            writer.writerows(rows)

