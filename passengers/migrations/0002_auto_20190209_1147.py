import csv
import os

from django.conf import settings
from django.db import migrations

TICKET_CLASS = 0
SURVIVED = 1
NAME = 2
SEX = 3
AGE = 4
EMBARKED = 10


def add_passengers(apps, schema_editor):
    Passenger = apps.get_model('passengers', 'Passenger')
    titanic_dataset_file = os.path.join(settings.BASE_DIR, 'titanic.csv')
    with open(titanic_dataset_file) as dataset:
        reader = csv.reader(dataset)
        next(reader)  # ignore first row (headers)
        for entry in reader:
            sex = 'F'
            if entry[SEX] == 'male':
                sex = 'M'
            age = 0.0
            if entry[AGE]:
                try:
                    age = float(entry[AGE])
                except:
                    age = 0
            Passenger.objects.create(
                name=entry[NAME],
                sex=sex,
                survived=bool(int(entry[SURVIVED])),
                age=age,
                ticket_class=int(entry[TICKET_CLASS]),
                embarked=entry[EMBARKED],
            )


class Migration(migrations.Migration):
    dependencies = [
        ('passengers', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_passengers),
    ]
