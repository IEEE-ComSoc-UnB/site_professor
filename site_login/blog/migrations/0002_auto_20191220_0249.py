# Generated by Django 2.2.6 on 2019-12-20 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='perfil_especifico',
            field=models.CharField(default=0, editable=False, max_length=120),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='escolaridade',
            field=models.CharField(choices=[('FI', 'Ensino Fundamental Incompleto'), ('FC', 'Ensino Fundamental Completo'), ('MI', 'Ensino Medio Incompleto'), ('MC', 'Ensino Medio Completo'), ('SUP', 'Ensino Superior Completo')], max_length=3, verbose_name='Escolaridade'),
        ),
    ]