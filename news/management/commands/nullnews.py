from django.core.management.base import BaseCommand, CommandError
from news.models import Category, News


class Command(BaseCommand):
    help = 'Удаление новостей из категории'

    def add_arguments(self, parser):
        parser.add_argument('category', type=str)

    def handle(self, *args, **options):
        answer = input(f'Вы правда хотите удалить все статьи в категории {options["category"]}? yes/no :')

        if answer != 'yes':
            self.stdout.write(self.style.ERROR('Отменено'))
            return
        try:
            category = Category.objects.get(name=options['category'])
            News.objects.filter(category=category).delete()
            self.stdout.write(self.style.SUCCESS(f'Succesfully deleted all news from category {Category.name}')) # в случае неправильного подтверждения говорим, что в доступе отказано
        except News.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Could not find category{Category.name}'))