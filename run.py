"""
    'pytdm' - a test data management
    This is the main run file for the application

    :copyright: (c) 2017

"""
# TODO implement the update on fetch
# TODO learn how to deploy on apache server
# TODO test the app with LR concurrency (hammer it)

from flask import request
from eve import Eve
import json


# post-request event hook to update the data after GET
def post_get_callback(resource, request, response):
    print('payload type is : ', type(response))


app = Eve()
mongo = app.data.driver


def before_returning_item(resource, response):
    print('before returning item', response)
    # response['_id'] = 'this is firstname'
    print(response['_id'])
    q = {'_id': response['_id']}
    # toggle
    if response['read']:
        u = {'$set': {'read': False}}
    else:
        u = {'$set': {'read': True}}

    mongo.db.ss_customers.update(q, u)
    print('updated')


@app.before_request
def before():
    print('the request object ready to processed', request)


@app.after_request
def after(response):
    """
    Your function must take one parameter, a `response_class` object and return
    a new response object or the same (see Flask documentation).
    """
    print('response object is here', response.status)
    print(type(response.get_data()))
    print(response.get_data())

    return response


app.on_post_GET += post_get_callback
app.on_fetched_item += before_returning_item

if __name__ == '__main__':
    app.run(debug=True)
