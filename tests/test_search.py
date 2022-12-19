import pytest


@pytest.mark.parametrize(("start_station", "end_station", "message"), (
    ("", "Berlin", b"Missing Start"),
    ("Brandenburg Altstadt \n", "", b"Missing End"),
    ("Aschersleben \n", "Berlin \n", b""),
))
def test_search(client, start_station, end_station, message):
    assert client.get("/search").status_code == 200
    response = client.post(
        "/search",
        data={"start_station": start_station, "end_station": end_station}
    )
    assert message in response.data


def test_search_route():
    pass
