import requests

AGE_API_ENDPOINT = "https://api.agify.io"
GENDER_API_ENDPOINT = "https://api.genderize.io"


class Api:
    def __init__(self):
        pass

    def get_age(self, user_name):
        params = {
            "name": user_name,
        }
        try:
            response = requests.get(AGE_API_ENDPOINT, params=params)
            response.raise_for_status()
            age_data = response.json()
            return age_data
        except requests.RequestException as e:
            print(f"Error fetching age data for {user_name}: {e}")
            return None  # Return None or an appropriate default value

    def get_gender(self, user_name):
        params = {
            "name": user_name,
        }
        try:
            response = requests.get(GENDER_API_ENDPOINT, params=params)
            response.raise_for_status()  # Raise an error for bad responses
            gender_data = response.json()  # Parse JSON response
            return gender_data  # Return only the gender field
        except requests.RequestException as e:
            print(f"Error fetching gender data for {user_name}: {e}")
            return None  # Return None or an appropriate default value
