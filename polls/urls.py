from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('list/', views.viewlist, name="list"),
    path('detail/<int:questions_id>', views.detail, name="details"),
    path('<int:questions_id>',views.vote,name="vote")
]


