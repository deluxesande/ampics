# Generated by Django 4.0.3 on 2022-03-30 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_alter_upload_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]