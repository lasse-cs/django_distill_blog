from pathlib import Path
import pytest
import os

import http.server
import threading


from django.conf import settings
from django.core.management import call_command


# This is required to make live_server work with playwright I think...
# https://github.com/microsoft/playwright-pytest/issues/29
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"


@pytest.fixture(scope="session")
def server_url():
    class CustomHandler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, request, client_address, server):
            directory = Path(settings.DISTILL_DIR)
            super().__init__(request, client_address, server, directory=directory)

    port = 8082
    httpd = http.server.HTTPServer(("", port), CustomHandler)
    thread = threading.Thread(target=httpd.serve_forever)
    thread.start()
    yield f"http://localhost:{port}/"
    httpd.shutdown()


@pytest.fixture(scope="session")
def collect_static():
    call_command("collectstatic", "--no-input", "--clear")


def pytest_runtest_call():
    call_command("distill-local", "--quiet", "--force")
