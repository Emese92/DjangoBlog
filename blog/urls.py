from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    # The first slug in angle  brackets is called a path converter. 
    # The second slog is a keyword name.
    # The path converter converts this text into a slug  field, it tells Django to match any slug string
    path('like/<slug:slug>/', views.PostLike.as_view(), name='post_like'),
]