from django.conf.urls import url
from . import views 

urlpatterns = [
    # /
    url(r'^$', views.index),

    # /courses
    url(r'^courses$', views.courses),

    # /delete/<id>
    url(r'^delete/(?P<id>\d+)$', views.delete)

]