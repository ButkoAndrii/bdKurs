from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from phonenumber_field.modelfields import PhoneNumberField
import uuid


class Person(AbstractBaseUser):
    passport = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    frame = models.CharField(max_length=20)
    phoneNumber = PhoneNumberField(unique=True, null=False, blank=False)
    age = models.PositiveIntegerField()
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=20)
    is_active = models.BooleanField(default=False)
    REQUIRED_FIELDS = ['name', 'surname', 'frame', 'phone', 'age', 'email', 'password']
    USERNAME_FIELD = 'email'

    def __str__(self):
        return str(self.email)


class QueueConscripts(models.Model):
    choices = (('dar', 'Дарницький військовий комісаріат'),
               ('dec', 'Деснянський військовий комісаріат'),
               ('dni', 'Дніпровський військовий комісаріат'))
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    department = models.CharField(max_length=3, choices=choices)
    week_day = models.CharField(max_length=2, choices=(('tu', 'tuesday'), ('th', 'thursday')))
    time = models.CharField(max_length=20)
    people = models.ForeignKey(Person, on_delete=models.PROTECT)
    busy = models.CharField(max_length=20, choices=(('', 'Вільно'), ('Зайнято', 'Зайнято')), default='Вільно')

    def __str__(self):
        return str(self.id)

