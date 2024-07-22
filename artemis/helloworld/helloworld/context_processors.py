from adocao.models import *

def context_grupo_usuario(request):
    grupo_usuario = str(request.user.groups.first())
    if grupo_usuario == 'Ong':
        dado_usuario = Ong.objects.filter(ongemail = str(request.user.email)).first()
    elif grupo_usuario == 'Pessoa':
        dado_usuario = Pessoa.objects.filter(pesemail = str(request.user.email)).first()
    elif grupo_usuario == 'Pet shop':
        dado_usuario = Petshop.objects.filter(ptsemail = str(request.user.email)).first()
    else:
        dado_usuario = None
    
    return {'grupo_usuario': grupo_usuario, 'dado_usuario': dado_usuario}
