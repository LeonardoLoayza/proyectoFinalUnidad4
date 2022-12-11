from django.contrib import admin
from django.urls import path, include # include allows us to call other urls from other apps
# basically with this imports below makes possible to show images in the frontend
from django.conf.urls.static import static 
from django.conf import settings 
from portfolio import views # import the views from portfolio app to be able to show the views :v 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'home'),
    path('blog/', include('blog.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # and also this


# to create a new user/admin use: 
# python manage.py createsuperuser 