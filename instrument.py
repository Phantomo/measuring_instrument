import unicodedata
import json
from tkinter import messagebox


def is_number(s):
    if s is None:
        return False
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    return False


class Instrument(object):

    def __init__(self, database_path):
        self.database_path = database_path
        self._id = self._next_id_()
        self._measure_types = {'thread': False,
                              'size': False,
                              'roughness': False,
                              'angle': False,
                              'deviation': False}# відхилення (індикатори)
        self._instrument_type = None
        self._model = None
        self._accuracy = None
        self._brand = None
        self._indicator_panel = 'analogue'
        self._weight = None
        self._additional_inf = None

    def _next_id_(self):
        with open(self.database_path, 'r') as f:
            self.database = json.load(f)
            try:
                instrument = self.database['instrument']
                if len(instrument) > 0:
                    ins_id = instrument[-1]['id']
                else:
                    ins_id = 1
                return ins_id
            except:
                messagebox.showerror("Database error!!", "Sorry but database not exist or invalid")

    def set_measuring_types(self, types):
        if types.keys() == self._measure_types.keys():
            self._measure_types = types

    def set_instrument_type(self, inst_type):
        self._instrument_type = inst_type

    def set_model(self, model):
        self._model = model

    def set_accuracy(self, accuracy):
        self._accuracy = accuracy

    def set_brand(self, brand):
        self._brand = brand

    def set_indicator_panel(self, indicator_panel):
        if indicator_panel == 'analogue' or indicator_panel == 'digital':
            self._indicator_panel = indicator_panel

    def set_weight(self, weight):
        if is_number(weight) and float(weight) > 0:
            self._weight = float(weight)

    @staticmethod
    def not_none_params(*args):
        for elem in args:
            if elem is None:
                return False
        return True

    def get_measuring_types(self):
        types = []
        for key, value in self._measure_types.items():
            if value:
                types.append(key)
        if len(types) == 0:
            return None
        return types

    def required_params(self):
        if self.not_none_params(self._id, self._instrument_type, self._accuracy) \
                and self.get_measuring_types() is not None:
            return True
        return False

    def instrument_dict(self):
        ins = dict()
        ins['id'] = self._id
        ins['instrument_type'] = self._instrument_type
        ins['brand'] = self._brand
        ins['model'] = self._model
        ins['measuring_types'] = self._measure_types
        ins['accuracy'] = self._accuracy
        ins['indicator_panel'] = self._indicator_panel
        ins['weight'] = self._weight
        ins['additional_information'] = self._additional_inf
        return ins

    def __str__(self):
        return str(self.instrument_dict())

    def add_record(self):
        self.database['instrument'].append(self.instrument_dict())
        with open(self.database_path, 'w') as f:
            f.write(json.dumps(self.database))
