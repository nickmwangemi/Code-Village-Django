# Generated by Django 3.0.4 on 2020-03-25 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('code', models.CharField(max_length=200)),
                ('shortName', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'tbl_Currency',
            },
        ),
    ]
