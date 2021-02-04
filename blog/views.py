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
from blog.models import Post
from django.conf import settings
from django.views.generic.dates import DayArchiveView, TodayArchiveView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.views.generic import ListView, DetailView, TemplateView, UpdateView, DeleteView, CreateView
from django.shortcuts import render, get_object_or_404, HttpResponse

@login_required
@require_POST
def post_like(request):
    pk = request.POST.get('pk', None)
    post = get_object_or_404(Post, pk=pk)
    user = request.user

    if post.likes_user.filter(id=user.id):
        post.likes_user.remove(user)
        message = '좋아요 취소'
    else:
        post.likes_user.add(user)
        message = '좋아요'

    context = {'likes_count': post.count_likes_user(), 'message': message}
    return HttpResponse(json.dumps(context), content_type="application/json")

class PostLV(ListView):
    model = Post
    template_name = 'blog/post_all.html' # 왜 기본값 세팅이 post_list가 되는건가?
    context_object_name = 'posts'
    paginate_by = 5

class PostDV(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['disqus_short'] = f"{settings.DISQUS_SHORTNAME}"
        context['disqus_id'] = f"post-{self.object.id}"
        context['disqus_url'] = f"{settings.DISQUS_MY_DOMAIN}{self.object.get_absolute_url()}"
        context['disqus_title'] = f"{self.object.title}"
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
        post_list = Post.objects.filter(Q(title__icontains=searchWord) | Q(description__icontains=searchWord)).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = searchWord
        context['object_list'] = post_list

        return render(self.request, self.template_name, context)

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'image','tags','owner']
    success_url = reverse_lazy('blog:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)



class PostUpdateView(OwnerOnlyMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'image','tags']
    success_url = reverse_lazy('blog:index')
    
class PostDeleteView(OwnerOnlyMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog:index')


# Create your views here.
