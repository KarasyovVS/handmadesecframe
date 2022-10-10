class ListOfModelsAttrsGetter(object):

    @staticmethod
    def get_list_of_attrs(models_list, model_func):
        attrs_list = []
        for model in models_list:
            attrs_list.append(str(model_func(model)))
        return attrs_list
