"""Write a Python program to get info about your location."""

import requests


def get_info_location():
    """Write your solution here. Don't forget to return the result at the end."""
    url = requests.get("https://api.ipify.org/?format=json", verify=False)
    my_ip = url.json()["ip"]
    url_location = requests.get(f"https://ipinfo.io/{my_ip}/geo", verify=False)
    location = url_location.json()
    return location

if __name__ == "__main__":
    location_info = get_info_location()
    assert "ip" in location_info, "Test case failed"
    assert "city" in location_info, "Test case failed"
    assert "region" in location_info, "Test case failed"
    assert "country" in location_info, "Test case failed"
    assert "loc" in location_info, "Test case failed"
    assert "org" in location_info, "Test case failed"
