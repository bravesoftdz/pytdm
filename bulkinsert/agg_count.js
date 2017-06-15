db.getCollection('ss_customers').aggregate({
    "$group": {"_id": "$state", "count": {"$sum": 1}}})