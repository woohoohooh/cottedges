from django.db import models

class Booking(models.Model):
    name = models.CharField('Имя', max_length=300)
    phone = models.CharField('Телефон', max_length=300)
    comment = models.CharField('Комментарий', max_length=300)
    def __str__(self):
        return self.name