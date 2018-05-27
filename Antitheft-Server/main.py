import os
from multiprocessing import Process

import urllib3
from flask import *

from lib.admin import Admin
from lib.control import Control
from lib.executeremotecommand import execute_command_remotely
from lib.getproductdetails import getproductdetails
from lib.history import History
from lib.index import Index
from lib.login import Login
from lib.members import Members
from lib.monitoring import Monitoring
from lib.updateuserprofile import UpdateProfile

app = Flask(__name__)


def update_session(dataobj):
    if dataobj.email:
        session['email'] = dataobj.email
    if dataobj.name:
        session['name'] = dataobj.name
    if dataobj.mobile:
        session['mobile'] = dataobj.mobile
    if dataobj.gender:
        session['gender'] = dataobj.gender
    if dataobj.age:
        session['age'] = dataobj.age
    if dataobj.address:
        session['address'] = dataobj.address
    if dataobj.photo:
        session['photo'] = dataobj.photo


@app.route('/')
def index():
    return Index.show_indexpage(app)


@app.route('/about')
def about():
    return Index.show_aboutpage(app)


@app.route('/team')
def team():
    return Index.show_teampage(app)


@app.route('/contact')
def contact():
    return Index.show_contactpage(app)


@app.route('/history')
def history():
    return History.show_historypage(app)


@app.route('/monitoring')
def monitoring():
    return Monitoring.show_monitoringpage(app)


@app.route('/control')
def control():
    return Control.show_controlpage(app)


@app.route('/admin')
def admin():
    try:
        id = session['id']
        return Admin.show_adminpage(app)
    except KeyError:
        return make_response(
            render_template("error.html"),
            404
        )


@app.route('/showmembers')
def showmembers():
    return Members.show_member(app)


@app.route('/deletemember/<memberid>')
def deletemember(memberid):
    if not Members.delete_member(app, memberid):
        flash('Deletion Unsuccessful')
    return redirect(url_for('showmembers'))


@app.route('/addmember', methods=['POST'])
def addmember():
    message = Members.add_member(Members(app), app)
    if message:
        flash(message)
    return redirect(url_for('showmembers'))


@app.route('/login', methods=['POST'])
def login_user():
    login = Login(BASE_DIR)
    found = Login.login(login)
    if not found:
        flash('Incorrect Details')
        return redirect(url_for('index'))
    else:
        return redirect(url_for('admin'))


@app.route('/logout')
def logout():
    session.pop('id', None)
    session.pop('email', None)
    return redirect(url_for('index'))


@app.route('/enablesystem')
def enablesystem():
    product = getproductdetails(app)
    http = urllib3.PoolManager()
    r = http.request('GET',
                     'http://' + product['productip'] + ':' + product['serverport'] + '/enablesystem?secretkey=' +
                     product['secretkey'])
    return make_response(r.data.decode('utf-8'))


@app.route('/disablesystem')
def disablesystem():
    product = getproductdetails(app)
    http = urllib3.PoolManager()
    r = http.request('GET',
                     'http://' + product['productip'] + ':' + product['serverport'] + '/disablesystem?secretkey=' +
                     product['secretkey'])
    return make_response(r.data.decode('utf-8'))


@app.route('/isenablesystem')
def isenablesystem():
    product = getproductdetails(app)
    http = urllib3.PoolManager()
    r = http.request('GET',
                     'http://' + product['productip'] + ':' + product['serverport'] + '/isenablesystem?secretkey=' +
                     product['secretkey'])
    return make_response(r.data.decode('utf-8'))


@app.route('/startserver')
def startserver():
    product = getproductdetails(app)
    command = 'cd ' + os.path.join(product['serverdir'], 'Antitheft-Client') + ';python3 main.py'

    def executecommandserver():
        execute_command_remotely(
            hostname=product['productip'],
            username=product['username'],
            password=product['password'],
            command=command
        )

    Process(target=executecommandserver).start()
    return make_response('success')


@app.route('/updateuserprofile', methods=['POST'])
def update_user():
    update = UpdateProfile(app)
    success = UpdateProfile.update_user(update, app)
    if not success:
        flash('Submission Failed! Please Contact to admin')
    else:
        update_session(update)
    return redirect(url_for('admin'))


@app.errorhandler(404)
def not_found(error):
    print(error)
    return make_response(
        render_template('error.html'),
        404
    )


if __name__ == '__main__':
    EMAIL = 'proantitheft@gmail.com'
    PASSWORD = 'sciencesciences8307'
    FACEBOOK = ''
    TWITTER = ''
    GOOGLE = ''
    BASE_DIR = os.path.dirname(os.path.realpath(__file__))
    UPLOADED_PHOTOS_DEST = 'static/usersData/images'
    DATA = 'data'
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
    app.config['BASE_DIR'] = BASE_DIR
    app.config['UPLOADED_PHOTOS_DEST'] = UPLOADED_PHOTOS_DEST
    app.config['DATA'] = DATA
    app.config['EMAIL'] = EMAIL
    app.config['PASSWORD'] = PASSWORD
    app.config['FACEBOOK'] = FACEBOOK
    app.config['TWITTER'] = TWITTER
    app.config['GOOGLE'] = GOOGLE

    app.run('0.0.0.0', 5000, True)
