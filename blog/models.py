from django.db import models


class Blog(models.Model):
    title = models.CharField(
        verbose_name="Название блога",
        max_length=255,
    )
    description = models.TextField(
        max_length=2000,
        verbose_name="Описание нашего блога",
    )
    image = models.ImageField(
        upload_to="blogs/",
        verbose_name="Фото блога",
    )
    
    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
