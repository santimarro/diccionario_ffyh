from django.db import models

# Create your models here.


class Meaning(models.Model):
    meaning_text = models.CharField(max_length=200)

    def __str__(self):
        return self.meaning_text


class Example(models.Model):
    example_text = models.CharField(max_length=200)

    def __str__(self):
        return self.example_text


class Word(models.Model):
    '''
    A word has a text and it can have multiple meanings and examples.
    Later it may be implemented a related words section.
    '''
    word_text = models.CharField(max_length=200)
    word_meaning = models.ManyToManyField(Meaning)
    word_examples = models.ManyToManyField(Example)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.word_text



