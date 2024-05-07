
from django.urls import path,include
from . import views


urlpatterns = [
    path('blogposts/', views.BlogPostListCreate.as_view(),name='blogpost-view-create'),
    path(
        'blogposts/<int:pk>/',
        views.BlogPostRetriveUpdateDestroy.as_view(),
        name='update',
         ),
    path('blogposts/getlist/',views.BlogPostList.as_view(),name='list-by-title'),
]
