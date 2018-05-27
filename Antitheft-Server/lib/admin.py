from flask import *


class Admin:
    def __init__(self):
        pass

    @staticmethod
    def show_adminpage(app):
        return render_template(
            'admin.html',
            title="ADMIN",
            app=app
        )
