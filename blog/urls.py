from django.urls import path
from . import views

urlpatterns = [
    #記事リストページ
    path('', views.post_list, name='post_list'),

    #記事詳細ページ
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    
    #新規作成ページ
    path('post/new/', views.post_new, name='post_new'),
    
    #記事編集ページ
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    
    #未公開記事リストページ
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    
    #記事公開ページ
    path('post/<pk>/publish/', views.post_publish, name='post_publish'),

    #記事削除ページ
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),

    #コメント追加ページ
    path('post/<int:pk>/comment/',views.add_comment_to_post, name='add_comment_to_post'),

    #コメント承認
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    
    #コメント削除
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
]