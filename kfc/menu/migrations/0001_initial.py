# Generated by Django 4.2.7 on 2024-02-14 03:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='userdetails',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key='True', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('phoneno', models.IntegerField()),
                ('emailid', models.CharField(max_length=20)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='DefaultGender', max_length=10)),
            ],
        ),
    ]
