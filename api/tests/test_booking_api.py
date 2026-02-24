import pytest
from api.booking_client import BookingClient
from api.test_data import NEW_BOOKING, UPDATED_BOOKING

class TestBookingAPI:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.client = BookingClient()
        self.client.get_token()

    def test_get_booking_returns_200(self):
        response = self.client.get_booking(1)
        assert response.status_code == 200

    def test_get_booking_has_required_fields(self):
        response = self.client.get_booking(1)
        data = response.json()
        assert "firstname" in data
        assert "lastname" in data
        assert "totalprice" in data
        assert "bookingdates" in data

    def test_get_all_bookings_returns_list(self):
        response = self.client.get_all_bookings()
        assert response.status_code == 200
        assert isinstance(response.json(), list)
        assert len(response.json()) > 0

    def test_create_booking(self):
        response = self.client.create_booking(NEW_BOOKING)
        assert response.status_code == 200
        data = response.json()
        assert "bookingid" in data
        assert data["booking"]["firstname"] == "Kaoz"
        assert data["booking"]["additionalneeds"] == "Chaos"

    def test_update_booking(self):
        # create one first so we own it
        created = self.client.create_booking(NEW_BOOKING).json()
        booking_id = created["bookingid"]

        response = self.client.update_booking(booking_id, UPDATED_BOOKING)
        assert response.status_code == 200
        assert response.json()["lastname"] == "Updated"

    def test_delete_booking(self):
        created = self.client.create_booking(NEW_BOOKING).json()
        booking_id = created["bookingid"]

        delete_response = self.client.delete_booking(booking_id)
        assert delete_response.status_code == 201

        get_response = self.client.get_booking(booking_id)
        assert get_response.status_code == 404