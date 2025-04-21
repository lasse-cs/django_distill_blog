from pytest_django.asserts import assertTemplateUsed


def test_index_view_uses_correct_template(client):
    """
    Test that the index view can be reached.
    """
    response = client.get("/")
    assert response.status_code == 200
    assertTemplateUsed(response, "blog/index.html")
