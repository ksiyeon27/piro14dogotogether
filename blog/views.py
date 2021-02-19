from django.utils.text import slugify
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.urls import reverse
from django.db import models
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from piroproject.views import OwnerOnlyMixin
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView
from django.db.models import Q
from blog.forms import PostSearchForm
from blog.models import Post, Comment
from django.conf import settings
from django.views.generic.dates import DayArchiveView, TodayArchiveView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.views.generic import ListView, DetailView, TemplateView, UpdateView, DeleteView, CreateView
from django.views.generic.edit import BaseDeleteView
from django.shortcuts import render, get_object_or_404, HttpResponse
from django.http import HttpResponse, request
import json
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib import messages
from .models import Post
from django.views.decorators.csrf import csrf_exempt


@login_required
@require_POST
def post_like(request):
    pk = request.POST.get('pk', None)
    post = get_object_or_404(Post, pk=pk)
    user = request.user

    if post.likes_user.filter(id=user.id):
        post.likes_user.remove(request.user)
        message = '좋아요 취소'
    else:
        post.likes_user.add(request.user)
        message = '좋아요'

    context = {'likes_count': post.count_likes_user(), 'message': message}
    return HttpResponse(json.dumps(context), content_type="application/json")

class PostLV(ListView):
    model = Post
    template_name = 'blog/post_all.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = Post.objects.all()
        new_post = []
        for post in posts:
            a = [post, post.count_likes_user()]
            new_post.append(a)

        sorted_post=sorted(new_post, key=lambda x: x[1], reverse=True)
        final_post=[]
        if len(sorted_post) <= 5:
            for i in range(len(sorted_post)):
                a=sorted_post[i][0]
                final_post.append(a)
        else:
            for i in range(5):
                a=sorted_post[i][0]
                final_post.append(a)
        context['sorted']=final_post
        return context


class PostDV(DetailView):
    model = Post
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get(self.pk_url_kwarg, None)
        post=get_object_or_404(Post,pk=pk)
        if post.likes_user.filter(id=self.request.user.id):
            likes=True
        else:
            likes=False
        context['likes']=likes
        context['comments'] = Comment.objects.filter(post=self.object.id)
        return context
    

class PostAV(ArchiveIndexView):
    model = Post
    date_field = 'modified_at'

class PostYAV(YearArchiveView):
    model = Post
    date_field = 'modified_at'
    make_object_list = True

class PostMAV(MonthArchiveView):
    model = Post
    date_field = 'modified_at'

class PostDAV(DayArchiveView):
    model = Post
    date_field = 'modified_at'

class PostTAV(TodayArchiveView):
    model = Post
    date_field = 'modified_at'

class TagCloudTV(TemplateView):
    template_name = 'taggit/taggit_cloud.html'

class TaggedObjectLV(ListView):
    template_name = 'taggit/taggit_post_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(tags__name=self.kwargs.get('tag'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tagname'] = self.kwargs['tag']
        return context

class SearchFormView(FormView):
    form_class = PostSearchForm
    template_name = 'blog/post_search.html'

    def form_valid(self, form):
        searchWord = form.cleaned_data['search_word']
        search_type = self.request.POST.get('type', '')
        if search_type == 'all':
            post_list = Post.objects.filter(Q(title__icontains=searchWord) | Q(content__icontains=searchWord)).distinct()
        elif search_type == 'title':
            post_list = Post.objects.filter(Q(title__icontains=searchWord))
        elif search_type == 'content':
            post_list = Post.objects.filter(Q(content__icontains=searchWord))
        elif search_type == 'writer':
            post_list = Post.objects.filter(owner__username__icontains=searchWord)

        context = {'form': form, 'search_term': searchWord, 'object_list': post_list}

        return render(self.request, self.template_name, context)

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'image','secret','tags','owner']
    success_url = reverse_lazy('blog:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)



class PostUpdateView(OwnerOnlyMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'image', 'secret', 'tags']
    success_url = reverse_lazy('blog:index')
    
class PostDeleteView(OwnerOnlyMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog:index')


def comment_write_view(request, pk):
    post = get_object_or_404(Post, id=pk)
    writer = request.POST.get('writer')
    content = request.POST.get('content')
    if content:
        comment = Comment.objects.create(post=post, content=content, writer=request.user)
        post.save()
        data = {
            'writer': writer,
            'content': content,
            'created': '방금 전',
            'comment_id': comment.id
        }
        if request.user == post.owner:
            data['self_comment'] = '(글쓴이)'

        return HttpResponse(json.dumps(data, cls=DjangoJSONEncoder), content_type="application/json")



def comment_delete_view(request,pk):
    post = get_object_or_404(Post, id=pk)
    comment_id = request.POST.get('comment_id')
    target_comment = Comment.objects.get(pk=comment_id)

    if request.user == target_comment.writer or request.user.level == '1' or request.user.level == '0':
        target_comment.deleted = True
        target_comment.delete()
        post.save()
        data = {
            'comment_id': comment_id,
            'deleted':target_comment.deleted,
        }
        return HttpResponse(json.dumps(data, cls=DjangoJSONEncoder), content_type = "application/json")

@csrf_exempt
@login_required
def comment_modify_view(request,pk):
    if request.method == 'POST':
        req = json.loads(request.body)
        content=req['content']
        pk=req['pk']
        writer=req['writer']
        comment = get_object_or_404(Comment, id=pk)
        comment.content = content
        comment.save()
        data = {
            'writer': writer,
            'content': content,
            'created': '방금전',
            'comment_id': comment.id
        }
        if request.user == comment.post.owner:
            data['self_comment'] = '(글쓴이)'
        else:
            data['self_comment'] = ''
        return JsonResponse(data)
    elif request.method == 'GET':
        return render(request, 'base.html')
    