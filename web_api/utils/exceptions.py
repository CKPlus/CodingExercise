class TopicException(Exception):
    ''' Exception related to topic  '''
    def __init__(self, msg):
        self.status_code = 400
        self.msg = msg

    def to_dict(self):
        return {'message': self.msg}