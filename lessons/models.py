from django.db import models


class Lesson(models.Model):
    test = models.FloatField()  # Число с плавающей точкой
    name = models.CharField("Название", max_length=150)  # Строка максимальной длины 150 символов
    count = models.IntegerField("Кол-во", default=10)  # Целое число
    preview = models.TextField("Превью", null=True, blank=True, default='')  # Неограниченный текст
    date_create = models.DateField("Дата создания", auto_now=True)  # Дата
    date_update = models.DateTimeField("Дата последнего изменения", auto_now=True)  # Дата и время
    is_true = models.BooleanField("Это правда?", default=False)  # Булевое значение

    class Meta:
        verbose_name = "Урок 5"
        verbose_name_plural = "Уроки"

    def __str__(self):
        return "{} {}".format(self.name, self.count)
