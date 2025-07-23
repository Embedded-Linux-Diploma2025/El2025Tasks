"""Write a Python program to get info about your location."""

import requests


def get_info_location():
    """Write your solution here. Don't forget to return the result at the end."""
    loc_info = None
    url_response = requests.get("https://api.ipify.org/?format=json",timeout=1.0)
    ip_add_dict = url_response.json()
    ip_add = ip_add_dict.get('ip',None)
    if ip_add and isinstance(ip_add,str):
        ip_link = 'https://ipinfo.io/'+ip_add+'/geo'
        url_response = requests.get(ip_link,timeout=1.0)
        loc_info = url_response.json()
    return loc_info

if __name__ == "__main__":
    location_info = get_info_location()
    assert "ip" in location_info, "Test case failed"
    assert "city" in location_info, "Test case failed"
    assert "region" in location_info, "Test case failed"
    assert "country" in location_info, "Test case failed"
    assert "loc" in location_info, "Test case failed"
    assert "org" in location_info, "Test case failed"
