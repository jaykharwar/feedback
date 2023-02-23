# Generated by Django 4.1.7 on 2023-02-23 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('woke', '0010_delete_db'),
    ]

    operations = [
        migrations.CreateModel(
            name='db',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Description', models.CharField(max_length=200)),
                ('Location', models.CharField(max_length=200)),
                ('Image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]