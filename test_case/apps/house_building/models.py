from django.db import models


class House(models.Model):
    adress = models.TextField('адрес', max_length=300)
    year = models.DateTimeField('Дата потсройки')

    def get_all_bricks_in_house(self):
        return sum([ task.bricks_count for task in BrickworkTask.objects.filter(house = self)])

    def get_all_dates(self):
        return {task.date: task.bricks_count for task in BrickworkTask.objects.filter(house = self)}

    class Meta:
        verbose_name= 'Дом'
        verbose_name_plural = 'Дома'

    def __str__(self):
        return self.adress


class BrickworkTask(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    bricks_count = models.IntegerField('кол-во кирпичей')
    date = models.DateTimeField('дата кладки')

    class Meta:
        verbose_name = 'Задание на кладку'
        verbose_name_plural = 'Задания на кладку'

    def __str__(self):
        return self.house.adress
