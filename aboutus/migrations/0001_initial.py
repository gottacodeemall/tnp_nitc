# Generated by Django 2.1.2 on 2019-01-01 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the ABOUTUS ON Djanoo-admin. Do not create multiple instances.', max_length=255, unique=True)),
                ('aboutus', models.TextField(help_text='HTML of About Us')),
                ('vision', models.TextField(help_text='HTML of Vision')),
                ('mission', models.TextField(help_text='HTML of Mission')),
            ],
        ),
        migrations.CreateModel(
            name='Academic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.CharField(help_text='Name of the Branch. Eg. Computer Science and Engineering', max_length=255)),
                ('subjects', models.TextField(help_text='HTML list of core and important subjects')),
                ('url', models.URLField()),
                ('stream', models.CharField(choices=[('B.Tech', 'B.Tech'), ('M.Tech', 'M.Tech'), ('MCA', 'MCA')], max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the achievement. To be displayed on Django admin.', max_length=255, unique=True)),
                ('pic', models.ImageField(default='static/img/slider_3.jpg', upload_to='static/img/achievements/')),
                ('alt_text', models.CharField(help_text='If image does not load, this will be displayed.', max_length=255)),
                ('title', models.TextField(help_text='Title')),
                ('content', models.TextField(help_text='Insert content.')),
                ('date', models.DateField(help_text='Date of the event. Sorted based on this.')),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the achievement. To be displayed on Django admin.', max_length=255, unique=True)),
                ('pic', models.ImageField(default='static/img/slider_3.jpg', upload_to='static/img/gallery/')),
                ('alt_text', models.CharField(help_text='If image does not load, this will be displayed.', max_length=255)),
                ('info', models.TextField(help_text='Description text of the image.')),
                ('date', models.DateField(help_text='Date of the event. Sorted based on this.')),
            ],
        ),
    ]
