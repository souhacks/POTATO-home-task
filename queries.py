from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['twitter_database']  # Database
collection = db['tweets']  # Collection

# Function to count tweets by a term on each day
def tweets_per_day(term):
    pipeline = [
        {'$match': {'text': {'$regex': term, '$options': 'i'}}},
        {'$group': {'_id': {'$substr': ['$created_at', 0, 10]}, 'count': {'$sum': 1}}},
        {'$sort': {'_id': 1}}
    ]
    result = list(collection.aggregate(pipeline))
    return result

# Function to get the number of unique users who tweeted a term
def unique_users(term):
    pipeline = [
        {'$match': {'text': {'$regex': term, '$options': 'i'}}},
        {'$group': {'_id': '$author_id'}},
        {'$group': {'_id': None, 'unique_users': {'$sum': 1}}}
    ]
    result = list(collection.aggregate(pipeline))
    return result[0]['unique_users'] if result else 0


# Function to get the average likes for tweets containing a term
def avg_likes(term):
    pipeline = [
        {"$match": {"text": {"$regex": term, "$options": "i"}}},
        {"$group": {"_id": None, "avg_likes": {"$avg": "$like_count"}}}
    ]
    result = collection.aggregate(pipeline)
    return list(result)[0]['avg_likes'] if result else 0

# Function to get places from tweets containing a term
def place_ids(term):
    pipeline = [
        {'$match': {'text': {'$regex': term, '$options': 'i'}, 'place_id': {'$ne': None}}},
        {'$group': {'_id': '$place_id', 'count': {'$sum': 1}}},
        {'$sort': {'count': -1}}
    ]
    result = list(collection.aggregate(pipeline))
    return result


# Function to get the times of day tweets were posted
def tweets_by_time_of_day(term):
    pipeline = [
        {'$match': {'text': {'$regex': term, '$options': 'i'}}},
        {'$group': {'_id': {'$hour': {'date': '$created_at'}}, 'count': {'$sum': 1}}},
        {'$sort': {'_id': 1}}
    ]
    result = list(collection.aggregate(pipeline))
    return result


# Function to find the user who posted the most tweets containing a term
def top_user(term):
    pipeline = [
        {'$match': {'text': {'$regex': term, '$options': 'i'}}},
        {'$group': {'_id': '$author_handle', 'count': {'$sum': 1}}},
        {'$sort': {'count': -1}},
        {'$limit': 1}
    ]
    result = list(collection.aggregate(pipeline))
    return result[0] if result else None


