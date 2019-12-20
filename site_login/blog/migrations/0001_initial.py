# Generated by Django 2.2.6 on 2019-12-20 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=120, verbose_name='Nome do Usuário')),
                ('idade', models.IntegerField()),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('genero', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro')], max_length=2, verbose_name='Gênero')),
                ('escolaridade', models.CharField(choices=[('FI', 'Ensino Fundamental Incompleto'), ('FC', 'Ensino Fundamental Completo'), ('MI', 'Ensino Medio Incompleto'), ('MC', 'Ensino Medio Completo'), ('SUP', 'Ensino Superior Completo')], max_length=2, verbose_name='Escolaridade')),
                ('curso', models.CharField(max_length=120, verbose_name='Curso')),
                ('nacionalidade', models.CharField(max_length=120, verbose_name='Nacionalidade')),
            ],
        ),
        migrations.CreateModel(
            name='PerfilGeral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=120, verbose_name='Nome do Perfil')),
                ('numero_de_usuarios', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
