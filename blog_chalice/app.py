import os
import logging

import boto3
from chalice import Chalice

from chalicelib import db

app = Chalice(app_name='blog_chalice')
app.debug = True
_DB = None


@app.route('/', methods=["GET"])
def all_posts():
    print("Before")

    return {'posts': get_db().get_all_posts()}


@app.route('/', methods=["POST"])
def create_post():
    body = app.current_request.json_body
    assert body['title']
    assert body['description']
    tags = body.get("tags", "").split(",")
    post_id = get_db().create_post(
        title=body['title'],
        description=body['description'],
        tags=body.get("tags", "").split(",") if body.get("tags", "") else []
    )
    return {
        "post": post_id
    }


@app.route('/{post_id}', methods=['GET'])
def get_post(post_id):
    return get_db().get_post(post_id)


@app.route('/{post_id}', methods=['PUT'])
def update_post(post_id):
    body = app.current_request.json_body
    post_id = get_db().update_post(
        post_id=post_id,
        title=body.get('title', None),
        description=body.get('description', None),
        tags=body.get("tags", "").split(",") if body.get("tags", "") else []
    )
    return {
        "post": post_id
    }


@app.route('/{post_id}', methods=['DELETE'])
def delete_post(post_id):
    post_id = get_db().delete_post(post_id)
    return {
        "post": post_id
    }


def get_db():
    # Original idea from https://chalice-workshop.readthedocs.io/en/latest/todo-app/part1/03-todo-app-dynamodb.html
    global _DB

    if _DB is None:
        _DB = db.DynamoPosts(
            boto3.resource('dynamodb').Table(
                os.getenv('POST_TABLE_NAME', "")
            )
        )
    return _DB