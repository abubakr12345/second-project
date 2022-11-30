from django.urls import path
from crud.views import article_func , article_detail, article_create, article_edit,like_article,like_article,dislike_article,article_delete,delete_comment,edit_comment

urlpatterns = [
    path("",article_func , name='article_func'),
    path('<slug>',article_detail,name='article_detail'),
    path('article_create/', article_create, name='article_create'),
    path('<slug>/edit',article_edit,name='article_edit'),
    path('<slug>/delete',article_delete,name ='article_delete'),

    path('<slug>/like',like_article,name ='article_like'),
    path('<slug>/dislike',dislike_article,name ='article_dislike'),
    path('<slug>/comment/<pk>/delete', delete_comment , name='comment_delete'),

    path('<slug>/comment/<pk>/edit', edit_comment , name='comment_edit'),
    
]

