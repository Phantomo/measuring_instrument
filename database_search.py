import json


class DatabaseWorker(object):

    def __init__(self, database_path):
        self._database_path = database_path
        with open(self._database_path, 'r') as f:
            self._database = json.load(f)
            self._instrument = self._database['instrument']

    @staticmethod
    def list_in_key_dict(param_list, **kwargs):
        keys = kwargs.keys()
        for param in param_list:
            if param not in keys:
                return False
        return True

    def thread_search(self, **kwargs):
        if self.list_in_key_dict(['step', 'accuracy'], **kwargs):
            self.search_request()

    def search(self, **kwargs):
        if 'type' in kwargs.keys():



