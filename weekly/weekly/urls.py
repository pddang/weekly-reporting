"""weekly URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
import accounts.views as accounts_view
import reports.views as reports_view
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/accounts/$',accounts_view.accounts_list),
    url(r'^api/accounts/(?P<pk>[0-9]+)$', accounts_view.accounts_detail),
    url(r'^api/reports/$',reports_view.reports_list),
    url(r'^api/reports/(?P<pk>[0-9]+)$', reports_view.reports_detail),
]
