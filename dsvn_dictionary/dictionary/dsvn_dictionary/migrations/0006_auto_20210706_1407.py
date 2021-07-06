# Generated by Django 3.2.4 on 2021-07-06 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dsvn_dictionary', '0005_vi_dictionary_katakana_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vi_dictionary',
            name='description',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='vi_dictionary',
            name='hiragana_text',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='vi_dictionary',
            name='kanji_text',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='vi_dictionary',
            name='katakana_text',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]
