from django.db import models
from django.utils import timezone


class Player(models.Model):
    player_id = models.CharField(max_length=100)


class Level(models.Model):
    title = models.CharField(max_length=100)
    order = models.IntegerField(default=0)


class Prize(models.Model):
    title = models.CharField()


class PlayerLevel(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    completed = models.DateField()
    is_completed = models.BooleanField(default=False)
    score = models.PositiveIntegerField(default=0)

    def add_prize(self):
        """
        Метод для присвоения приза игроку,
        в случае успешного прохождения уровня
        """
        if self.is_completed:
            level_prize = LevelPrize.object.filter(level=self.level)
            level_prize.received = timezone.now()
            level_prize.save()


class LevelPrize(models.Model):
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    prize = models.ForeignKey(Prize, on_delete=models.CASCADE)
    received = models.DateField()
