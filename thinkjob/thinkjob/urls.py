"""thinkjob URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

#from offers.views import my_first_view
from offers.views import offer_detail, offer_list, offer_add, enterprise_detail


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^offer_detail/(?P<offer_id>\d)/$', offer_detail, name='offer_detail'),
    url(r'^offer_add/$', offer_add, name='offer_add'),
    url(r'^$', offer_list),

    url(r'^enterprise_detail/(?P<enterprise_id>\d)/$', enterprise_detail, name='enterprise_detail'),
]
