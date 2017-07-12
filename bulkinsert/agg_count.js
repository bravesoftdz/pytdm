db.getCollection('ss_customers').aggregate([
{$group: {
    _id: {state: "$state", readcount: "$readcount"}, 
    count:{"$sum":1}}},
{$sort: {
    "_id.state":1}},
{$project: {
    _id:0,
    state: "$_id.state", "count":1,
    readcount: "$_id.readcount",}}
])
