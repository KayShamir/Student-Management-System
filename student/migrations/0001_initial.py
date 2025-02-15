# Generated by Django 5.0.6 on 2024-05-27 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.IntegerField()),
                ('student_lastname', models.CharField(max_length=50)),
                ('student_firstname', models.CharField(max_length=50)),
                ('student_gender', models.CharField(max_length=10)),
                ('student_yearlevel', models.IntegerField()),
                ('student_course', models.CharField(max_length=255)),
                ('student_email', models.EmailField(max_length=254)),
                ('student_profile', models.ImageField(upload_to='')),
                ('student_units', models.IntegerField()),
                ('student_birthdate', models.DateField()),
            ],
        ),
    ]
