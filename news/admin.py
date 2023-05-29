from django.contrib import admin
from .models import News, Author, Category


def nullnews(self, *args, **options):
    answer = input(f'Вы правда хотите удалить все статьи в категории {options["category"]}? yes/no :')

    if answer != 'yes':
        self.stdout.write(self.style.ERROR('Отменено'))
        return
    try:
        category = Category.objects.get(name=options['category'])
        News.objects.filter(category=category).delete()
        self.stdout.write(self.style.SUCCESS(
            f'Succesfully deleted all news from category {Category.name}'))  # в случае неправильного подтверждения говорим, что в доступе отказано
    except News.DoesNotExist:
        self.stdout.write(self.style.ERROR(f'Could not find category{Category.name}'))

# создаём новый класс для представления товаров в админке
class NewsAdmin(admin.ModelAdmin):
    # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с товарами
    #list_display = [field.name for field in News._meta.get_fields()] # генерируем список имён всех полей для более красивого отображения
    #list_display = ('name', 'category', 'published_date', 'author', 'rating')  # оставляем поля
    list_filter = ('name', 'category', 'published_date', 'author', 'rating')  # добавляем примитивные фильтры в нашу админку
    search_fields = ('name', 'category__name', 'published_date', 'author__name')  # тут всё очень похоже на фильтры из запросов в базу
    actions = [nullnews]  # добавляем действия в список

admin.site.register(Author)
admin.site.register(News, NewsAdmin)
admin.site.register(Category)

