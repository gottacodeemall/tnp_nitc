# Generated by Django 2.1 on 2019-04-23 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruiters', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chartdata',
            name='data',
            field=models.TextField(help_text='Enter the data seperated by commas without spaces after and before comma Eg. [110,111,230]'),
        ),
        migrations.AlterField(
            model_name='chartdata',
            name='labels',
            field=models.TextField(help_text="Enter the labels seperated by commas without spaces after and before comma Eg. [2010,2011,2012] or ['cse','ece','eee'] "),
        ),
    ]