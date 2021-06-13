from django.db import models


# Create your models here.


class Sections(models.Model):
    '''Раздел'''
    name = models.CharField('Категория', max_length=150)
    description = models.TextField('Описание')
    cover = models.ImageField('Обложка_Раздела', upload_to='section_cover/', blank=True, null=True)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'


class Books(models.Model):
    '''Книги'''
    title = models.CharField('Название', max_length=150)
    description = models.TextField('Описание')
    cover = models.ImageField('Обложка', upload_to='books_cover/')
    author = models.CharField('Автор', max_length=150)
    pages = models.PositiveSmallIntegerField('Страниц', default=0)
    year_of_release = models.PositiveSmallIntegerField('Дата выхода', default=2005)
    sections = models.ForeignKey(Sections, verbose_name='раздел', on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=160, unique=True)
    url_on_book = models.SlugField(max_length=160, unique=True)
    file_book = models.FileField('Книга book_pdf', upload_to='books_pdf/', default='books_pdf/1.pdf')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'


class RatingStar(models.Model):
    '''Звёзды рейтинга'''
    value = models.PositiveSmallIntegerField('Значение', default=0)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'Звёзда рейтинга'
        verbose_name_plural = 'Звёзды рейтинга'


class Rating(models.Model):
    '''Рейтинг'''
    ip = models.CharField('IP адрес', max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name='звезда')
    book = models.ForeignKey(Books, on_delete=models.CASCADE, verbose_name='книга')

    def __str__(self):
        return f'{self.star} - {self.book}'

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'
