import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

BASE_URL = "https://restful-booker.herokuapp.com"

class BookingClient:

    def __init__(self):
        self.base_url = BASE_URL
        self.token = None
        self.session = self._create_session()

    def _create_session(self):
        session = requests.Session()
        retry = Retry(
            total=3,
            backoff_factor=2,
            status_forcelist=[500, 502, 503, 504]
        )
        adapter = HTTPAdapter(max_retries=retry)
        session.mount("https://", adapter)
        session.mount("http://", adapter)
        return session

    def get_token(self):
        response = self.session.post(
            f"{self.base_url}/auth",
            json={"username": "admin", "password": "password123"},
            timeout=30
        )
        self.token = response.json()["token"]
        return self.token

    def get_booking(self, booking_id: int):
        return self.session.get(
            f"{self.base_url}/booking/{booking_id}",
            timeout=30
        )

    def get_all_bookings(self):
        return self.session.get(
            f"{self.base_url}/booking",
            timeout=30
        )

    def create_booking(self, payload: dict):
        return self.session.post(
            f"{self.base_url}/booking",
            json=payload,
            timeout=30
        )

    def update_booking(self, booking_id: int, payload: dict):
        return self.session.put(
            f"{self.base_url}/booking/{booking_id}",
            json=payload,
            headers={
                "Cookie": f"token={self.token}",
                "Content-Type": "application/json"
            },
            timeout=30
        )

    def delete_booking(self, booking_id: int):
        return self.session.delete(
            f"{self.base_url}/booking/{booking_id}",
            headers={"Cookie": f"token={self.token}"},
            timeout=30
        )