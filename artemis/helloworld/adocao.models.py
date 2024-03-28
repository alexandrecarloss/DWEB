# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Formapagamento(models.Model):
    fpgid = models.AutoField(primary_key=True)
    fpgdescricao = models.CharField(max_length=65, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'formapagamento'


class Itemvenda(models.Model):
    produto_proid = models.OneToOneField('Produto', models.DO_NOTHING, db_column='produto_proid', primary_key=True)  # The composite primary key (produto_proid, venda_venid) found, that is not supported. The first column is selected.
    venda_venid = models.ForeignKey('Venda', models.DO_NOTHING, db_column='venda_venid')
    itvqtde = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'itemvenda'
        unique_together = (('produto_proid', 'venda_venid'),)


class Ong(models.Model):
    ongid = models.AutoField(primary_key=True)
    ongnome = models.CharField(max_length=65)
    ongcidade = models.CharField(max_length=70, blank=True, null=True)
    ongbairro = models.CharField(max_length=70)
    ongrua = models.CharField(max_length=70)
    ongnum = models.SmallIntegerField()
    ongtelefone = models.CharField(max_length=15, blank=True, null=True)
    ongemail = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ong'


class Pessoa(models.Model):
    pesid = models.AutoField(primary_key=True)
    pescpf = models.CharField(max_length=11)
    pesdtnascto = models.DateField()
    pessexo = models.CharField(max_length=1)
    pescidade = models.CharField(max_length=65)
    pesbairro = models.CharField(max_length=65)
    pesrua = models.CharField(max_length=65)
    pesemail = models.CharField(max_length=65)
    pesnumero = models.SmallIntegerField()
    pestelefone = models.CharField(max_length=15)
    pesnome = models.CharField(max_length=100)
    pesestado = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'pessoa'


class Pet(models.Model):
    petid = models.AutoField(primary_key=True)
    petnome = models.CharField(max_length=65)
    petsexo = models.CharField(max_length=1)
    petcastrado = models.CharField(max_length=12)
    petdtnascto = models.DateField()
    petpeso = models.FloatField()
    pessoa_pesid = models.ForeignKey(Pessoa, models.DO_NOTHING, db_column='pessoa_pesid', blank=True, null=True)
    pet_porte_ptpid = models.ForeignKey('PetPorte', models.DO_NOTHING, db_column='pet_porte_ptpid')
    pet_raca_ptrid = models.ForeignKey('PetRaca', models.DO_NOTHING, db_column='pet_raca_ptrid')
    pet_tipo_pttid = models.ForeignKey('PetTipo', models.DO_NOTHING, db_column='pet_tipo_pttid')

    class Meta:
        managed = False
        db_table = 'pet'


class PetAdocao(models.Model):
    ong_ongid = models.ForeignKey(Ong, models.DO_NOTHING, db_column='ong_ongid', blank=True, null=True)
    pet_petid = models.OneToOneField(Pet, models.DO_NOTHING, db_column='pet_petid', primary_key=True)

    class Meta:
        managed = False
        db_table = 'pet_adocao'


class PetFoto(models.Model):
    pftid = models.AutoField(primary_key=True)
    pftfoto = models.CharField(max_length=100)
    pet_petid = models.ForeignKey(Pet, models.DO_NOTHING, db_column='pet_petid')

    class Meta:
        managed = False
        db_table = 'pet_foto'


class PetPorte(models.Model):
    ptpid = models.AutoField(primary_key=True)
    ptpnome = models.CharField(max_length=65)
    ptpdescricao = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'pet_porte'


class PetRaca(models.Model):
    ptrid = models.AutoField(primary_key=True)
    ptrnome = models.CharField(max_length=65, blank=True, null=True)
    pet_tipo_pttid = models.ForeignKey('PetTipo', models.DO_NOTHING, db_column='pet_tipo_pttid')

    class Meta:
        managed = False
        db_table = 'pet_raca'


class PetTipo(models.Model):
    pttid = models.AutoField(primary_key=True)
    pttnome = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'pet_tipo'


class Petshop(models.Model):
    ptsid = models.AutoField(primary_key=True)
    ptsnome = models.CharField(max_length=65, blank=True, null=True)
    ptscnpj = models.CharField(max_length=20)
    ptscidade = models.CharField(max_length=65, blank=True, null=True)
    ptsbairro = models.CharField(max_length=65, blank=True, null=True)
    ptsrua = models.CharField(max_length=65, blank=True, null=True)
    ptsnumero = models.SmallIntegerField(blank=True, null=True)
    ptstelefone = models.CharField(max_length=15, blank=True, null=True)
    ptsemail = models.CharField(max_length=65, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'petshop'


class Produto(models.Model):
    proid = models.AutoField(primary_key=True)
    pronome = models.CharField(max_length=65)
    propreco = models.FloatField()
    prosaldo = models.IntegerField(blank=True, null=True)
    propetshop_ptsid = models.ForeignKey(Petshop, models.DO_NOTHING, db_column='propetshop_ptsid')
    prodtvalidade = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'produto'


class ProdutoFoto(models.Model):
    prfid = models.AutoField(primary_key=True)
    prffoto = models.CharField(max_length=100)
    produto_proid = models.ForeignKey(Produto, models.DO_NOTHING, db_column='produto_proid')

    class Meta:
        managed = False
        db_table = 'produto_foto'


class Servico(models.Model):
    serid = models.AutoField(primary_key=True)
    servalor = models.FloatField()
    tosdatahora = models.DateTimeField()
    pet_petid = models.ForeignKey(Pet, models.DO_NOTHING, db_column='pet_petid')
    pessoa_pesid = models.ForeignKey(Pessoa, models.DO_NOTHING, db_column='pessoa_pesid')
    petshop_ptsid = models.ForeignKey(Petshop, models.DO_NOTHING, db_column='petshop_ptsid')
    tiposervico_tpsid = models.ForeignKey('Tiposervico', models.DO_NOTHING, db_column='tiposervico_tpsid')

    class Meta:
        managed = False
        db_table = 'servico'


class Tiposervico(models.Model):
    tpsid = models.AutoField(primary_key=True)
    tpsnome = models.CharField(max_length=70)
    tpsdescricao = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'tiposervico'


class Venda(models.Model):
    venid = models.AutoField(primary_key=True)
    venformapagamento_fpgid = models.ForeignKey(Formapagamento, models.DO_NOTHING, db_column='venformapagamento_fpgid')
    venpessoa_pesid = models.ForeignKey(Pessoa, models.DO_NOTHING, db_column='venpessoa_pesid')
    venpetshop_ptsid = models.ForeignKey(Petshop, models.DO_NOTHING, db_column='venpetshop_ptsid')
    venvalor = models.FloatField()

    class Meta:
        managed = False
        db_table = 'venda'
