import yaml

try:
    conf = yaml.load(open("tests/conf_test.yml", "r", encoding="utf-8"), yaml.CLoader)
except FileNotFoundError as e:
    raise FileNotFoundError(
        "ERROR: Please create a 'conf_test.yml' that follows the tempate of 'example_conf_test.yml'"
    ) from e
