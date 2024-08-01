from django.db import models

from config import settings

NULLABLE = {"null": True, "blank": True}


class Car(models.Model):
    title = models.CharField(max_length=50, verbose_name='название')
    description = models.TextField(verbose_name="описание")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'автомобиль'
        verbose_name_plural = 'автомобили'


class Moto(models.Model):
    title = models.CharField(max_length=50, verbose_name='название')
    description = models.TextField(verbose_name="описание")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'мотоцикл'
        verbose_name_plural = 'мотоциклы'


class Milage(models.Model):
    car = models.ForeignKey(Car, verbose_name="автомобиль", on_delete=models.CASCADE, **NULLABLE, related_name='milage')
    moto = models.ForeignKey(Moto, verbose_name="Мотоцикл", on_delete=models.CASCADE, **NULLABLE, related_name='milage')

    milage = models.PositiveIntegerField(verbose_name="пробег")
    year = models.PositiveSmallIntegerField(verbose_name="год регистрации")

    def __str__(self):
        return f'{self.moto if self.moto else self.car} - {self.year} - {self.milage}'

    class Meta:
        verbose_name = 'пробег'
        verbose_name_plural = 'пробеги'
        ordering = ('-year',)
