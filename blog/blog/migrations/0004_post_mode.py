# Generated by Django 3.1.5 on 2021-02-05 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='mode',
            field=models.CharField(choices=[('Public', 'Public'), ('Private', 'Private')], default='public', max_length=7),
        ),
    ]