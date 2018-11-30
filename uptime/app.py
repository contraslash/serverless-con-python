import requests
import os
from chalice import Chalice, Rate


app = Chalice(app_name='uptime')


@app.route('/hello')
def index():
    return {'hello': 'world'}


@app.schedule(Rate(1, unit=Rate.MINUTES))
def check_blog(event):
    page_to_check = "http://blog.contraslash.com/"
    response = requests.get(page_to_check)
    requests.post(
        os.getenv("SLACK_WEBHOOK_URL", ""),
        json={
            "text": "Page {} has a response {}".format(
                page_to_check,
                response.status_code
            )
        }
    )
