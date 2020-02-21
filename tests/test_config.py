
from cs334demo.config import Config

def test_config_reads_delay_():
    config = Config()
    assert config.get_delay() == 100


# This test completely invalidates the entire point of
# putting secret data in the .env file.  It is here to
# make sure you followed the directions to set up the
# project.
def test_config_loads_secret():
    config = Config()
    assert config.get_secret() == 42
