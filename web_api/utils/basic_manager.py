import importlib

from web_api import data_source


class BasicManager(object):

    def __init__(self, model_name, package_name):
        self.model_name = model_name
        self.package_name = package_name
        self.data_set = data_source.data.setdefault(model_name, [])

    def get_query_set(self):
        return self.data_set

    def create(self, **kwargs):
        module = importlib.import_module(
            '%s.models' % self.package_name)
        ModelCls = getattr(module, self.model_name)
        kwargs.setdefault('id', len(self.data_set))
        instance = ModelCls(**kwargs)
        self.data_set.append(instance)