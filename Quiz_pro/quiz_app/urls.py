from django.urls import path
from .views import home, post, search, add_comment, add_subcomment


urlpatterns = [
    path('', home, name = 'home'),
    path('search', search, name='search'),
    path('add_comment', add_comment),
    path('add_subcomment', add_subcomment),
]
