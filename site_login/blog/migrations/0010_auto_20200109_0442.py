# Generated by Django 2.2.6 on 2020-01-09 04:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_usuario_perfil_especifico'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='perfil_especifico',
            field=models.ForeignKey(max_length=120, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='blog.PerfilGeral'),
        ),
    ]
