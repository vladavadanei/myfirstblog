from django.shortcuts import render, get_object_or_404
from .models import Post
from .models import Cv
from django.utils import timezone
from .forms import PostForm
from .forms import CvForm
from django.shortcuts import redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

# Create your views here.
def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post': post})
	
def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm()
	return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm(instance=post)
	return render(request, 'blog/post_edit.html', {'form': form})
	
def login(request):
    return render(request, 'registration/login.html')
	
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            auth_login(request, user)
            return redirect('post_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def cv_list(request):
	cvs = Cv.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/cv_list.html', {'cvs': cvs})
	
def cv_detail(request, pk):
	cv = get_object_or_404(Cv, pk=pk)
	return render(request, 'blog/cv_detail.html', {'cv': cv})
	
def cv_new(request):
	if request.method == "POST":
		form = CvForm(request.POST)
		if form.is_valid():
			cv = form.save(commit=False)
			cv.author = request.user
			cv.published_date = timezone.now()
			cv.save()
			return redirect('cv_detail', pk=cv.pk)
	else:
		form = CvForm()
	return render(request, 'blog/cv_edit.html', {'form': form})

def cv_edit(request, pk):
	cv = get_object_or_404(Cv, pk=pk)
	if request.method == "POST":
		form = CvForm(request.POST, instance=cv)
		if form.is_valid():
			cv = form.save(commit=False)
			cv.author = request.user
			cv.published_date = timezone.now()
			cv.save()
			return redirect('cv_detail', pk=cv.pk)
	else:
		form = CvForm(instance=cv)
	return render(request, 'blog/cv_edit.html', {'form': form})