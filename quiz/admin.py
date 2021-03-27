from django.contrib import admin
from .models import Quiz, Category, Option, OptionList

admin.site.register(Quiz)
admin.site.register(Category)
admin.site.register(Option)
admin.site.register(OptionList)
