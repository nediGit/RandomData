import random
import string
from faker import Faker

fake = Faker()

def id(len=15):
    lst =  [random.choice(string.hexdigits) for n in range(len)]
    return "".join(lst)

def quantity():
    return random.randrange(1, 3)

def small_positive_int():
    return random.randrange(1, 10)

def random_positive_int(num):
    return random.randrange(1,num)

def positive_int():
    return random.randrange(1, 1000)

def product_name():
    return fake.text(max_nb_chars=30)

def price():
    return round(random.uniform(0,20),2)

def email():
    return fake.email()

def full_name():
    return fake.name()

def phone():
    return fake.msisdn()

def store():
    return fake.company()

def city():
    return fake.city()

def address():
    return fake.address().replace('\n','')

def date_time():
    return fake.date_time()

def store_type():
    return random.choice(["Sport",
                          "Electronics",
                          "Supermarket",
                          "General store",
                          "Ladies shoes",
                          "Mens shoes"
                          "Ladies clothes",
                          "Men's clothes"
])

TYPES_TO_GENERATORS = {
    'id': id,
    'small_positive_int': small_positive_int,
    'quantity': quantity,
    'random_positive_int': random_positive_int,
    'positive_int': positive_int,
    'product_name': product_name,
    'price': price,
    'email': email,
    'full_name': full_name,
    'phone': phone,
    'store': store,
    'city': city,
    'datetime': date_time,
    'address': address,
    'store_type': store_type,
    'total': float
}

