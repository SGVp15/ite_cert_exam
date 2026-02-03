import unittest
import datetime
from freezegun import freeze_time

# Предположим, у нас есть класс или объект с полем date_exam
class User:
    def __init__(self, date_exam):
        self.date_exam = date_exam

def is_exam_passed_two_days(u):
    # Ваше условие
    if datetime.datetime.now() >= u.date_exam + datetime.timedelta(days=2):
        return True
    return False

class TestExamCondition(unittest.TestCase):
    def setUp(self):
        # Устанавливаем дату экзамена: 1 января 2024, 10:00
        self.date_exam = datetime.datetime(2024, 1, 1, 10, 0, 0)
        self.user = User(self.date_exam)
        # Порог (date_exam + 2 дня) = 3 января 2024, 10:00

    @freeze_time("2024-01-03 09:59:59")
    def test_before_two_days(self):
        """Проверка: прошло чуть меньше 2 суток (должно быть False)"""
        self.assertFalse(is_exam_passed_two_days(self.user))

    @freeze_time("2024-01-03 10:00:00")
    def test_exactly_two_days(self):
        """Проверка: прошло ровно 2 суток (должно быть True, так как >=)"""
        self.assertTrue(is_exam_passed_two_days(self.user))

    @freeze_time("2024-01-03 10:00:01")
    def test_after_two_days(self):
        """Проверка: прошло чуть больше 2 суток (должно быть True)"""
        self.assertTrue(is_exam_passed_two_days(self.user))

    @freeze_time("2024-01-05 12:00:00")
    def test_long_after(self):
        """Проверка: прошло много времени (должно быть True)"""
        self.assertTrue(is_exam_passed_two_days(self.user))

if __name__ == '__main__':
    unittest.main()