import json

from flask import Blueprint, request
from web_api.utils.client_result import ClientResult
from web_api.topics.models import Topics
from datetime import datetime
from web_api.utils.exceptions import CreateTopicException

TOPICS_BP = Blueprint('topics', __name__)


@TOPICS_BP.route("", methods=['GET'])
def get_topic():
    '''Get topics list'''
    client_result = ClientResult()
    ret_data = [{
        'id': topic.id,
        'content': topic.content,
        'upvote': topic.upvote,
        'downvote': topic.downvote,
        'ctime': topic.ctime
    } for topic in Topics.manager.get_query_set()]

    client_result.data(ret_data)

    return client_result.to_json()


@TOPICS_BP.route("", methods=['POST'])
def create_topic():
    ''' Create topic '''
    req_data = json.loads(request.data)
    if 'content' not in req_data:
        raise CreateTopicException('Must have content')

    topic = Topics.manager.create(content=req_data.get('content'))
    client_result = ClientResult()
    client_result.data({'id': topic.id})

    return client_result.to_json()
