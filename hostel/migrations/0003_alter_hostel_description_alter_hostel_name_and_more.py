# Generated by Django 4.0.2 on 2022-03-12 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0002_alter_hostel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostel',
            name='description',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='hostel',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='hostel',
            name='price',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='hostel',
            name='stock',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]