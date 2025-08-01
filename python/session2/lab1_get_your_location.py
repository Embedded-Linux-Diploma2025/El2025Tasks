"""Write a Python program to get info about your location."""

import requests



def get_info_location():
    """Write your solution here. Don't forget to return the result at the end."""
    req=requests.get("https://api.ipify.org/?format=json",timeout=500).json()
    my_ip=req['ip']
    # print(my_ip)
    data_api="https://ipinfo.io/{}/geo"
    data_api=data_api.format(my_ip)
    # print(data_api)
    loc_info=requests.get(str(data_api),timeout=500).json()
    # print(loc_info)
    return loc_info


if __name__ == "__main__":
    location_info = get_info_location()
    assert "ip" in location_info, "Test case failed"
    assert "city" in location_info, "Test case failed"
    assert "region" in location_info, "Test case failed"
    assert "country" in location_info, "Test case failed"
    assert "loc" in location_info, "Test case failed"
    assert "org" in location_info, "Test case failed"
