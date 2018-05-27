import json
import os

from flask import *


def getproductdetails(app):
    productdata = None
    with open(os.path.join(app.config['BASE_DIR'], 'data', 'products.json'), 'r') as productfile:
        products = json.load(productfile)
    for product in products:
        if product['productid'] == session['productid']:
            productdata = product
            break
    return productdata
