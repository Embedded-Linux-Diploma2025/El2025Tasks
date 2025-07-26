"""Write a Python program to get info about your location."""

import requests


def get_info_location():
    """Get IP-based location information."""
    url = requests.get("https://api.ipify.org/?format=json", timeout=5)
    ip = str(url.json()['ip'])
    print(f"ip = {ip}")
    info = requests.get(f"https://ipinfo.io/{ip}/geo", timeout=5).json()
    return info

if __name__ == "__main__":
    location_info = get_info_location()
    assert "ip" in location_info, "Test case failed"
    assert "city" in location_info, "Test case failed"
    assert "region" in location_info, "Test case failed"
    assert "country" in location_info, "Test case failed"
    assert "loc" in location_info, "Test case failed"
    assert "org" in location_info, "Test case failed"
