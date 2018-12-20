"""
This is the iris module and supports all the ReST actions for the
iris collection
"""

# 3rd party modules
from flask import make_response, abort
from flask import request, jsonify
import pickle

def predict(sepal_length, sepal_width, petal_length, petal_width):
	c1 = [[sepal_length, sepal_width, petal_length, petal_width]]
	with open('test.pkl','rb') as file_handle:
		clf = pickle.load(file_handle)
	result = clf.predict(c1)
	return jsonify("The number is {}".format(result.tolist()))


def read_all():
    """
    This function responds to a request for /api/people
    with the complete lists of people
    :return:        json string of list of people
    """
    # Create the list of people from our data
    return [PEOPLE[key] for key in sorted(PEOPLE.keys())]
