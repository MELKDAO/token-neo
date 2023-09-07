import pytest
from boa3_test.test_drive.testrunner.neo_test_runner import NeoTestRunner


@pytest.fixture(scope="module")
def neo_test_runner():
    neoxp_folder = '/home/lorenzobattistela/Code/melk-token/melk-token/neo/default.neo-express'
    runner = NeoTestRunner(neoxp_folder)
    yield runner
    # Add any cleanup code here if needed after the test is done.


def pytest_configure(config):
    # Perform any setup tasks you want to run before the tests start here.
    pass
