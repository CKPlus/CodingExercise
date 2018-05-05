from flask import Blueprint

TOPICS_BP = Blueprint('topics', __name__)


@TOPICS_BP.route("", methods=['GET'])
def get_topic():
    '''
        Get topics list
    '''
    return "Topics"
