import requests

BASE_URL = "http://localhost:8080"

def test_mutual_follow_true():
    payload = {
        "id_user_1": 3,
        "id_user_2": 4
    }

    response = requests.post(f"{BASE_URL}/check-follow", json=payload)
    print("Test: Mutual Follow True")
    print("Status Code:", response.status_code)
    print("Response:", response.json())
    print()

def test_missing_fields():
    payload = {
        "id_user_1": 3
    }

    response = requests.post(f"{BASE_URL}/check-follow", json=payload)
    print("Test: Missing Fields")
    print("Status Code:", response.status_code)
    print("Response:", response.json())
    print()

def test_invalid_ids():
    payload = {
        "id_user_1": "abc",
        "id_user_2": "xyz"
    }

    response = requests.post(f"{BASE_URL}/check-follow", json=payload)
    print("Test: Invalid IDs")
    print("Status Code:", response.status_code)
    print("Response:", response.json())
    print()


if __name__ == "__main__":
    test_mutual_follow_true()
    test_missing_fields()
    test_invalid_ids()
