# Generated by Django 4.0.3 on 2022-04-08 08:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0021_alter_upload_account'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upload',
            name='account',
        ),
        migrations.AddField(
            model_name='upload',
            name='account',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='website.account'),
        ),
    ]