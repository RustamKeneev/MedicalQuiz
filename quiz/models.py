from django.db import models

class Quiz(models.Model):
    """Название опросника"""
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Названия опросника"
        verbose_name_plural = "Название опросников"


class Category(models.Model):
    """Категории"""
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='categories')
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Option(models.Model):
    """Субкатегории или Параметры"""
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='options')
    name = models.CharField(max_length=256)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Субкатегория"
        verbose_name_plural = "Субкатегории"


class OptionList(models.Model):
    options = models.ManyToManyField(Option,related_name="answers",blank=True)
    options_post_answers = models.TextField(null=True)

    def __str__(self):
        return self.options_post_answers

    class Meta:
        verbose_name = "Детальный ответ"
        verbose_name_plural = "Детальные ответы"


