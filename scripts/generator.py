import os
import django
import random
from faker import Faker

# Настройка Django для работы со скриптом
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hotel_service.settings')
django.setup()

from hotel_service.hotels.models import Hotel, MetaHotel

# Инициализация Faker
fake = Faker()


# Создание тестовых данных для MetaHotel
def create_meta_hotels(n):
    meta_hotels = []
    for _ in range(n):
        id = fake.company()
        meta_hotel, created = MetaHotel.objects.get_or_create(id=id)
        meta_hotels.append(meta_hotel)
    return meta_hotels


# Функция для создания фейковых отелей
def create_hotels(n, meta_hotels):
    for _ in range(n):
        name = fake.company()
        supplier_id = fake.bothify(text='???-###')
        meta_hotel = random.choice(meta_hotels)  # Выбор случайного мета-отеля из списка
        Hotel.objects.create(name=name, supplier_id=supplier_id, meta_hotel=meta_hotel)


# Количество мета-отелей и отелей для создания
NUM_META_HOTELS = 2
NUM_HOTELS = 10

# Создание мета-отелей и отелей
meta_hotels = create_meta_hotels(NUM_META_HOTELS)
create_hotels(NUM_HOTELS, meta_hotels)

print(f"Создано {NUM_META_HOTELS} мета-отелей и {NUM_HOTELS} отелей.")
