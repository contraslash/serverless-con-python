from uuid import uuid4
import datetime


class DynamoPosts(object):

    def __init__(self, table_resource):
        self._table = table_resource

    def get_all_posts(self):
        response = self._table.scan()
        return response['Items']

    def create_post(self, title, description, tags):
        uid = str(uuid4())
        self._table.put_item(
            Item={
                'post_id': uid,
                'title': title,
                'description': description,
                'tags': tags,
                'created': datetime.datetime.utcnow().isoformat(),
            }
        )
        return uid

    def get_post(self, post_id):
        response = self._table.get_item(
            Key={
                'post_id': post_id,
            },
        )
        return response['Item']

    def update_post(self, post_id, title, description, tags):
        # We could also use update_item() with an UpdateExpression.
        item = self.get_post(post_id)
        if title is not None:
            item['title'] = title
        if description is not None:
            item['description'] = description
        print(tags)
        item['tags'] = tags if tags else []
        item['updated'] = datetime.datetime.utcnow().isoformat()
        self._table.put_item(Item=item)
        return post_id

    def delete_post(self, post_id):
        self._table.delete_item(
            Key={
                'post_id': post_id,
            }
        )
        return post_id