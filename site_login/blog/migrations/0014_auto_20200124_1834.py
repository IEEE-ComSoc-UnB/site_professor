# Generated by Django 3.0.2 on 2020-01-24 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20200124_1829'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='tela',
        ),
        migrations.RemoveField(
            model_name='question',
            name='tela_pai',
        ),
        migrations.AddField(
            model_name='question',
            name='tela_filha',
            field=models.ManyToManyField(related_name='tela_filha', through='blog.Escolha', to='blog.Tela'),
        ),
        migrations.AddField(
            model_name='tela',
            name='question',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='blog.Question'),
        ),
    ]
