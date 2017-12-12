import json


class DatabaseWorker(object):

    def __init__(self, database_path):
        self._database_path = database_path
        with open(self._database_path, 'r') as f:
            self._database = json.load(f)
            self._instrument = self._database['instrument']

    @staticmethod
    def list_in_key_dict(param_list, param_dict):
        keys = param_dict.keys()
        for param in param_list:
            if param not in keys:
                return False
        return True

    def thread_search(self, param_dict):
        if self.list_in_key_dict(['step', 'accuracy'], param_dict):
            self.search_request(param_dict)

    @staticmethod
    def measuring_type(db_item_type, need_type_param):
        for key, value in db_item_type:
            if key == need_type_param and value == True:
                return True
        return False

    @staticmethod
    def suitable(instrument, param):
        instrument_keys = instrument.keys()
        param_keys = param.keys()
        # if 'accuracy' in param_keys and 'accuracy' in instrument_keys and float(param['accuracy']) >= float(instrument['accuracy']):
        #


    def search_request(self, param):
        instrument_list = []
        for item in self._database:
            if self.measuring_type(item['measuring_type'], param['type']) and self.suitable(item, param=param):
                instrument_list.append(item)

    # def search(self, param_dict):
    #     if 'type' in param_dict.keys():

    def search(self, **kwargs):
        if 'type' in kwargs.keys():
            type_search = kwargs['type']
            if type_search == 'thread':
                self.thread_search(**kwargs)
            elif type_search == 'size':
                self.size_search(**kwargs)
            elif type_search == 'roughness':
                self.roughness_search(**kwargs)
            elif type_search == 'angle':
                self.angle_search(**kwargs)

