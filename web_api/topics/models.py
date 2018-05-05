from datetime import datetime

from web_api.topics.managers import TopicsManager
from web_api.utils.exceptions import TopicException


class Topics(object):
    '''Topic model'''
    manager = TopicsManager()

    def __init__(self, *args, **kwargs):
        self.id = kwargs.get('id')
        self.content = kwargs.get('content', '')
        self.upvote = kwargs.get('upvote', 0)
        self.downvote = kwargs.get('downvote', 0)
        self.ctime = datetime.utcnow()

        if len(kwargs.get('content', '')) > 255:
            raise TopicException('Content can not exceed 255 characters')

    def __str__(self):
        return 'Topic <%s>' % self.id
