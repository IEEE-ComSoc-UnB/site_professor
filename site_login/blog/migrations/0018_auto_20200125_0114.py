# Generated by Django 3.0.2 on 2020-01-25 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20200125_0044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='arvores',
            field=models.ManyToManyField(blank=True, to='blog.Arvore'),
        ),
    ]