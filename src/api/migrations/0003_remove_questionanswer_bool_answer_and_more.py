# Generated by Django 5.0.4 on 2024-04-13 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_question_options_question_position'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questionanswer',
            name='bool_answer',
        ),
        migrations.RemoveField(
            model_name='questionanswer',
            name='text_answer',
        ),
        migrations.AddField(
            model_name='questionanswer',
            name='answer',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
