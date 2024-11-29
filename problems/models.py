from django.db.models import Model, CharField, SlugField, TextField, ImageField, ForeignKey, PROTECT, BinaryField
from django.conf import settings


class Categories(Model):
    name = CharField(max_length=120, unique=True, verbose_name="Название")
    slug = SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name="URL")

    class Meta:
        db_table = "category"
        verbose_name = "Категорию"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

class Problems(Model):
    STATUS_CHOICES = (
        ('New', 'Новая'),
        ('Rejected', 'Отклонена'),
        ('Success', 'Решена')
    )

    user = ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=PROTECT,
        related_name="problems",
        verbose_name="Пользователь"
    )
    name = CharField(max_length=120, verbose_name="Название проблемы")
    description = TextField(max_length=255, blank=True, null=True, verbose_name="Описание проблемы")
    address = CharField(max_length=150, verbose_name="Адрес проблемы")
    image = BinaryField(verbose_name="Изображение проблемы", blank=True, null=True)
    image_resolved = BinaryField(verbose_name="Изображение решенной проблемы", blank=True, null=True)
    category = ForeignKey(to="Categories", on_delete=PROTECT, verbose_name="Категория")
    status = CharField(max_length=20, choices=STATUS_CHOICES, default='New', verbose_name="Статус")
    slug = CharField(max_length=200, unique=True, blank=True, null=True, verbose_name="URL")

    class Meta:
        db_table = "problem"
        verbose_name = "Проблему"
        verbose_name_plural = "Проблемы"

    def __str__(self):
        return f"{self.name} | {self.status} | {self.category}"