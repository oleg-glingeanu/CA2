from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('',views.allProdCat, name='allProdCat'),
    path('<uuid:category_id>/',views.allProdCat, name='products_by_category'),
]