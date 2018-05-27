from flask import *
import json
import os
from string import ascii_lowercase, digits
from random import SystemRandom


class Members:
    def __init__(self, app):
        self.id = ''.join(SystemRandom().choice(ascii_lowercase + digits) for _ in range(8))
        self.name = request.form['name']
        self.email = request.form['email']
        self.mobile = request.form['mobile']
        self.password = request.form['password']
        self.age = request.form['age']
        self.address = request.form['address']
        self.gender = request.form['gender']
        self.role = request.form['role']
        photo = request.files['photo']
        randomfilename = ''.join(SystemRandom().choice(ascii_lowercase + digits) for _ in range(32))
        photo.save(os.path.join(
            app.config['BASE_DIR'],
            app.config['UPLOADED_PHOTOS_DEST'],
            randomfilename)
        )
        self.photo = os.path.join(
            '/' + app.config['UPLOADED_PHOTOS_DEST'],
            randomfilename
        )

    @staticmethod
    def show_member(app):

        global membersid
        members = []
        with open(os.path.join(app.config['BASE_DIR'], app.config['DATA'], 'products.json'), 'r') as productfile:
            productdata = json.load(productfile)
            for product in productdata:
                if product['productid'] == session['productid']:
                    membersid = product['product_access_users_id']
                    break

        with open(os.path.join(app.config['BASE_DIR'], app.config['DATA'], 'users.json'), 'r') as userfile:
            userdata = json.load(userfile)
            for user in userdata:
                if user['id'] in membersid and not user['id'] == session['id']:
                    members.append(user)
        return render_template(
            'members.html',
            title="Members",
            members=members,
            app = app
        )

    @staticmethod
    def delete_member(app, memberid):
        with open(os.path.join(app.config['BASE_DIR'], app.config['DATA'], 'users.json'), 'r') as userfile:
            userdata = json.load(userfile)
            i = 0
            for j in range(len(userdata)):
                if userdata[j]['id'] == memberid:
                    i = j
                    break
        del userdata[i]
        with open(os.path.join(app.config['BASE_DIR'], app.config['DATA'], 'users.json'), 'w') as userfile:
            userfile.write(json.dumps(userdata))

        with open(os.path.join(app.config['BASE_DIR'], app.config['DATA'], 'products.json'), 'r') as productfile:
            productdata = json.load(productfile)
            for product in productdata:
                if product['productid'] == session['productid']:
                    i = 0
                    for j in range(len(product['product_access_users_id'])):
                        if product['product_access_users_id'][j] == memberid:
                            i = j
                    del product['product_access_users_id'][i]
                    break

        with open(os.path.join(app.config['BASE_DIR'], app.config['DATA'], 'products.json'), 'w') as productfile:
            productfile.write(json.dumps(productdata))
        return 1

    def add_member(self, app):
        memberinfo = {
            "role": self.role,
            "id": self.id,
            "email": self.email,
            "password": self.password,
            "name": self.name,
            "mobile": self.mobile,
            "gender": self.gender,
            "age": self.age,
            "address": self.address,
            "photo": self.photo,
            "productid": session['productid']
        }
        with open(os.path.join(app.config['BASE_DIR'], app.config['DATA'], 'users.json'), 'r') as usersdatafile:
            usersdata = json.load(usersdatafile)

        for users in usersdata:
            if users['email'] == self.email:
                return 'Email Exist'

        usersdata.append(memberinfo)
        with open(os.path.join(app.config['BASE_DIR'], app.config['DATA'], 'users.json'), 'w') as usersdatafile:
            usersdatafile.write(json.dumps(usersdata))

        with open(os.path.join(app.config['BASE_DIR'], app.config['DATA'], 'products.json'), 'r') as productfile:
            productdata = json.load(productfile)
            for product in productdata:
                if product['productid'] == session['productid']:
                    product['product_access_users_id'].append(self.id)
                    break

        with open(os.path.join(app.config['BASE_DIR'], app.config['DATA'], 'products.json'), 'w') as productfile:
            productfile.write(json.dumps(productdata))
