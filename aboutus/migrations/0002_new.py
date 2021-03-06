# Generated by Django 2.1 on 2019-04-23 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutus', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the achievement. To be displayed on Django admin.', max_length=255, unique=True)),
                ('short_desc', models.CharField(help_text='Short description about the news.', max_length=255)),
                ('pic', models.ImageField(default='static/img/slider_3.jpg', upload_to='static/img/news/')),
                ('alt_text', models.CharField(help_text='If image does not load, this will be displayed.', max_length=255)),
                ('title', models.TextField(help_text='Title')),
                ('content', models.TextField(help_text='Insert content.')),
                ('date', models.DateField(help_text='Date of the event. Sorted based on this.')),
            ],
        ),
    ]
