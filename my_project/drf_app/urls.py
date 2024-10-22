from django.urls import path
from drf_app.views import profile_list_create, profile_detail, post_list_create, post_detail, author_detail, author_list_create, article_detail, article_list_create

urlpatterns = [
    # Profile
    path("profiles/", profile_list_create, name="profile_list_create"),
    path("profiles/<int:pk>", profile_detail, name="profile_detail"),

    # Post
    path("posts/", post_list_create, name="post_list_create"),
    path("posts/<int:pk>", post_detail, name="post_detail"),

    # Author
    path("authors/", author_list_create, name="author_list_create"),
    path("authors/<int:pk>", author_detail, name="author_detail"),

    # Article
    path("articles/", article_list_create, name="article_list_create"),
    path("articles/<int:pk>", article_detail, name="article_detail"),
]