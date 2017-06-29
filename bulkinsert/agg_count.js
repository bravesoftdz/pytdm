db.getCollection('ss_customers').aggregate({
    "$group": {"_id": {"state":"$state"}, "count": {"$sum": 1}}});
   
db.getCollection('ss_customers').aggregate({
    "$group": {"_id": "$readcount", "count": {"$sum": 1}}});