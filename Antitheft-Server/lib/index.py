from flask import *


class Index:
    def __init__(self):
        pass

    @staticmethod
    def show_indexpage(app):
        global render_to
        try:
            user = session['id']
            render_to = 'admin.html'
        except KeyError:
            render_to = 'index.html'

        return render_template(
            render_to,
            title="Anti-theft Pro",
            message='Prateek',
            app=app
        )

    @staticmethod
    def show_aboutpage(app):
        return render_template(
            'about.html',
            title="About | Antitheft Pro",
            app=app
        )

    @staticmethod
    def show_teampage(app):
        return render_template(
            'team.html',
            title="Team | Antitheft Pro",
            app=app
        )

    @staticmethod
    def show_contactpage(app):
        return render_template(
            'contact.html',
            title="Contact | Antitheft Pro",
            app=app
        )
