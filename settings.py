"""
    'pytdm' - a test data management
    settings file for eve application

    PLEASE NOTE: We don't need to create the two collections in MongoDB.
    Actually, we don't even need to create the database: GET requests on an
    empty/non-existent DB will be served correctly ('200' OK with an empty
    collection); DELETE/PATCH will receive appropriate responses ('404' Not
    Found), and POST requests will create database and collections when needed.
    Keep in mind however that such an auto-managed database will most likely
    perform poorly since it lacks any sort of optimized index.

    :author: Dinanath Basumatary
    :inspired by: Nicola Iarocci
    :copyright: (c) 2017

"""

MONGO_HOST = 'localhost'
MONGO_PORT = 27017
# MONGO_USERNAME = 'user'
# MONGO_PASSWORD = 'user'
MONGO_DBNAME = 'racq_data'

SCHEMA_ENDPOINT = 'schema'

# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET', 'POST']
# Enable reads (GET), edits (PATCH), replacements (PUT) and deletes of
# individual items  (defaults to read-only item access).
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

# Resource customization
ss_customers = {
    # Item title should be ss_customer by default. It can be overridden by following
    # 'item_title': 'customer',

    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'state',
    },

    # We don't need cache control since we need the latest data every time the request is made
    # overriding resource methods
    # 'resource_methods': ['GET', 'POST'],

    # schema definition
    'schema': {
        'firstname': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 20,
            'required': True,
        },
        'lastname': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 20,
            'required': True,
        },
        'email': {
            'type': 'string',
            'minlength': 5,
            'maxlength': 50,
            'unique': True,
            'required': True,
        },
        'state': {
            'type': 'string',
            # 'type': 'list',
            'allowed': ["rsa", "ren", "bp09", "bp15", "rmb", "doc"],
            'required': True,
        },
        'read': {
            'type': 'boolean',
            'default': False
        },
        # Eve takes care of inserted/updated field
        # 'inserted': {
        #     'type': 'datetime'
        # }
    }

}

hosts = {
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'name',
    },
    'resource_methods': ['GET', 'POST'],
    'schema': {
        'name': {
            'type': 'string',
            'required': True
        },
        'ss_host': {
            'type': 'string',

        },
        'janrain_host': {
            'type': 'string',

        },
        'cc_host': {
            'type': 'string',

        },
        'mrm_host': {
            'type': 'string',

        }
    }
}


# Domain specifications
DOMAIN = {
    'ss_customers': ss_customers,
    'hosts': hosts,
    'cc_users': {},
}