# Generated by Django 3.0.2 on 2020-05-05 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gun',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_gun', models.CharField(help_text='Enter field documentation', max_length=40)),
                ('grade', models.CharField(help_text='качество оружия common uncommon...', max_length=40)),
                ('quality', models.CharField(help_text='качество оружия с завода, после полевых....', max_length=40)),
                ('img_road_gun', models.CharField(help_text='Enter field documentation', max_length=100)),
                ('value', models.DecimalField(decimal_places=2, max_digits=6)),
                ('startrec', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(help_text='Enter field documentation', max_length=20)),
                ('Money', models.DecimalField(decimal_places=2, max_digits=6)),
                ('Admin', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-Name'],
            },
        ),
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Enter field documentation', max_length=40)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('img_road', models.CharField(help_text='Enter field documentation', max_length=100)),
                ('guns', models.ManyToManyField(to='case.Gun')),
            ],
        ),
    ]