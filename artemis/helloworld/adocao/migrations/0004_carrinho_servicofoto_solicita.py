# Generated by Django 5.0.3 on 2024-07-28 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adocao', '0003_authgroup_authgrouppermissions_authpermission_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrinho',
            fields=[
                ('carid', models.AutoField(primary_key=True, serialize=False)),
                ('carquant', models.IntegerField()),
                ('carpreco', models.FloatField()),
            ],
            options={
                'db_table': 'carrinho',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ServicoFoto',
            fields=[
                ('serftid', models.AutoField(primary_key=True, serialize=False)),
                ('serftvalor', models.ImageField(upload_to='venda\\images\\servico')),
            ],
            options={
                'db_table': 'servico_foto',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Solicita',
            fields=[
                ('solid', models.AutoField(primary_key=True, serialize=False)),
                ('soldthr', models.DateTimeField()),
                ('solpetid', models.IntegerField()),
            ],
            options={
                'db_table': 'solicita',
                'managed': False,
            },
        ),
    ]