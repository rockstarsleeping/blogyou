from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=500, unique=True, help_text="Title of the article")
    article_image = models.ImageField(blank=True, help_text="Article Image")
    slug = models.SlugField(unique=True)
    content = models.TextField(help_text="Content")
    description = models.TextField(help_text="What is the article about?")
    likes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)
    def get_absolute_url(self):
        return "/blog/articles/%s/" % self.slug

    def __str__(self):
        return self.title
