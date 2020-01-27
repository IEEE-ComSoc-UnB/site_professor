# Generated by Django 3.0.2 on 2020-01-24 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_perfilgeral_formularios'),
    ]

    operations = [
        migrations.CreateModel(
            name='Arvore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=120, null=True, verbose_name='Nome do Formulário')),
            ],
        ),
        migrations.CreateModel(
            name='Escolha',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=120, null=True, verbose_name='Nome da Escolha')),
            ],
        ),
        migrations.RemoveField(
            model_name='resposta',
            name='form_key',
        ),
        migrations.RemoveField(
            model_name='resposta',
            name='resp',
        ),
        migrations.RemoveField(
            model_name='resposta',
            name='resp_key',
        ),
        migrations.AddField(
            model_name='resposta',
            name='alternativa',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='blog.Alternativa'),
        ),
        migrations.AddField(
            model_name='resposta',
            name='formulario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='blog.Formulario'),
        ),
        migrations.AddField(
            model_name='resposta',
            name='pergunta',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='blog.Pergunta'),
        ),
        migrations.AddField(
            model_name='resposta',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='blog.Usuario'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='alternativas',
            field=models.ManyToManyField(blank=True, to='blog.Alternativa'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True, verbose_name='Email'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='form_atual',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='form_atual', to='blog.Formulario'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='formularios',
            field=models.ManyToManyField(blank=True, to='blog.Formulario'),
        ),
        migrations.AlterField(
            model_name='resposta',
            name='pub_data',
            field=models.DateField(blank=True, null=True, verbose_name='Data da resposta'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='curso',
            field=models.CharField(max_length=120, null=True, verbose_name='Curso'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='escolaridade',
            field=models.CharField(choices=[('FI', 'Ensino Fundamental Incompleto'), ('FC', 'Ensino Fundamental Completo'), ('MI', 'Ensino Medio Incompleto'), ('MC', 'Ensino Medio Completo'), ('SI', 'Ensino Superior Incompleto'), ('SC', 'Ensino Superior Completo')], max_length=3, null=True, verbose_name='Escolaridade'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='genero',
            field=models.CharField(choices=[('Masc', 'Masculino'), ('Femin', 'Feminino'), ('Outro', 'Outro')], max_length=15, null=True, verbose_name='Gênero'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='idade',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nacionalidade',
            field=models.CharField(max_length=120, null=True, verbose_name='Nacionalidade'),
        ),
        migrations.CreateModel(
            name='Tela',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=120, null=True, verbose_name='Nome da Tela')),
                ('arvore', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Arvore')),
            ],
        ),
        migrations.CreateModel(
            name='Raiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tela', models.OneToOneField(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='blog.Tela')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=120, null=True, verbose_name='Texto da Question')),
                ('tela', models.ManyToManyField(through='blog.Escolha', to='blog.Tela')),
                ('tela_pai', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='tela_pai', to='blog.Tela')),
            ],
        ),
        migrations.AddField(
            model_name='escolha',
            name='question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Question'),
        ),
        migrations.AddField(
            model_name='escolha',
            name='tela',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Tela'),
        ),
    ]
