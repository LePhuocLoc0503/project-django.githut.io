from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    #path('detail/<int:id>', views.detail(), name="detail"),
    path('list/', views.viewlist, name="view_list"),
]


