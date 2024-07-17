# Generated by Django 5.0.6 on 2024-07-17 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=20)),
                ('course_code', models.IntegerField()),
                ('teacher', models.CharField(max_length=30)),
                ('number_of_topics', models.IntegerField()),
                ('duration_of_course', models.DateField()),
                ('number_of_students', models.IntegerField()),
                ('description_of_course', models.TextField()),
                ('fees_required', models.IntegerField()),
            ],
        ),
    ]