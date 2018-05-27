from flask import *


class History:
    def __init__(self):
        pass

    @staticmethod
    def show_historypage(app):
        return render_template(
            'history.html',
            title="History",
            app=app
        )
