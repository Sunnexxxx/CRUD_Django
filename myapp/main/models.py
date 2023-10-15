from django.db import models


class Burger(models.Model):
    name = models.CharField('Название', max_length=50)
    meat = models.BooleanField('Говядина')
    chicken = models.BooleanField('Курица')
    cheese = models.BooleanField('Сыр')
    tomato = models.BooleanField('Помидоры')
    price = models.IntegerField('Цена')

    def __str__(self):
        return '{} - {} - {}'.format(self.id, self.name, self.price)
