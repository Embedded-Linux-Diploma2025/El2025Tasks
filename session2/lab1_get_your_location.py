"""Gt info about the user's location."""

import requests


def get_info_location():
    """Get information about the user's location using an external API."""
    try:
        req = requests.get("https://ipwho.is/", timeout=5).json()
        lat = req["latitude"]
        lon = req["longitude"]
        req["loc"] = f"{lat},{lon}"
        req["org"] = req["connection"]["org"]
        return req
    except requests.RequestException as e:
        print("Network error:", e)
        return {}


if __name__ == "__main__":
    location_info = get_info_location()
    assert "ip" in location_info, "Test case failed"
    assert "city" in location_info, "Test case failed"
    assert "region" in location_info, "Test case failed"
    assert "country" in location_info, "Test case failed"
    assert "loc" in location_info, "Test case failed"
    assert "org" in location_info, "Test case failed"
