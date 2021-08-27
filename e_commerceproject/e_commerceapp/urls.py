from django.urls import path
from . import views
urlpatterns = [
    path('customer/',views.ListCustomer.as_view()),
    path('customerdetails/<int:pk>/',views.DetailCustomer.as_view()),
    path('categories/',views.ListCategory.as_view()),
    path('categoriesdetails/<int:pk>/',views.DetailCategory.as_view()),
    path('products/',views.ListProduct.as_view()),
    path('productsdetails/<int:pk>/',views.DetailProduct.as_view()),


]