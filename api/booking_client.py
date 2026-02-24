import requests

BASE_URL = "https://restful-booker.herokuapp.com"

class BookingClient:

    def __init__(self):
        self.base_url = BASE_URL
        self.token = None

    def get_token(self):
        response = requests.post(f"{self.base_url}/auth", json={
            "username": "admin",
            "password": "password123"
        })
        self.token = response.json()["token"]
        return self.token

    def get_booking(self, booking_id: int):
        return requests.get(f"{self.base_url}/booking/{booking_id}")

    def get_all_bookings(self):
        return requests.get(f"{self.base_url}/booking")

    def create_booking(self, payload: dict):
        return requests.post(f"{self.base_url}/booking", json=payload)

    def update_booking(self, booking_id: int, payload: dict):
        return requests.put(
            f"{self.base_url}/booking/{booking_id}",
            json=payload,
            headers={
                "Cookie": f"token={self.token}",
                "Content-Type": "application/json"
            }
        )

    def delete_booking(self, booking_id: int):
        return requests.delete(
            f"{self.base_url}/booking/{booking_id}",
            headers={"Cookie": f"token={self.token}"}
        )