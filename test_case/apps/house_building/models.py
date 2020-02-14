from django.db import models
from django.utils import timezone


class House(models.Model):
    address = models.TextField('адрес', max_length=300)
    year = models.DateTimeField('Дата потсройки')

    # Sum of all bricks tasks on this address, if task not is ready - no need summing
    def get_all_bricks_in_house(self):
        return sum([task.bricks_count for task in BrickworkTask.objects.filter(house=self)
                    if task.date < timezone.now()])

    # Creating a dictionary of date: bricks
    def get_all_dates(self):
        return {task.date: task.bricks_count for task in BrickworkTask.objects.filter(house=self)}

    class Meta:
        verbose_name = 'Дом'
        verbose_name_plural = 'Дома'

    def __str__(self):
        return self.address


class BrickworkTask(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    bricks_count = models.IntegerField('кол-во кирпичей')
    date = models.DateTimeField('дата кладки')

    class Meta:
        verbose_name = 'Задание на кладку'
        verbose_name_plural = 'Задания на кладку'

    def __str__(self):
        return self.house.address
