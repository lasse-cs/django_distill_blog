import pytest

from django.core.management import call_command


@pytest.fixture(scope="session")
def server_url():
    # In future, might be nice to autolaunch the server here
    return "http://localhost:8080/"


@pytest.fixture(scope="session")
def collect_static():
    call_command("collectstatic", "--no-input", "--clear")


@pytest.fixture(scope="function")
def distill(collect_static):
    call_command("distill-local", "--quiet", "--force")
