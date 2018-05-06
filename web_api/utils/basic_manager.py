import importlib

from web_api import data_source


class BasicManager(object):

    def __init__(self, model_name, package_name):
        self.model_name = model_name
        self.package_name = package_name
        self.data_set = data_source.data.setdefault(model_name, [])

    def get_query_set(self, **kwargs):
        ret = []
        if kwargs.get('order') == 'desc':
            ret = sorted(self.data_set, key=lambda topic: topic.upvote, reverse=True)
        elif kwargs.get('order') == 'asc':
            ret = sorted(self.data_set, key=lambda topic: topic.upvote, reverse=False)
        return ret

    def create(self, **kwargs):
        module = importlib.import_module(
            '%s.models' % self.package_name)
        ModelCls = getattr(module, self.model_name)
        kwargs.setdefault('id', len(self.data_set))
        instance = ModelCls(**kwargs)
        self.data_set.append(instance)

        return instance

    def update(self, **kwargs):
        instance = self.data_set[kwargs.get('id')]
        for k in kwargs:
            setattr(instance, k, kwargs.get(k))

        return instance

    def get(self, id):
        return self.data_set[id]
