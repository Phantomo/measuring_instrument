import unicodedata


def is_number(s):
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

    def __init__(self, inst_id):
        self.id = inst_id
        self.measure_types = {'thread': False,
                              'size': False,
                              'roughness': False,
                              'angle': False,
                              'deviation': False}# відхилення (індикатори)
        self.instrument_type = None
        self.model = None
        self.accuracy = None
        self.brand = None
        self.indicator_panel = 'analogue'
        self.weight = None

    def set_measuring_types(self, types):
        if types.keys() == self.measure_types.keys():
            self.measure_types = types

    def set_instrument_type(self, inst_type):
        self.instrument_type = inst_type

    def set_model(self, model):
        self.model = model

    def set_accuracy(self, accuracy):
        self.accuracy = accuracy

    def set_brand(self, brand):
        self.brand = brand

    def set_indicator_panel(self, indicator_panel):
        if indicator_panel == 'analogue' or indicator_panel == 'digital':
            self.indicator_panel = indicator_panel

    def set_weight(self, weight):
        if is_number(weight) and float(weight) > 0:
            self.weight = float(weight)

    @staticmethod
    def not_none_params(self, *args):
        for elem in args:
            if elem is None:
                return False
        return True

    def get_measuring_types(self):
        types = []
        for key, value in self.measure_types.items():
            if value == True:
                types.append(key)
        if len(types) == 0:
            return None
        return types

    def required_params(self):
        if self.not_none_params(self.id, self.instrument_type, self.accuracy) and self.get_measuring_types() is not None:
            return True
        return False
