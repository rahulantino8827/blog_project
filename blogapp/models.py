from django.db import models

# Create your models here.

class BlogModel(models.Model):
    blog_title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    blog_type = models.CharField(max_length=200)
    tags = models.CharField(max_length=200)
    thumbnail_image = models.URLField(max_length=200,null=True,blank=True)
    auther_name = models.CharField(max_length=200)
    bio = models.CharField(max_length=200)
    twitter_link = models.URLField(max_length=200)
    instagram_link = models.URLField(max_length=200)
    linkdin_link = models.URLField(max_length=200)
    meta_desc = models.TextField(max_length=500)
    meta_keyword = models.CharField(max_length=200)
    meta_title = models.CharField(max_length=200)
    content = models.JSONField(default=list)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.blog_title