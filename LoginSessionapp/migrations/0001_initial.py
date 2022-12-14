# Generated by Django 4.1.3 on 2022-11-15 07:41

import LoginSessionapp.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100, null=True)),
                ('full_name', models.CharField(max_length=50, null=True)),
                ('gender', models.CharField(choices=[('---', '---'), ('Male', 'Male'), ('Female', 'Female')], default='---', max_length=40)),
                ('age', models.IntegerField(validators=[LoginSessionapp.validators.age_validation])),
            ],
        ),
    ]
