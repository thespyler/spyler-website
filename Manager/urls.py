from .views import *
from django.urls import path

urlpatterns = [
	path('', main),
	path('c/', c),
	path('django/', django),
	path('flask/', flask),
	path('matplotlib/', matplotlib),
	path('signin/', signup),
]