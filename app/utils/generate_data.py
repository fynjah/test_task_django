import random
import datetime

from django.utils import timezone

from db.models import Booking, Table

FIRST_NAMES = [
    "James", "Oliver", "William", "Henry", "Charles",
    "Emma", "Charlotte", "Sophia", "Amelia", "Isabella",
    "George", "Thomas", "Edward", "Arthur", "Frederick",
    "Eleanor", "Margaret", "Alice", "Florence", "Clara",
]

LAST_NAMES = [
    "Smith", "Johnson", "Williams", "Brown", "Jones",
    "Miller", "Davis", "Wilson", "Taylor", "Anderson",
    "Thomas", "Jackson", "White", "Harris", "Martin",
]


def generate_data():
    tables = [Table(name=f"Table {i + 1}") for i in range(10)]
    Table.objects.bulk_create(tables)
    tables = list(Table.objects.all())

    now = timezone.now()
    bookings = []
    for table in tables:
        for _ in range(random.randint(1, 5)):
            try:
                name = f"{random.choice(FIRST_NAMES)} {random.choice(LAST_NAMES)}"
                delta_days = random.randint(-7, 7)
                delta_hours = random.randint(0, 23)
                delta_minutes = random.choice([0, 15, 30, 45])
                date = (now + datetime.timedelta(days=delta_days, hours=delta_hours, minutes=delta_minutes)).replace(second=0, microsecond=0)
                phone = f"+7{''.join([str(random.randint(0, 9)) for _ in range(10)])}"
                bookings.append(Booking.objects.create(table=table, date=date, client_name=name, client_phone=phone))
            except Exception as e:
                print(e)

        print(f"Generated tables: 10, bookings: {len(bookings)}")
