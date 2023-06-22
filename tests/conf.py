import yaml
import os

try:
    conf = yaml.load(open("tests/conf_test.yml", "r", encoding="utf-8"), yaml.CLoader)
except FileNotFoundError as e:

    if (
        os.environ.get("CONF_USER", None)
        and os.environ.get("CONF_PASS", None)
        and os.environ.get("CONF_URL")
    ) is not None:
        conf = {
            "url": os.environ.get("CONF_URL"),
            "username": os.environ.get("CONF_USER"),
            "password": os.environ.get("CONF_PASS")
        }

    else:
        raise FileNotFoundError(
            "ERROR: Please create a 'conf_test.yml' that follows the tempate of 'example_conf_test.yml'"
        ) from e
