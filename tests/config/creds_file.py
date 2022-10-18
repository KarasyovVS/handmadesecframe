# Временное решение для хранения кред
from framework.utils.random_generator import RandomGenerator as RandGen


class Creds(object):


    CORRECT_CREDS = [
        {"login": "admin", "password": "admin"},
        {"login": "jsmith", "password": "demo1234"}
        ]
    INCORRECT_CREDS = [
        (CORRECT_CREDS[0]["login"], 
         RandGen.get_random_string(8, punctuation=False)),
        (RandGen.get_random_string(8, punctuation=False), 
            CORRECT_CREDS[0]["password"]),
        (RandGen.get_random_string(8, punctuation=False), 
            RandGen.get_random_string(8, punctuation=False)),
        (CORRECT_CREDS[0]["login"][:-1], CORRECT_CREDS[0]["password"]),
        (CORRECT_CREDS[0]["login"], CORRECT_CREDS[0]["password"][:-1]),
        (CORRECT_CREDS[0]["login"], CORRECT_CREDS[1]["password"])
        ]