from flask import *


class Control:
    def __init__(self):
        pass

    @staticmethod
    def show_controlpage(app):
        return render_template(
            'control.html',
            title="Control",
            app=app
        )
