from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Profile
from .forms import ProfileForm, CheckPasswordForm
# decorators import
from django.contrib.auth.decorators import login_required
# needed when define signup:
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
# needed when define user_delete:
from django.contrib.auth import logout as auth_logout
# needed when define profile_edit:
from django.core.files.storage import FileSystemStorage
from blog.models import Post 

# 이름 수정 필요.
def base(request):
    posts = Post.objects.all()
    new_post = []

    for post in posts:
        a=[post,post.count_likes_user()]
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

        
    ctx={'posts':final_post}
    
    return render(request, 'accounts/base.html',ctx)                                   


def signup(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auth_login 인자로 user를 넘겨줘서 자동 로그인
            auth_login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            next_url = request.GET.get('next') or reverse("accounts:base") #회원가입 후 이동
            return redirect(next_url)
        else:
            return render(request, "accounts/signup.html", {'form':form})
    else:
        form=UserCreationForm()
        return render(request, "accounts/signup.html", {'form':form})

@login_required
def signup_completed(request):
    return render(request, 'accounts/signup_completed.html')

@login_required
def profile(request):
    profile = Profile.objects.get(user=request.user)
    ctx = {'profile':profile}
    return render(request, 'accounts/profile.html', ctx)

@login_required
def profile_edit(request):
    # if request.method=='POST':
    #     name = request.POST['name']
    #     nickname = request.POST['nickname']
    #     email = request.POST['nickname']
    #     image = request.FILES['image']
    #     # 따로 이미지 저장소를 파고, 이미지 링크만 남기는게 일반적.
    #     if image:
    #         fs=FileSystemStorage()
    #         filename=fs.save(image.name, image)
    #         uploaded_file_url = fs.url(filename)
    #     Profile.objects.filter(user=request.user).update(name=name, nickname=nickname, email=email, image=image)
    #     url = reverse("accounts:profile")
    #     return redirect(url)
    # else:
    #     profile = get_object_or_404(Profile, user=request.user)
    #     return render(request, 'accounts/profile_edit.html', {'profile':profile})

    profile = Profile.objects.get(user=request.user)
    if request.method=='POST':
        profileform = ProfileForm(request.POST, request.FILES, instance=profile)
        if profileform.is_valid():
            profile = profileform.save()
            url = reverse("accounts:profile")
            return redirect(url)
    else:
        profileform = ProfileForm(instance=profile)
        return render(request, 'accounts/profile_edit.html', {'profileform':profileform})

# 계정 탈퇴(redirect url 추후 수정 필요)
@login_required
def user_delete(request):
    if request.method == 'POST':
        password_form = CheckPasswordForm(request.user, request.POST)
        
        if password_form.is_valid():
            request.user.delete()
            auth_logout(request)
            url = reverse("accounts:base")
            return redirect(url)
    else:
        password_form = CheckPasswordForm(request.user)

    return render(request, 'accounts/user_delete.html', {'password_form':password_form})
