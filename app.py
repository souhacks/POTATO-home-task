from flask import Flask, request, jsonify
from queries import ( tweets_per_day, unique_users, avg_likes, place_ids, tweets_by_time_of_day, top_user)

app = Flask(__name__)

@app.route('/tweets/count', methods=['GET'])
def count_tweets():
    term = request.args.get('term')
    result = tweets_per_day(term)
    return jsonify(result)

@app.route('/tweets/users', methods=['GET'])
def unique_users_res():
    term = request.args.get('term')
    result = unique_users(term)
    return jsonify(result)

@app.route('/tweets/likes', methods=['GET'])
def average_likes():
    term = request.args.get('term')
    result = avg_likes(term)
    return jsonify(result)

@app.route('/tweets/places', methods=['GET'])
def places():
    term = request.args.get('term')
    result = place_ids(term)
    return jsonify(result)

@app.route('/tweets/times', methods=['GET'])
def post_times():
    term = request.args.get('term')
    result = tweets_by_time_of_day(term)
    return jsonify(result)

@app.route('/tweets/top_user', methods=['GET'])
def top_user_of_tweet():
    term = request.args.get('term')
    result = top_user(term)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)

