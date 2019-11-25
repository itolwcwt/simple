from comment.models import Comment
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from food.models import Article
from .forms import CommentForm


@login_required(login_url='user/login')
def comment(request, sid):
    article = get_object_or_404(Article, id=sid)

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.article = article
            new_comment.user = request.user
            new_comment.save()
            return redirect(article)
        else:
            return HttpResponse("内容有误，请重新填写。")
    else:
        return HttpResponse("发表评论仅接受POST请求。")



