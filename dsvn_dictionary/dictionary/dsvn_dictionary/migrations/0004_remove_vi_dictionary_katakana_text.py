# Generated by Django 3.2.4 on 2021-07-06 07:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dsvn_dictionary', '0003_rename_ja_text_vi_dictionary_kanji_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vi_dictionary',
            name='katakana_text',
        ),
    ]
