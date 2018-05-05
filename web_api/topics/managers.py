from web_api.utils.basic_manager import BasicManager

class TopicsManager(BasicManager):
    
    def __init__(self):
        super(TopicsManager, self).__init__(str(self), __package__)
    
    def get_topics(self):
        print(super(TopicsManager, self).get_query_set())

    def __str__(self):
        '''Model'''
        return 'Topics'