# Generated by Django 4.0.3 on 2022-04-08 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0018_alter_account_downloads_alter_account_uploads'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upload',
            name='account',
        ),
        migrations.AddField(
            model_name='account',
            name='upload',
            field=models.ManyToManyField(null=True, to='website.upload'),
        ),
        migrations.AlterField(
            model_name='upload',
            name='category',
            field=models.CharField(choices=[('Portrait', 'Portrait'), ('Landscape', 'Landscape'), ('Sports', 'Sports'), ('Fashion', 'Fashion'), ('Technology', 'Technology'), ('Science', 'Science')], max_length=200, null=True),
        ),
    ]
