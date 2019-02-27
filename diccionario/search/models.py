from django.db import models

# Create your models here.

class Example(models.Model):
    example_text = models.CharField(max_length=200)

    def __str__(self):
        return self.example_text


class Origin(models.Model):
    origin_text = models.CharField(max_length=30)

    def __str__(self):
        return self.origin_text

class Word(models.Model):
    '''
    A word has a text and it can have multiple meanings and examples.
    Later it may be implemented a related words section.
    '''
    word_text = models.CharField(max_length=30)
    # word_meaning = models.ForeignKey(Meaning, on_delete=models.CASCADE, default=None)
    word_examples = models.ForeignKey(Example, on_delete=models.CASCADE, default=None)
    word_origin = models.ForeignKey(Origin, on_delete=models.CASCADE, default=None)
    pub_date = models.DateTimeField('date published')
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.word_text


class Meaning(models.Model):
    meaning_text = models.CharField(max_length=200)
    word = models.ForeignKey(Word, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.meaning_text