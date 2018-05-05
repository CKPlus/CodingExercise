import json

from flask import Blueprint, request
from web_api.utils.client_result import ClientResult
from web_api.topics.models import Topics
from datetime import datetime
from web_api.utils.exceptions import TopicException

TOPICS_BP = Blueprint('topics', __name__)


class TopicActions(object):
    UPVOTE = 1
    DOWNVOTE = 2


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
    } for topic in Topics.manager.get_topics()]

    client_result.data(ret_data)

    return client_result.to_json()


@TOPICS_BP.route("", methods=['POST'])
def create_topic():
    ''' Create topic '''
    req_data = json.loads(request.data)
    if not all([req_data.get('content')]):
        raise TopicException('Must have content')

    topic = Topics.manager.create(content=req_data.get('content'))
    client_result = ClientResult()
    client_result.data({
        'id': topic.id,
        'content': topic.content,
        'upvote': topic.upvote,
        'downvote': topic.downvote,
        'ctime': topic.ctime
    })

    return client_result.to_json()


@TOPICS_BP.route("/<int:topic_id>/action/<int:action_id>", methods=['PUT'])
def update_topic(topic_id, action_id):
    ''' Vote to topic by action'''
    if action_id not in [TopicActions.UPVOTE, TopicActions.DOWNVOTE]:
        raise TopicException('Wrong action_id. Must be `1` or `2`')

    try:
        if action_id == TopicActions.UPVOTE:
            topic = Topics.manager.upvote(topic_id)
        elif action_id == TopicActions.DOWNVOTE:
            topic = Topics.manager.downvote(topic_id)
    except IndexError:
        raise TopicException('No such topic id')

    client_result = ClientResult()
    client_result.data({
        'id': topic.id,
        'content': topic.content,
        'upvote': topic.upvote,
        'downvote': topic.downvote,
    })

    return client_result.to_json()
