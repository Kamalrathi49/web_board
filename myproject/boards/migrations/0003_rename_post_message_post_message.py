# Generated by Django 3.2.5 on 2021-07-20 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0002_topic_topic_message'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='message',
            new_name='message',
        ),
    ]