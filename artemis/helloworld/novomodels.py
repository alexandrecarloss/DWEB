# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    created = models.DateTimeField()
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'authtoken_token'


class Avaliacao(models.Model):
    produto_proid = models.ForeignKey('Produto', models.DO_NOTHING, db_column='produto_proid', blank=True, null=True)
    servico_serid = models.ForeignKey('Servico', models.DO_NOTHING, db_column='servico_serid', blank=True, null=True)
    avadescricao = models.CharField(max_length=100, blank=True, null=True)
    avavalor = models.IntegerField()
    pessoa_pesid = models.ForeignKey('Pessoa', models.DO_NOTHING, db_column='pessoa_pesid')
    avacod = models.AutoField(primary_key=True)
    avadthora = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'avaliacao'


class Carrinho(models.Model):
    carid = models.AutoField(primary_key=True)
    carpro = models.ForeignKey('Produto', models.DO_NOTHING, db_column='carpro', blank=True, null=True)
    carpes = models.ForeignKey('Pessoa', models.DO_NOTHING, db_column='carpes')
    carser = models.ForeignKey('Servico', models.DO_NOTHING, db_column='carser', blank=True, null=True)
    carquant = models.IntegerField()
    carpreco = models.FloatField()

    class Meta:
        managed = False
        db_table = 'carrinho'


class CategoriaProduto(models.Model):
    ctpid = models.AutoField(primary_key=True)
    ctpnome = models.CharField(max_length=60)
    ctpdescricao = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'categoria_produto'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Formapagamento(models.Model):
    fpgid = models.AutoField(primary_key=True)
    fpgdescricao = models.CharField(max_length=65, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'formapagamento'


class Login(models.Model):
    logemail = models.CharField(primary_key=True, max_length=70)
    logsenha = models.CharField(max_length=45, blank=True, null=True)
    petshop_ptsid = models.ForeignKey('Petshop', models.DO_NOTHING, db_column='petshop_ptsid', blank=True, null=True)
    pessoa_pesid = models.ForeignKey('Pessoa', models.DO_NOTHING, db_column='pessoa_pesid', blank=True, null=True)
    ong_ongid = models.ForeignKey('Ong', models.DO_NOTHING, db_column='ong_ongid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'login'


class Notafiscal(models.Model):
    petshop_ptsid = models.ForeignKey('Petshop', models.DO_NOTHING, db_column='petshop_ptsid')
    venda_venid = models.ForeignKey('Venda', models.DO_NOTHING, db_column='venda_venid')
    ntfcod = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'notafiscal'


class Ong(models.Model):
    ongid = models.AutoField(primary_key=True)
    ongnome = models.CharField(max_length=65)
    ongcidade = models.CharField(max_length=70, blank=True, null=True)
    ongbairro = models.CharField(max_length=70)
    ongrua = models.CharField(max_length=70)
    ongnum = models.SmallIntegerField()
    ongtelefone = models.CharField(max_length=15, blank=True, null=True)
    ongemail = models.CharField(max_length=70, blank=True, null=True)
    ongestado = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'ong'


class Pessoa(models.Model):
    pesid = models.AutoField(primary_key=True)
    pescpf = models.CharField(unique=True, max_length=11)
    pesdtnascto = models.DateField()
    pessexo = models.CharField(max_length=1)
    pescidade = models.CharField(max_length=65)
    pesbairro = models.CharField(max_length=65)
    pesrua = models.CharField(max_length=65)
    pesemail = models.CharField(max_length=70)
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
    ong_ongid = models.ForeignKey(Ong, models.DO_NOTHING, db_column='ong_ongid')
    pet_petid = models.ForeignKey(Pet, models.DO_NOTHING, db_column='pet_petid')
    adoid = models.AutoField(primary_key=True)

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
    ptsemail = models.CharField(max_length=70, blank=True, null=True)
    ptsestado = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'petshop'


class Produto(models.Model):
    proid = models.AutoField(primary_key=True)
    pronome = models.CharField(max_length=65)
    propreco = models.FloatField()
    prosaldo = models.IntegerField(blank=True, null=True)
    propetshop_ptsid = models.ForeignKey(Petshop, models.DO_NOTHING, db_column='propetshop_ptsid')
    categoria_produto_ctpid = models.ForeignKey(CategoriaProduto, models.DO_NOTHING, db_column='categoria_produto_ctpid')

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
    petshop_ptsid = models.ForeignKey(Petshop, models.DO_NOTHING, db_column='petshop_ptsid')
    tiposervico_tpsid = models.ForeignKey('Tiposervico', models.DO_NOTHING, db_column='tiposervico_tpsid')
    serdescricao = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'servico'


class ServicoFoto(models.Model):
    serftid = models.AutoField(primary_key=True)
    serftvalor = models.CharField(max_length=100)
    servico_serid = models.ForeignKey(Servico, models.DO_NOTHING, db_column='servico_serid')

    class Meta:
        managed = False
        db_table = 'servico_foto'


class Solicita(models.Model):
    pessoa_pesid = models.ForeignKey(Pessoa, models.DO_NOTHING, db_column='pessoa_pesid')
    servico_serid = models.ForeignKey(Servico, models.DO_NOTHING, db_column='servico_serid')
    solid = models.AutoField(primary_key=True)
    soldthr = models.DateTimeField()
    solpetid = models.IntegerField()
    solstatus = models.CharField(max_length=9)

    class Meta:
        managed = False
        db_table = 'solicita'


class TentativaAdota(models.Model):
    ttaid = models.AutoField(primary_key=True)
    ttapes = models.ForeignKey(Pessoa, models.DO_NOTHING, db_column='ttapes')
    tta_petadocao = models.ForeignKey(PetAdocao, models.DO_NOTHING, db_column='tta_petadocao')
    ttastatus = models.CharField(max_length=11)

    class Meta:
        managed = False
        db_table = 'tentativa_adota'


class Tiposervico(models.Model):
    tpsid = models.AutoField(primary_key=True)
    tpsnome = models.CharField(max_length=70)
    tpsdescricao = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'tiposervico'


class Venda(models.Model):
    venid = models.IntegerField(primary_key=True)
    venser = models.IntegerField(blank=True, null=True)
    venpro = models.IntegerField(blank=True, null=True)
    venformapagamento_fpgid = models.ForeignKey(Formapagamento, models.DO_NOTHING, db_column='venformapagamento_fpgid')
    venpessoa_pesid = models.ForeignKey(Pessoa, models.DO_NOTHING, db_column='venpessoa_pesid')
    venvalor = models.FloatField()
    vendthora = models.DateTimeField(blank=True, null=True)
    venqtd = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'venda'
