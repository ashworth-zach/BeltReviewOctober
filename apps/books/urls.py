from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^add$', views.addbook),
    url(r'^new$', views.newbook),
    url(r'^(?P<bookid>\d+)$', views.show),
    url(r'^addreview$', views.addreview),

]  