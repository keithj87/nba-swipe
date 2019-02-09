"""This module will serve the api request."""

from config import db
from app import app
from bson.json_util import dumps
from flask import request, jsonify
import json
import ast
import imp
import pdb


# Import the helpers module
helper_module = imp.load_source('*', './app/helpers.py')

# Select the collection
collection = db.users

@app.route("/")
def get_initial_response():
    """Welcome message for the API."""
    # Message to the user
    message = {
        'apiVersion': 'v1.0',
        'status': '200',
        'message': 'Welcome to the Flask API'
    }
    # Making the message looks good
    resp = jsonify(message)
    # Returning the object
    print("hello world /")
    return resp

@app.route("/api/v1/matchups", methods=['GET'])
def fetch_matchups():
    """
       Function to fetch the users.
       """
    try:
        print("hello world /matchups")
        collection = db.season_stats
        # Call the function to get the query params
        query_params = helper_module.parse_query_params(request.query_string)
        print("hello world after query_params")
        # Check if dictionary is not empty
        print(query_params)
        if query_params:
            print(query)
            # Try to convert the value to int
            query = {k: int(v) if isinstance(v, str) and v.isdigit() else v for k, v in query_params.items()}
            query["Year"] = {"$in": ['2000', ' 2001', ' 2002', ' 2003', ' 2004', ' 2005', ' 2006', ' 2007', ' 2008', ' 2009', ' 2010', ' 2011', ' 2012', ' 2013', ' 2014', ' 2015', ' 2016', ' 2017']}
            print(query)
            # Fetch all the record(s)
            records_fetched = collection.find(query)

            # Check if the records are found
            if records_fetched.count() > 2:
                print("hello world")
                # Prepare the response
                return dumps(records_fetched[0:2])
            else:
                # No records are found
                return "", 404

        # If dictionary is empty
        else:
            # Return all the records as query string parameters are not available
            if collection.find().count > 0:
                # Prepare response if the users are found
                return dumps(collection.find())
            else:
                # Return empty array if no users are found
                return jsonify([])
    except:
        # Error while trying to fetch the resource
        # Add message for debugging purpose
        return "", 500

@app.route("/api/v1/players", methods=['GET'])
def fetch_players():
    """
       Function to fetch the users.
       """
    try:
        collection = db.players
        # Call the function to get the query params
        query_params = helper_module.parse_query_params(request.query_string)
        # Check if dictionary is not empty
        pdb.set_trace()
        if query_params:

            # Try to convert the value to int
            query = {k: int(v) if isinstance(v, str) and v.isdigit() else v for k, v in query_params.items()}

            # Fetch all the record(s)
            records_fetched = collection.find(query)

            # Check if the records are found
            if records_fetched.count() > 0:
                # Prepare the response
                return dumps(records_fetched)
            else:
                # No records are found
                return "", 404

        # If dictionary is empty
        else:
            # Return all the records as query string parameters are not available
            if collection.find().count > 0:
                # Prepare response if the users are found
                return dumps(collection.find())
            else:
                # Return empty array if no users are found
                return jsonify([])
    except:
        # Error while trying to fetch the resource
        # Add message for debugging purpose
        return "", 500

@app.route("/api/v1/season_stats", methods=['GET'])
def fetch_season_stats():
    """
       Function to fetch season stats.
       """
    try:
        collection.season_stats
        # Call the function to get the query params
        query_params = helper_module.parse_query_params(request.query_string)
        # Check if dictionary is not empty
        #pdb.set_trace()
        if query_params:

            # Try to convert the value to int
            query = {k: int(v) if isinstance(v, str) and v.isdigit() else v for k, v in query_params.items()}

            # Fetch all the record(s)
            records_fetched = collection.find(query)

            # Check if the records are found
            if records_fetched.count() > 0:
                # Prepare the response
                return dumps(records_fetched)
            else:
                # No records are found
                return "", 404

        # If dictionary is empty
        else:
            # Return all the records as query string parameters are not available
            if collection.find().count > 0:
                # Prepare response if the users are found
                return dumps(collection.find())
            else:
                # Return empty array if no users are found
                return jsonify([])
    except:
        # Error while trying to fetch the resource
        # Add message for debugging purpose
        return "", 500

@app.errorhandler(404)
def page_not_found(e):
    """Send message to the user with notFound 404 status."""
    # Message to the user
    message = {
        "err":
            {
                "msg": "This route is currently not supported. Please refer API documentation."
            }
    }
    # Making the message looks good
    resp = jsonify(message)
    # Sending OK response
    resp.status_code = 404
    # Returning the object
    return resp
