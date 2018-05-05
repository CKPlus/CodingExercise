from web_api.topics.managers import TopicsManager
from datetime import datetime

class Topics(object):
    '''Topic model'''
    manager = TopicsManager()

    def __init__(self, *args, **kwargs):
        self.id = kwargs.get('id')
        self.content = kwargs.get('content', '')
        self.upvote = kwargs.get('upvote', 0)
        self.downvote = kwargs.get('downvote', 0)
        self.ctime = datetime.utcnow()

    def __str__(self):
        return 'Topic <%s>' % self.id
 