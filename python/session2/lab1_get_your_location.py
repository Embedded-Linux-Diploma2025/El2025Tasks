"""Write a Python program to get info about your location."""

import requests


def get_info_location():
    """Write your solution here. Don't forget to return the result at the end."""
    ip_url = "https://api.ipify.org/?format=json"
    ip_response = requests.get(ip_url, timeout = 5)
    my_ip_dic = ip_response.json()
    my_ip = my_ip_dic['ip']
    get_loc_url = f"https://ipinfo.io/{my_ip}/geo"
    location_timezone_reponse = requests.get(get_loc_url, timeout = 5)
    my_location_timezone_dic = location_timezone_reponse.json()
    return my_location_timezone_dic

if __name__ == "__main__":
    location_info = get_info_location()
    assert "ip" in location_info, "Test case failed"
    assert "city" in location_info, "Test case failed"
    assert "region" in location_info, "Test case failed"
    assert "country" in location_info, "Test case failed"
    assert "loc" in location_info, "Test case failed"
    assert "org" in location_info, "Test case failed"
