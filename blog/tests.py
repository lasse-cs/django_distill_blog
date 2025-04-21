from pytest_django.asserts import assertContains


def test_index_view_can_be_reached(client):
    """
    Test that the index view can be reached.
    """
    response = client.get("/")
    assert response.status_code == 200


def test_index_view_content(client):
    response = client.get("/")
    assertContains(response, "<title>Test Title</title>")
