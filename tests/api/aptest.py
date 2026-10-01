import pytest


@pytest.mark.api
def test_get_users(request):

    response = request.get(
        "https://jsonplaceholder.typicode.com/users"
    )

    assert response.ok

    body = response.json()

    assert len(body) > 0