from rest_framework import serializers

from adocao.models import *
from django.db.models import Avg

class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = (
            'produto_proid',
            'servico_serid',
            'avadescricao',
            'avavalor',
            'pessoa_pesid',
            'avacod',
        )
    
    def validate(self, data):
        produto_proid = data.get('produto_proid')
        servico_serid = data.get('servico_serid')

        if produto_proid is None and servico_serid is None:
            raise serializers.ValidationError(
                "Pelo menos um dos campos produto ou serviço deve ser fornecido."
            )
        return data
    
    def validate_avavalor(self, value):
        if value in range(1, 6):
            return value
        else:
            raise serializers.ValidationError('A nota da avaliação precisa ser entre 1 e 5')


class CarrinhoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrinho
        fields = (
            'carid',
            'carpro',
            'carpes',
            'carser',
            'carquant',
            'carpreco',
        )

class FormapagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formapagamento
        fields = (
            'fpgid',
            'fpgdescricao',
        )


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            # 'logemail': {'write_only': True},
            'logsenha': {'write_only': True}
        }
        model = Login
        fields = (
            'logemail',
            'logsenha',
            'petshop_ptsid',
            'pessoa_pesid',
            'ong_ongid', 
        )


class NotafiscalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notafiscal
        fields = (
            'petshop_ptsid',
            'venda_venid',
            'ntfcod',
        )


class OngSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            # 'ongemail': {'write_only': True},
        }
        model = Ong
        fields = (
            'ongid',
            'ongnome',
            'ongcidade',
            'ongbairro',
            'ongrua',
            'ongnum',
            'ongtelefone',
            'ongemail',
            'ongestado',
        )


class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        # extra_kwargs = {
        #     'pesemail': {'write_only': True}
        # }
        model = Pessoa
        fields = (
            'pesid',
            'pescpf',
            'pesdtnascto',
            'pessexo',
            'pescidade',
            'pesbairro',
            'pesrua',
            'pesemail',
            'pesnumero',
            'pestelefone',
            'pesnome',
            'pesestado',
        )


class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = (
            'petid',
            'petnome',
            'petsexo',
            'petcastrado',
            'petdtnascto',
            'petpeso',
            'pessoa_pesid',
            'pet_porte_ptpid',
            'pet_raca_ptrid',
            'pet_tipo_pttid',
        )


class PetAdocaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetAdocao
        fields = (
            'ong_ongid',
            'pet_petid',
            'adoid',
        )


class PetFotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetFoto
        fields = (
            'pftid',
            'pftfoto',
            'pet_petid',
        )


class PetPorteSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetPorte
        fields = (
            'ptpid',
            'ptpnome',
            'ptpdescricao',
        )


class PetRacaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetRaca
        fields = (
            'ptrid',
            'ptrnome',
            'pet_tipo_pttid',
        )


class PetTipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetTipo
        fields = (
            'pttid',
            'pttnome',
        )


class PetshopSerializer(serializers.ModelSerializer):
    class Meta:
        # extra_kwargs = {
        #     'ptsemail': {'write_only': True}
        # }
        model = Petshop
        fields = (
            'ptsid',
            'ptsnome',
            'ptscnpj',
            'ptscidade',
            'ptsbairro',
            'ptsrua',
            'ptsnumero',
            'ptstelefone',
            'ptsemail',
            'ptsestado',
        )


class ProdutoSerializer(serializers.ModelSerializer):
    # 1 Nested Relationship - Menos performático, traz o conteúdo
    #avaliacoes = AvaliacaoSerializer(many=True, read_only=True)

    # 2 HyperLinked Related Field - Mais performático e gera link, recomendado
    #avaliacoes = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='avaliacao-detail')

    # 3 Primary Key Related Field
    avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)


    media_avaliacoes = serializers.SerializerMethodField()

    class Meta:
        model = Produto
        fields = (
            'proid', 
            'pronome', 
            'propreco', 
            'prosaldo', 
            'propetshop_ptsid', 
            'prodtvalidade',
            'avaliacoes', 
            'media_avaliacoes',
        )
    
    def get_media_avaliacoes(self, obj):
        media = obj.avaliacoes.aggregate(Avg('avavalor')).get('avavalor__avg')
        if media is None:
            return 0
        else:
            #return media
            return round(media*2)/2


class ProdutoFotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProdutoFoto
        fields = (
            'prfid',
            'prffoto',
            'produto_proid',
        )


class ServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servico
        fields = (
            'serid',
            'servalor',
            'petshop_ptsid',
            'tiposervico_tpsid',
            'serdescricao',
        )


class ServicoFotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicoFoto
        fields = (
            'serftid',
            'serftvalor',
            'servico_serid',
        )


class SolicitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicita
        fields = (
            'pessoa_pesid',
            'servico_serid',
            'solid',
            'soldthr',
            'solpetid',
        )


class TiposervicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tiposervico
        fields = (
            'tpsid',
            'tpsnome',
            'tpsdescricao',
        )


class VendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venda
        fields = (
            'venid',
            'venser',
            'venpro',
            'venformapagamento_fpgid',
            'venpessoa_pesid',
            'venvalor',
        )


    
    
    
