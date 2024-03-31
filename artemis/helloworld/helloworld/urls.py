"""helloworld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from adocao import views as adocaoViews
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', adocaoViews.index, name='index'),
    path('adocao/', adocaoViews.adocao, name='adocao'),
    path('adocao/load_racas/', adocaoViews.load_racas, name="load_racas"),
    path('adocao/load_pets/', adocaoViews.load_pets, name="load_pets"),
    #path('login/', adocaoViews.login, name="login"),
    path('adocao/petdetalhe/<int:petid>', adocaoViews.petdetalhe, name="petdetalhe"),
    path('adocao/cadastropet', adocaoViews.cadastropet, name="cadastropet"),
    path('adocao/salvarpet', adocaoViews.salvarpet, name="salvarpet"),
    path('adocao/fotopet/<int:petid>/<int:multiplo>', adocaoViews.fotopet.as_view(), name="fotopet"),
    path('accounts/', include('accounts.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

