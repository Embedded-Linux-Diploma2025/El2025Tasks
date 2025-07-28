"""Write a Python program to get info about your location."""

import requests


def get_info_location():
    """Write your solution here. Don't forget to return the result at the end."""
    ip = requests.get("https://api.ipify.org/?format=json", timeout= 3)
    print(ip.json())
    location = requests.get("https://ipinfo.io/193.83.181.21/geo/json", timeout=3)
    print(location.json())
    data = location.json()
    return data

if __name__ == "__main__":
    location_info = get_info_location()
    assert "ip" in location_info, "Test case failed"
    assert "city" in location_info, "Test case failed"
    assert "region" in location_info, "Test case failed"
    assert "country" in location_info, "Test case failed"
    assert "loc" in location_info, "Test case failed"
    assert "org" in location_info, "Test case failed"
