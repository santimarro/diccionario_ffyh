from django.contrib import admin
from .models import Word, Meaning, Example, Origin

# Register your models here.

admin.site.register(Word)
admin.site.register(Meaning)
admin.site.register(Example)
admin.site.register(Origin)