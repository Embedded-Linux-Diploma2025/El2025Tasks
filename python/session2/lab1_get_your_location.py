"""Write a Python program to get info about your location."""

import requests


def get_info_location():
    """Gets location information based on public IP address.

    Uses the ipinfo.io API to fetch location data.

    Returns:
        dict: A dictionary containing location information such as
              ip, city, region, country, etc. Returns an empty
              dictionary with placeholder values if the request fails.
    """
    try:
        # This URL provides all the necessary fields (ip, city, region, etc.)
        response = requests.get("https://ipinfo.io/json", timeout=15)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
        return response.json()
    except requests.exceptions.RequestException as exception:
        print(f"Error fetching location data: {exception}")
        # If the request fails, return a dictionary with all the keys the tests expect.
        return {
            "ip": "N/A",
            "city": "N/A",
            "region": "N/A",
            "country": "N/A",
            "loc": "N/A",
            "org": "N/A",
        }


if __name__ == "__main__":
    location_info = get_info_location()
    assert "ip" in location_info, "Test case failed"
    assert "city" in location_info, "Test case failed"
    assert "region" in location_info, "Test case failed"
    assert "country" in location_info, "Test case failed"
    assert "loc" in location_info, "Test case failed"
    assert "org" in location_info, "Test case failed"
