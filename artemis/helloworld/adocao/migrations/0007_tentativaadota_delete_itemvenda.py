# Generated by Django 5.0.3 on 2024-08-09 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adocao', '0006_categoriaproduto'),
    ]

    operations = [
        migrations.CreateModel(
            name='TentativaAdota',
            fields=[
                ('ttaid', models.AutoField(primary_key=True, serialize=False)),
                ('ttastatus', models.CharField(max_length=11)),
            ],
            options={
                'db_table': 'tentativa_adota',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Itemvenda',
        ),
    ]
