# Generated by Django 3.2.5 on 2021-07-20 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0004_rename_topic_message_topic_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_topic', to='boards.topic'),
        ),
    ]
