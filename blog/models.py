from django.conf import settings
from django.db import models
from django.utils import timezone

#ポストモデル(記事)
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    
    #公開メソッド
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    #非公開メソッド
    def private(self):
        self.published_date = None
        self.save()

    #承認されたコメントを返す
    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

    def __str__(self):
        return self.title

    

#コメントモデル
class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    #承認メソッド
    def approve(self):
        self.approved_comment = True
        self.save()
    
    #未承認メソッド
    def unapprove(self):
        self.approved_comment = False
        self.save()

    def __str__(self):
        return self.text