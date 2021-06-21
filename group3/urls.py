"""group3 URL Configuration

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
from mysite.views import index,logout,rank,paper
from mysite.views import index,logout,rank,chart
from mysite.views import show
from mysite.views import detailed
from mysite.views import aboutus
from mysite.views import metal
from mysite.views import plastic
from mysite.views import glass
from mysite.views import textile
from mysite.views import ea
from mysite.views import battery
from mysite.views import cs
from mysite.views import drug
from mysite.views import oil
from mysite.views import other
from mysite.views import yilan,keelung,taipei,newtaipei,taoyuan,hsinchu,hsinchuc
from mysite.views import miaoli,taichung,changhua,nantou,yunlin
from mysite.views import chiayi,chiayic,tainan,kaohsiung,pingtung
from mysite.views import taitung,hualien,penghu,kinmen,renjiang
urlpatterns = [
	path('show<int:id>/', show),
    path('aboutus/',aboutus),
    path('detailed/',detailed),
    path('admin/', admin.site.urls),
    path('rank/',rank),
    path('paper/',paper),
    path('metal/',metal),
    path('plastic/',plastic),
    path('glass/',glass),
    path('textile/',textile),
    path('ea/',ea),
    path('battery/',battery),
    path('cs/',cs),
    path('drug/',drug),
    path('oil/',oil),
    path('other/',other),
    path('yilan/',yilan),
    path('keelung/',keelung),
    path('taipei/',taipei),
    path('newtaipei/',newtaipei),
    path('taoyuan/',taoyuan),
    path('hsinchu/',hsinchu),
    path('hsinchuc/',hsinchuc),
    path('miaoli/',miaoli),
    path('taichung/',taichung),
    path('changhua/',changhua),
    path('nantou/',nantou),
    path('yunlin/',yunlin),
    path('chiayi/',chiayi),
    path('chiayic/',chiayic),
    path('tainan/',tainan),
    path('kaohsiung/',kaohsiung),
    path('pingtung/',pingtung),
    path('taitung/',taitung),
    path('hualien/',hualien),
    path('penghu/',penghu),
    path('kinmen/',kinmen),
    path('renjiang/',renjiang),
    path('chart/',chart),
    path('logout/',logout),
    path('',index),

]
