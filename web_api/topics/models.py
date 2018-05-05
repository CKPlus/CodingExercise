from web_api.topics.managers import TopicsManager

class Topics(object):
    '''Topic model'''
    manager = TopicsManager()

    def __init__(self, *args, **kwargs):
        self.id = kwargs.get('id')
        self.content = kwargs.get('content')
        self.upvote = kwargs.get('upvote')
        self.downvote = kwargs.get('downvote')
        self.ctime = kwargs.get('ctime')

    def __str__(self):
        return 'Topic <%s>' % self.id
 