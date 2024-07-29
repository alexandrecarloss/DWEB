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
from udemydrf.urls import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', adocaoViews.index, name='index'),
    path('adocao/', include('adocao.urls')),
    path('accounts/', include('accounts.urls')),
    path('venda/', include('venda.urls')),
    path('load_racas/', adocaoViews.load_racas, name="load_racas"),
    path('auth/', include('rest_framework.urls')),
    path('api/v1/', include('udemydrf.urls')),
    path('api/v2/', include(router.urls)),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

