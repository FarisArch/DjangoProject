from django.urls import path
from . import views
# Add url patterns below
urlpatterns = [
    path('',views.post_list,name='post-list'),
]
