"""
    'pytdm' - a test data management
    This is the main run file for the application

    :copyright: (c) 2017

"""

from eve import Eve

# post-request event hook to update the data after GET
def post_get_callback(resource, request, payload):
    print(resource, request)



app = Eve()

app.on_post_GET += post_get_callback

if __name__ == '__main__':
    app.run(debug=True)