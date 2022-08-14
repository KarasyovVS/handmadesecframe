class Sorting:

    @staticmethod
    def is_sorted(input_list):
        if input_list == sorted(input_list):
            return True
        else:
            return False

    @staticmethod
    def sort_by_condition(some_list, condition):
        return some_list.sort(condition)
