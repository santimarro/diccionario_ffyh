from django.contrib import admin
from .models import Word, Meaning, Example, Origin

# Register your models here.

class WordInline(admin.TabularInline):
	model = Meaning

class WordAdmin(admin.ModelAdmin):
	inlines = [WordInline]

admin.site.register(Word, WordAdmin)
admin.site.register(Meaning)
admin.site.register(Example)
admin.site.register(Origin)
