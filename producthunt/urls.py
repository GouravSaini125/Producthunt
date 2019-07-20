from products import views
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('accounts/', include('accounts.urls')),
    path('cart/', include('cart.urls')),
    path('auth/', include('social_django.urls', namespace='social')),
    path('products/', include('products.urls')),
    url(r'^response/', views.response, name="response"),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
