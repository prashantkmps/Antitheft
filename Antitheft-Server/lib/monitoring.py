from flask import *

from lib.executeremotecommand import execute_command_remotely
from lib.getproductdetails import getproductdetails


class Monitoring:
    def __init__(self):
        pass

    @staticmethod
    def show_monitoringpage(app):
        product = getproductdetails(app)
        execute_command_remotely(
            hostname=product['productip'],
            username=product['username'],
            password=product['password'],
            command='sudo modprobe bcm2835-v4l2'
        )
        return render_template(
            'monitoring.html',
            title="Monitoring",
            app=app,
            productip=product['productip'],
            motionport=product['motionport']
        )

