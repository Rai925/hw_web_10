from django.contrib import admin
from django.urls import path, include

app_name = 'quotes_scraper'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('quotes.urls')),
    path('quotes/', include('quotes.urls')),
    path('users/', include('users.urls')),
    path('accounts/', include('allauth.urls')),
]
