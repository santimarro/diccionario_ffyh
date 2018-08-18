# Generated by Django 2.1 on 2018-08-18 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Example',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('example_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Meaning',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meaning_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.AddField(
            model_name='meaning',
            name='word',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search.Word'),
        ),
        migrations.AddField(
            model_name='example',
            name='word',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search.Word'),
        ),
    ]