db.getCollection('ss_customers').updateMany({"readcount":1},{"$set":{"readcount":0}})