from django.test import TestCase
from .models import House, BrickworkTask
# Create your tests here.


class HouseTestCase(TestCase):

    def setUp(self):
        self.first_house = House.objects.create(
            address="Гурьевский пр кв 333", year="1900-11-11 00:00")
        self.first_task = BrickworkTask.objects.create(
            house=self.first_house, bricks_count=100, date="2020-11-11 00:00")
        self.second_task = BrickworkTask.objects.create(
            house=self.first_house, bricks_count=200, date="2021-11-11 00:00")
        self.third_task = BrickworkTask.objects.create(
            house=self.first_house, bricks_count=200, date="2019-11-11 00:00")

    def test_all_bricks_for_house(self):
        """Проверяем сумму кирпичей, если дата задания больше сегодняшнего числа,
         добавлятся не должно т.к задание еще не готово"""

        self.assertEqual(House.get_all_bricks_in_house(self.first_house), 200)
