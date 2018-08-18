from django.db import models

# Create your models here.

class Word(models.Model):
    '''
    A word has a text and it can have multiple meanings and examples.
    Later it may be implemented a related words section.
    '''
    word_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.word_text


class Meaning(models.Model):
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    meaning_text = models.CharField(max_length=200)

    def __str__(self):
        return self.meaning_text


class Example(models.Model):
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    example_text = models.CharField(max_length=200)

    def __str__(self):
        return self.example_text
