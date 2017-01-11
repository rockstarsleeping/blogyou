from django.shortcuts import render
from blog.models import Article
from django.http import HttpResponseRedirect, HttpResponse
from django_comments.models import Comment
# Create your views here.

def index(request):
    return render(request, "blog/index.html" )

def articles(request):
    article_list = Article.objects.order_by("-views")
    context_dict = {"articles": article_list}
    return render(request, "blog/articles.html", context_dict)


def show_article(request, article_title_slug):
    article = Article.objects.get(slug=article_title_slug)
    views = article.views
    views = views + 1
    article.views = views
    article.save()
    context_dict = {"article":article}
    return render(request, "blog/show_article.html", context_dict)

def comment_posted(request):
    if request.GET['c']:
        comment_id = request.GET['c']
        comment = Comment.objects.get(pk=comment_id )
        article = Article.objects.get(id=comment.object_pk)

        if article:
            return HttpResponseRedirect(article.get_absolute_url())

    return HttpResponseRedirect('/')

def like_article(request):
    art_id = None
    if request.method == 'GET':
        art_id = request.GET['article_id']
        likes = 0
        if art_id:
            article = Article.objects.get(id=int(art_id))
            if article:
                likes = article.likes + 1
                article.likes = likes
                article.save()

    return HttpResponse(likes)
