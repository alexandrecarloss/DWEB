def context_grupo_usuario(request):
    grupo_usuario = request.user.groups.all().first()
    return {'grupo_usuario': grupo_usuario}