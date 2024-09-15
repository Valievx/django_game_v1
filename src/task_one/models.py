from django.db import models


class Boost(models.Model):
    type = models.CharField(
        verbose_name="Тип буста",
        max_length=255,
        choices=[
            ("speed", "Скорость"),
            ("strength", "Сила"),
            ("time", "Время"),
            ("defense", "Защита"),
            ("health", "Здоровье"),
        ]
    )
    value = models.PositiveIntegerField(default=1)


class Player(models.Model):
    username = models.CharField(unique=True, max_length=100)
    first_login = models.DateTimeField(auto_now_add=True)

    def add_boost(self, boost, quantity=1):
        """
        Метод для начисления бустов игроку.
        """
        player_boost, created = PlayerBoost.objects.get_or_create(
            player=self,
            boost=boost
        )
        player_boost.quantity += quantity
        player_boost.save()


class PlayerBoost(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    boost = models.ForeignKey(Boost, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
