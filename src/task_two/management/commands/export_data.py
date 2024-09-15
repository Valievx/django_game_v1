import csv

from django.core.management import BaseCommand
from django.http import StreamingHttpResponse
from django.utils.encoding import smart_str
from player.models import PlayerLevel, Level, LevelPrize


class Command(BaseCommand):
    def handle(self, *args, **options):
        # Определяем заголовки CSV
        def get_data():
            # Выборка данных для CSV
            query_set = PlayerLevel.objects.select_related('player', 'level').prefetch_related('level__levelprize_set')

            # Генерация строк CSV
            for player_level in query_set:
                player_id = player_level.player.player_id
                level_title = player_level.level.title
                is_completed = 'Yes' if player_level.is_completed else 'No'
                prize_title = ''

                if player_level.is_completed:
                    # Получение приза для уровня
                    try:
                        level_prize = LevelPrize.objects.get(level=player_level.level, player=player_level.player)
                        prize_title = level_prize.prize.title
                    except LevelPrize.DoesNotExist:
                        prize_title = 'No Prize'

                yield [player_id, level_title, is_completed, prize_title]

        response = StreamingHttpResponse(
            (smart_str(','.join(row)) + '\n' for row in get_data()),
            content_type="text/csv"
        )

        response['Content-Disposition'] = 'attachment; filename=player_levels.csv'
        return response
