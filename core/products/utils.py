from typing import List
from django.db.models import Max
import math


class FilterPrice:
    def __init__(self, products):
        self.products = products.order_by('price')
        # count total products and take 30% and 60%
        self.total = [math.ceil(products.count()*p) for p in [0.30, 0.60]]

    def price1(self):
        # take max price 30% products
        price = self.products[:self.total[0]].aggregate(Max('price'))
        return int(price['price__max']) # convert decimal to int

    def price2(self):
        # take max price 60% produts
        price = self.products[:self.total[1]].aggregate(Max('price'))
        return int(price['price__max']) # convert decimal to int

    def bitween_price(self):
        # check if you have products bitween 30% and 60% of products
        result = self.products.filter(price__gt=self.price1(), price__lte=self.price2()).exists()
        return result

    def max_price(self):
        # take max price of products
        price = self.products.aggregate(Max('price'))
        return int(price['price__max']) # convert decimal to int

    def result_count(self):
        return self.products.count()

