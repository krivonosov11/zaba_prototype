"""dzenzaba URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static

# from sitemap.views import sitemap


urlpatterns = [
    # path('sitemap.xml', sitemap, name='sitemap-xml'),
    path('admin/', admin.site.urls),
    path('login/', auth_views.login, name='login'),
    path('logout/', auth_views.logout, name='logout'),
    path('i18n/', include('django.conf.urls.i18n')),
    # url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
]

urlpatterns += i18n_patterns(
    path('', views.home, name='home'),
    path('jobs/', include('jobs.urls')),
    path('rents/', include('rents.urls')),
    path('items/', include('items.urls')),
    path('gifts/', include('gifts.urls')),
)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        path('rosetta/', include('rosetta.urls'))
    ]
