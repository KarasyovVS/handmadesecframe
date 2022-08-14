class CompareLists:

    @staticmethod
    def compare_lists(first_list, second_list):
        if len(first_list) != len(second_list):
            return False
        for i in range(len(first_list)):
            if first_list[i] != second_list[i]:
                return False
        return True
