from flask import *
import json
import os
from string import ascii_lowercase, digits
from random import SystemRandom


class UpdateProfile:
    def __init__(self, app):
        self.id = request.form['id']
        self.email = request.form['email']
        self.name = request.form['name']
        self.mobile = request.form['mobile']
        self.gender = request.form['gender']
        self.age = request.form['age']
        self.address = request.form['address']
        if request.files:
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

    def update_user(self, app):
        usersdata = None
        with open(os.path.join(app.config['BASE_DIR'], app.config['DATA'], 'users.json'), 'r') as usersdatafile:
            usersdata = json.load(usersdatafile)

        for users in usersdata:
            if users['id'] == self.id:
                users['name'] = self.name
                users['email'] = self.email
                users['mobile'] = self.mobile
                users['gender'] = self.gender
                users['age'] = self.age
                users['address'] = self.address
                users['photo'] = self.photo
                break
        with open(os.path.join(app.config['BASE_DIR'], app.config['DATA'], 'users.json'), 'w') as usersdatafile:
            usersdatafile.write(json.dumps(usersdata))
        return 1
