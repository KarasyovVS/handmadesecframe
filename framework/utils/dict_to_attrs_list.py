class DictToAttrsList:

    @staticmethod
    def get_list_of_attrs(input_dict, attr):
        attrs_list = []
        for elem in input_dict:
            attrs_list.append(elem[attr])
        return attrs_list
