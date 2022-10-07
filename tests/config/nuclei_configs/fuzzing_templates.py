class FuzzingTemplates(object):

    ALL_TEMPLATES_CMD = "-t fuzzing/ -itags fuzz"
    EXCLUDE_TEMPLATES_CMD = "-et {templates}"
    EXCLUDED_TEMPLATES = \
        "fuzzing/cache-poisoning-fuzz.yaml," \
        "fuzzing/header-command-injection.yaml," \
        "fuzzing/valid-gmail-check.yaml," \
        "fuzzing/wordpress-plugins-detect.yaml," \
        "fuzzing/wordpress-themes-detect.yaml," \
        "fuzzing/wordpress-weak-credentials.yaml"
