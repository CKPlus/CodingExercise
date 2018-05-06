import json

from tests.base import BaseTestCase
from web_api import app
from web_api.topics.views import TopicActions


class TopicsTestCase(BaseTestCase):
    def setUp(self):
        self.test_app = app.test_client()
        self.topic_content = 'Hello'

    def test_01_create_topic(self):
        with self.test_app as c:
            resp = c.post('/topics', data=json.dumps({
                'content': self.topic_content
            }))
            self.assert200(resp)

            # Check response
            resp_data = resp.json
            self.assertEqual(resp_data.get('id'), 0)
            self.assertEqual(resp_data.get('content'), self.topic_content)
            self.assertEqual(resp_data.get('upvote'), 0)
            self.assertEqual(resp_data.get('downvote'), 0)

            resp = c.post('/topics', data=json.dumps({
                'content': self.topic_content
            }))
            resp_data = resp.json
            self.assert200(resp)
            self.assertEqual(resp_data.get('id'), 1)

    def test_02_get_topics(self):
        with self.test_app as c:
            resp = c.get('/topics')
            self.assert200(resp)

            # Check response
            resp_data = resp.json
            self.assertEqual(len(resp_data), 2)

            for topic in resp_data:
                self.assertEqual(topic.get('content'), self.topic_content)

    def test_03_create_invalid_topic(self):
        with self.test_app as c:
            resp = c.post('/topics', data=json.dumps({
                'content': 'a' * 256
            }))
            self.assert400(resp)

            resp_data = resp.json
            self.assertEqual(
                resp_data.get('message'),
                'Content can not exceed 255 characters')

    def test_04_upvote(self):
        with self.test_app as c:
            resp = c.get('/topics')
            self.assert200(resp)
            for topic in resp.json:
                resp = c.put('/topics/{topic_id}/action/{action_id}'.format(
                    topic_id=topic.get('id'),
                    action_id=TopicActions.UPVOTE
                ))
                self.assert200(resp)
                self.assertEqual(resp.json.get('upvote'), 1)

                resp = c.put('/topics/{topic_id}/action/{action_id}'.format(
                    topic_id=topic.get('id'),
                    action_id=TopicActions.UPVOTE
                ))
                self.assert200(resp)
                self.assertEqual(resp.json.get('upvote'), 2)

    def test_05_downvote(self):
        with self.test_app as c:
            resp = c.get('/topics')
            self.assert200(resp)
            for topic in resp.json:
                resp = c.put('/topics/{topic_id}/action/{action_id}'.format(
                    topic_id=topic.get('id'),
                    action_id=TopicActions.DOWNVOTE
                ))
                self.assert200(resp)
                self.assertEqual(resp.json.get('downvote'), 1)

                resp = c.put('/topics/{topic_id}/action/{action_id}'.format(
                    topic_id=topic.get('id'),
                    action_id=TopicActions.DOWNVOTE
                ))
                self.assert200(resp)
                self.assertEqual(resp.json.get('downvote'), 2)

    def test_06_get_vote_count(self):
        with self.test_app as c:
            resp = c.get('/topics')
            self.assert200(resp)
            for topic in resp.json:
                self.assertEqual(len(resp.json), 2)
                self.assertEqual(topic.get('upvote'), 2)
                self.assertEqual(topic.get('downvote'), 2)
                self.assertEqual(topic.get('result'), 0)
