import random
import string


class RandomGenerator:

    @staticmethod
    def get_random_string(length, lowercase=True, uppercase=True,
                          digits=True, punctuation=True,
                          string_to_check_including="",
                          num_of_included_elems=0):
        result = ""
        if num_of_included_elems > length:
            raise IndexError
        else:
            while len(result) < num_of_included_elems:
                result += random.choice(string_to_check_including)
        while len(result) < length:
            if lowercase:
                result += random.choice(string.ascii_lowercase)
            if uppercase:
                result += random.choice(string.ascii_uppercase)
            if digits:
                result += random.choice(string.digits)
            if punctuation:
                result += random.choice(string.punctuation)
        if len(result) > length:
            result = result[:length]
        result_list = result.split()
        random.shuffle(result_list)
        result = ''.join(result_list)
        return result

    @staticmethod
    def get_random_int(max_value, exceptions=[], min_value=0):
        result_range = list(range(min_value, max_value + 1))
        for elem in exceptions:
            result_range.remove(elem)
        choice = random.choice(result_range)
        return choice

    @staticmethod
    def get_random_from_list(input_list):
        return random.choice(input_list)
