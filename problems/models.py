from django.db.models import Model, CharField, SlugField, TextField, ImageField, ForeignKey, PROTECT

# Create your models here.
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


    name = CharField(max_length=120, verbose_name="Названии проблемы")
    description = TextField(max_length=255, blank=True, null=True,  verbose_name="Описание проблемы")
    address = CharField(max_length=150, verbose_name="Адресс проблемы")

    image = ImageField(upload_to="problems_images", verbose_name="Изображение проблемы")
    image_resolved = ImageField(
        upload_to="problems_images_resolved",
        default=None, 
        blank=True, 
        null=True, 
        verbose_name="Изображение решенной проблемы"
    )
    slug = SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name="URL")

    category = ForeignKey(to=Categories, on_delete=PROTECT)
    status = CharField(max_length=20, choices=STATUS_CHOICES, default='New', verbose_name="Статус")


    class Meta :
        db_table = "problem"
        verbose_name = "Проблему"
        verbose_name_plural = "Проблемы"

    def __str__(self):
        return f"{self.name} | {self.status} | {self.category}"