
from django.conf.urls import url,include
from django.contrib import admin
from Home import urls as homeUrls
from accounts import urls as cuentasUrls
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(homeUrls, namespace="Home")),
    url(r'^accounts/',include(cuentasUrls)),
     url(
    	regex=r'^media/(?P<path>.*)$',
    	view=serve,
    	kwargs={'document_root':settings.MEDIA_ROOT}),
]
