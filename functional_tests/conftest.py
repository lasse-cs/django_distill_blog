import pytest
import os


from django.core.management import call_command


# This is required to make live_server work with playwright I think...
# https://github.com/microsoft/playwright-pytest/issues/29
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"


@pytest.fixture(scope="session")
def server_url():
    # In future, might be nice to autolaunch the server here
    # currently it is launched with something like `uv run -m http.server 8080 -d ./output/`
    return "http://localhost:8080/"


@pytest.fixture(scope="session")
def collect_static():
    call_command("collectstatic", "--no-input", "--clear")


@pytest.fixture(scope="function", autouse=True)
def distill(collect_static, articles, about_page, tagged_articles):
    call_command("distill-local", "--quiet", "--force")
