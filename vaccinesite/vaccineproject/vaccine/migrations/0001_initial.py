# Generated by Django 3.2.10 on 2021-12-10 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('gender', models.TextField()),
                ('age', models.IntegerField()),
                ('date_of_birth', models.DateField()),
                ('mobile_no', models.IntegerField(max_length=10, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'person',
                'ordering': ('name',),
            },
        ),
    ]