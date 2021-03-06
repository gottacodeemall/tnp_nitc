# Generated by Django 2.1.2 on 2019-01-01 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(upload_to='static/files/students/')),
                ('file_name', models.CharField(help_text='Name', max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='StudentInstruction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name to be displayed on Django admin. Do not create multiple instances.', max_length=255, unique=True)),
                ('instruction_html', models.TextField(help_text='Enter the html content of the student instructions.')),
            ],
        ),
    ]
