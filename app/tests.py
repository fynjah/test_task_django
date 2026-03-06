import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from db.models import Booking, Table


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def table(db):
    return Table.objects.create(name="Table 1")


@pytest.fixture
def booking(db, table):
    return Booking.objects.create(
        table=table,
        date="2026-03-06 12:00:00",
        client_name="John Doe",
        client_phone="+380001234567",
    )


# --- /bookings/ ---

@pytest.mark.django_db
def test_list_bookings_empty(client):
    response = client.get("/bookings/")
    assert response.status_code == 200
    assert response.json() == []


@pytest.mark.django_db
def test_list_bookings_returns_data(client, booking):
    response = client.get("/bookings/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["client_name"] == "John Doe"
    assert data[0]["client_phone"] == "+380001234567"


@pytest.mark.django_db
def test_create_booking(client, table):
    payload = {
        "table_id": table.id,
        "date": "2026-03-07T14:00:00",
        "client_name": "Jane Doe",
        "client_phone": "+380007654321",
    }
    response = client.post("/bookings/", payload, format="json")
    assert response.status_code == 201
    assert Booking.objects.count() == 1


@pytest.mark.django_db
def test_create_booking_duplicate_fails(client, booking, table):
    payload = {
        "table_id": table.id,
        "date": "2026-03-06T12:00:00",
        "client_name": "Another Person",
        "client_phone": "+380000000000",
    }
    response = client.post("/bookings/", payload, format="json")
    assert response.status_code == 400


# --- /tables/ ---

@pytest.mark.django_db
def test_list_tables(client, table):
    response = client.get("/tables/")
    assert response.status_code == 200
    data = response.json()["tables"]
    assert len(data) == 1
    assert data[0]["name"] == "Table 1"


@pytest.mark.django_db
def test_list_tables_excludes_booked(client, booking, table):
    # Стіл зайнятий о 12:00 — запит на 12:30 (в межах ±2год) не повинен його повернути
    response = client.get("/tables/?date=2026-03-06T12:30:00")
    assert response.status_code == 200
    assert response.json()["tables"] == []


@pytest.mark.django_db
def test_list_tables_includes_free(client, booking, table):
    # Стіл зайнятий о 12:00 — запит на 15:00 (поза межами ±2год) повинен його повернути
    response = client.get("/tables/?date=2026-03-06T15:00:00")
    assert response.status_code == 200
    assert len(response.json()["tables"]) == 1
