#!/usr/bin/python
# -*- coding: utf-8 -*-
import servers as sv

a = sv.Product('aaa333',5)
b = sv.Product('aaa433',5)
c = sv.Product('ccc333',11)
d = sv.Product('sss66',10)

svr = sv.MapServer([a, b, c, d])
Adolf = sv.Client(svr)
print(Adolf.get_total_price(3))