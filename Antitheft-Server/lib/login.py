from flask import *
import json


class Login:
    def __init__(self, projectroot):

        self.id = request.form['id']
        self.email = request.form['email']
        self.password = request.form['password']
        self.projectroot = projectroot

    @staticmethod
    def login(self):
        with open(self.projectroot + '/data/users.json', 'r') as usersdatafile:
            usersdata = json.load(usersdatafile)

        for users in usersdata:
            if users['id'] == self.id and users['email'] == self.email and users['password'] == self.password:
                session['role'] = users['role']
                session['id'] = users['id']
                session['email'] = users['email']
                session['name'] = users['name']
                session['mobile'] = users['mobile']
                session['gender'] = users['gender']
                session['age'] = users['age']
                session['address'] = users['address']
                session['photo'] = users['photo']
                session['productid'] = users['productid']
                return 1
