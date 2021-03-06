from web_api.utils.basic_manager import BasicManager

class TopicsManager(BasicManager):
    TOPIC_LIMIT = 20
    
    def __init__(self):
        super(TopicsManager, self).__init__(str(self), __package__)
    
    def get_topics(self, limit=20):
        return super(TopicsManager, self) \
            .get_query_set(order='desc')[0:self.TOPIC_LIMIT]

    def upvote(self, id):
        topic = super(TopicsManager, self).get(id)
        topic.upvote += 1
        return topic

    def downvote(self, id):
        topic = super(TopicsManager, self).get(id)
        topic.downvote += 1
        return topic

    def __str__(self):
        '''Model'''
        return 'Topics'