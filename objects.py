class person:
    def __init__(self,person_id,name,phone):
        self.person_id=person_id
        self.name=name
        self.phone=phone

    def to_string(person):
        return [str(person.person_id),str(person.name),str(person.phone)]

class customer:
    def __init__(self,customer_id,person_id,shop_id,email):
        self.customer_id=customer_id
        self.person_id=person_id
        self.email=email
        self.shop_id=shop_id

    def to_string(customer):
        return [str(customer.customer_id),str(customer.person_id),str(customer.shop_id),str(customer.email)]

class shop:
    def __init__(self,shop_id,shop_name,address,city,store_type):
        self.shop_id=shop_id
        self.shop_name=shop_name
        self.address=address
        self.city=city
        self.store_type=store_type

    def to_string(shop):
        return [str(shop.shop_id),str(shop.shop_name),str(shop.address),str(shop.city),str(shop.store_type)]

class product:
    def __init__(self,product_id,product_name,shop_id,price):
        self.product_id=product_id
        self.product_name=product_name
        self.shop_id=shop_id
        self.price=price

    def to_string(product):
        return [str(product.product_id),str(product.name),str(product.shop_id),str(product.price)]

class bill:
    def __init__(self,bill_id,shop_id,customer_id,date_time,total):
        self.bill_id=bill_id
        self.shop_id=shop_id
        self.customer_id=customer_id
        self.date_time=date_time
        self.total=total

    def to_string(bill):
        return [str(bill.bill_id),str(bill.shop_id),str(bill.customer_id),str(bill.date_time),str(bill.total)]

class bill_detail:
    def __init__(self,bill_id,product_id,quantity,total):
        self.bill_id=bill_id
        self.product_id=product_id
        self.quantity=quantity
        self.total=total

    def to_string(bill_detail):
        return [str(bill_detail.bill_id),str(bill_detail.product_id),str(bill_detail.quantity),str(bill_detail.total)]
