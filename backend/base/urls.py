from django.urls import path
from . import views


urlpatterns = [
    path('users/login/', views.TokenObtainPairView.as_view(), 
    name='token_obtain_pair'),
    path('', views.getRoutes, name="routes"),
    path('users/profile/', views.getUserProfile, name="user-profile"),
    path('products/', views.getProducts, name="products"),
    path('product/<str:pk>/', views.getProduct, name="product"),
]

# {
#     "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY3NTQwMTI3NiwianRpIjoiMzYzMTU1YWRlZjVkNDU4OWEyZjE2M2U3ZmE1MDZlMzQiLCJ1c2VyX2lkIjoxfQ.qtEHR6ccOf7I1a33x7bFVyvQmwVH_PqPvcy9yhciS7s",
#     "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc3OTA2ODc2LCJqdGkiOiJmMDk1NTFjZjY4N2Y0NzdkYTNmYzU4MDI3ZGVhMjg1OSIsInVzZXJfaWQiOjF9.IjdN-ZlAUQdooHRfJhb471_kSxaG1Ln9xMnol1NJAXI"
# }