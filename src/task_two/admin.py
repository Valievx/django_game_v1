from django.contrib import admin

from .models import (
    Player, Level, Prize,
    PlayerLevel, LevelPrize
)


class PlayerAdmin(admin.ModelAdmin):
    list_display = (
        'player_id',
    )


class LevelAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'order',
    )


class PrizeAdmin(admin.ModelAdmin):
    list_display = (
        'title',
    )


class PlayerLevelAdmin(admin.ModelAdmin):
    list_display = (
        'player',
        'level',
        'completed',
        'is_completed',
        'score',
    )


class LevelPrizeAdmin(admin.ModelAdmin):
    list_display = (
        'level',
        'prize',
        'received',
    )


admin.site.register(Player)
admin.site.register(Level)
admin.site.register(Prize)
admin.site.register(PlayerLevel)
admin.site.register(LevelPrize)
