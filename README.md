Test task django
---------------------

[git](https://github.com/fynjah/test_task_django)


## Залежності:

- Python 3.9+
- PostgresQL 14
-----------

## Суперкористувач:

login: admin
psw: 123
-----------

## Локальний запуск

**1. Клонувати репозиторій**
```bash
git clone https://github.com/fynjah/test_task_django
cd test_task_django
```

**2. Створити та активувати віртуальне середовище**
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

**3. Встановити залежності**
```bash
pip install -r requirements.txt
```

**4. Налаштувати змінні середовища**

Створити файл `.env` у корені проєкту:
```env
SECRET_KEY=your-secret-key
DEBUG=1
ENVIRONMENT=local
ALLOWED_HOSTS=0.0.0.0,127.0.0.1,localhost
HTTPS=0
```

**5. Застосувати міграції**
```bash
python manage.py migrate
```

**6. Запустити сервер**
```bash
python manage.py runserver
```

Сервер буде доступний за адресою: http://localhost:8000

-----------

## Генерація тестових даних

Утиліта `app/utils/generate_data.py` створює 10 столів і випадкові бронювання (1–5 на кожен стіл) в діапазоні ±7 днів від поточного часу.

Запускається через Django shell:

```bash
python manage.py shell
```

```python
from app.utils.generate_data import generate_data
generate_data()
```

-----------

## API ендпоінти

### Столи

#### `GET /tables/`
Повертає список усіх столів.

```bash
curl http://localhost:8000/tables/
```

#### `GET /tables/?date=<datetime>`
Повертає лише **вільні** столи на вказаний час (виключає столи, заброньовані в межах ±2 години від переданого часу).

`date` — дата і час у форматі ISO 8601: `YYYY-MM-DDTHH:MM:SS`

```bash
curl "http://localhost:8000/tables/?date=2026-03-07T14:00:00"
```

Приклад відповіді:
```json
[
  { "id": 1, "name": "Table 1" },
  { "id": 2, "name": "Table 2" }
]
```

---

### Бронювання

#### `GET /bookings/`
Повертає список усіх бронювань із вкладеною інформацією про стіл.

```bash
curl http://localhost:8000/bookings/
```

Приклад відповіді:
```json
[
  {
    "id": 1,
    "table": { "id": 1, "name": "Table 1" },
    "date": "2026-03-07T14:00:00",
    "client_name": "John Doe",
    "client_phone": "+380001234567"
  }
]
```

#### `POST /bookings/`
Створює нове бронювання.

| Поле | Тип | Опис |
|---|---|---|
| `table_id` | integer | ID столу |
| `date` | string | Дата і час у форматі ISO 8601 |
| `client_name` | string | Ім'я клієнта (макс. 255 символів) |
| `client_phone` | string | Телефон клієнта (макс. 20 символів) |

```bash
curl -X POST http://localhost:8000/bookings/ \
  -H "Content-Type: application/json" \
  -d '{"table_id": 1, "date": "2026-03-07T14:00:00", "client_name": "John Doe", "client_phone": "+380001234567"}'
```

```bash
curl -X POST http://localhost:8000/bookings/ \
  -H "Content-Type: application/json" \
  -d '{"table_id": 2, "date": "2026-03-08T19:30:00", "client_name": "Jane Doe", "client_phone": "+380007654321"}'
```

```bash
curl -X POST http://localhost:8000/bookings/ \
  -H "Content-Type: application/json" \
  -d '{"table_id": 1, "date": "2026-03-07T14:00:00", "client_name": "Duplicate", "client_phone": "+380000000000"}'
# -> 400 Bad Request: стіл вже заброньований на цей час
```

-----------

## Запуск тестів

**1. Встановити залежності для тестів**
```bash
pip install pytest pytest-django
```

**2. Запустити всі тести**
```bash
pytest app/tests.py -v
```
