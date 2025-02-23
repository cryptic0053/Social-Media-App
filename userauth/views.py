from itertools import chain
from  django . shortcuts  import  get_object_or_404, render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from . models import  Followers, LikePost, Post, Profile
from django.db.models import Q
from django.contrib import messages
from django.shortcuts import redirect




def signup(request):
 try:
    if request.method == 'POST':
        fnm=request.POST.get('fnm')
        emailid=request.POST.get('emailid')
        pwd=request.POST.get('pwd')
        print(fnm,emailid,pwd)
        my_user=User.objects.create_user(fnm,emailid,pwd)
        my_user.save()
        user_model = User.objects.get(username=fnm)
        new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
        new_profile.save()
        if my_user is not None:
            login(request,my_user)
            return redirect('/')
        return redirect('/loginn')
    
        
 except:
        invalid="User already exists"
        return render(request, 'signup.html',{'invalid':invalid})
  
    
 return render(request, 'signup.html')

def create_post(request):
    if request.method == 'POST':
        messages.success(request, "Post created successfully.")
        return redirect('profile')  # Redirect to the profile page or wherever appropriate
        
     
        
        
        
        
    

def loginn(request):
    if request.method == 'POST':
        email = request.POST.get('email')  # Get the email from the form
        pwd = request.POST.get('pwd')
        print(f"Attempting login with email: {email}")  # Debugging line
        
        try:
            user = User.objects.get(email=email)  # Get the user by email
            userr = authenticate(request, username=user.username, password=pwd)  # Authenticate with username
        except User.DoesNotExist:
            userr = None  # If user does not exist, set userr to None

        if userr is not None:
            login(request, userr)
            messages.success(request, "Login successful!")  # Optional success message
            return redirect('/')  # Redirect to the home page or dashboard
        else:
            messages.error(request, "Invalid email or password.")  # Error message for invalid credentials
            return render(request, 'loginn.html', {'invalid': "Invalid Credentials"})
    
    return render(request, 'loginn.html')

@login_required(login_url='/loginn')
def logoutt(request):
    logout(request)
    return redirect('/loginn')



@login_required(login_url='/loginn')
def home(request):
    
    following_users = Followers.objects.filter(follower=request.user.username).values_list('user', flat=True)

    
    post = Post.objects.filter(Q(user=request.user.username) | Q(user__in=following_users)).order_by('-created_at')

    profile = Profile.objects.get(user=request.user)

    context = {
        'post': post,
        'profile': profile,
    }
    return render(request, 'main.html',context)
    


@login_required(login_url='/loginn')
def upload(request):

    if request.method == 'POST':
        user = request.user.username
        image = request.FILES.get('image_upload')
        caption = request.POST['caption']

        new_post = Post.objects.create(user=user, image=image, caption=caption)
        new_post.save()

        return redirect('/')
    else:
        return redirect('/')

@login_required(login_url='/loginn')
def likes(request, id):
    if request.method == 'GET':
        username = request.user.username
        post = get_object_or_404(Post, id=id)

        like_filter = LikePost.objects.filter(post_id=id, username=username).first()

        if like_filter is None:
            new_like = LikePost.objects.create(post_id=id, username=username)
            post.no_of_likes = post.no_of_likes + 1
        else:
            like_filter.delete()
            post.no_of_likes = post.no_of_likes - 1

        post.save()

        # Generate the URL for the current post's detail page
        print(post.id)

        # Redirect back to the post's detail page
        return redirect('/#'+id)
    
@login_required(login_url='/loginn')
def explore(request):
    post=Post.objects.all().order_by('-created_at')
    profile = Profile.objects.get(user=request.user)

    context={
        'post':post,
        'profile':profile
        
    }
    return render(request, 'explore.html',context)
    
@login_required(login_url='/loginn')
def profile(request,id_user):
    user_object = User.objects.get(username=id_user)
    print(user_object)
    profile = Profile.objects.get(user=request.user)
    user_profile = Profile.objects.get(user=user_object)
    user_posts = Post.objects.filter(user=id_user).order_by('-created_at')
    user_post_length = len(user_posts)

    follower = request.user.username
    user = id_user
    
    if Followers.objects.filter(follower=follower, user=user).first():
        follow_unfollow = 'Unfollow'
    else:
        follow_unfollow = 'Follow'

    user_followers = len(Followers.objects.filter(user=id_user))
    user_following = len(Followers.objects.filter(follower=id_user))

    context = {
        'user_object': user_object,
        'user_profile': user_profile,
        'user_posts': user_posts,
        'user_post_length': user_post_length,
        'profile': profile,
        'follow_unfollow':follow_unfollow,
        'user_followers': user_followers,
        'user_following': user_following,
    }
    
    
    if request.user.username == id_user:
        if request.method == 'POST':
            if request.FILES.get('image') == None:
             image = user_profile.profileimg
             bio = request.POST['bio']
             location = request.POST['location']

             user_profile.profileimg = image
             user_profile.bio = bio
             user_profile.location = location
             user_profile.save()
            if request.FILES.get('image') != None:
             image = request.FILES.get('image')
             bio = request.POST['bio']
             location = request.POST['location']

             user_profile.profileimg = image
             user_profile.bio = bio
             user_profile.location = location
             user_profile.save()
            

            return redirect('/profile/'+id_user)
        else:
            return render(request, 'profile.html', context)
    return render(request, 'profile.html', context)

@login_required(login_url='/loginn')
def delete(request, id):
    post = Post.objects.get(id=id)
    post.delete()

    return redirect('/profile/'+ request.user.username)


@login_required(login_url='/loginn')
def search_results(request):
    query = request.GET.get('q')

    users = Profile.objects.filter(user__username__icontains=query)
    posts = Post.objects.filter(caption__icontains=query)

    context = {
        'query': query,
        'users': users,
        'posts': posts,
    }
    return render(request, 'search_user.html', context)

def home_post(request,id):
    post=Post.objects.get(id=id)
    profile = Profile.objects.get(user=request.user)
    context={
        'post':post,
        'profile':profile
    }
    return render(request, 'main.html',context)



def follow(request):
    if request.method == 'POST':
        follower = request.POST['follower']
        user = request.POST['user']

        if Followers.objects.filter(follower=follower, user=user).first():
            delete_follower = Followers.objects.get(follower=follower, user=user)
            delete_follower.delete()
            return redirect('/profile/'+user)
        else:
            new_follower = Followers.objects.create(follower=follower, user=user)
            new_follower.save()
            return redirect('/profile/'+user)
    else:
        return redirect('/')
    
    

@login_required(login_url='/loginn')
def post_list(request):
    # Get filter parameters from request
    date_filter = request.GET.get('date')
    media_type_filter = request.GET.get('media_type')
    author_filter = request.GET.get('author')
    search_query = request.GET.get('search')

    # Debug prints
    print(f"Search query: {search_query}")
    print(f"Date filter: {date_filter}")
    print(f"Media filter: {media_type_filter}")
    print(f"Author filter: {author_filter}")

    posts = Post.objects.all()
    print(f"Initial post count: {posts.count()}")

    # Apply filters
    if date_filter == 'latest':
        posts = posts.order_by('-created_at')
    elif date_filter == 'oldest':
        posts = posts.order_by('created_at')

    if media_type_filter == 'images':
        posts = posts.filter(image__isnull=False)
        print(f"After image filter: {posts.count()}")
    elif media_type_filter == 'text-only':
        posts = posts.filter(image__isnull=True)
        print(f"After text filter: {posts.count()}")

    if author_filter:
        posts = posts.filter(user=author_filter)
        print(f"After author filter: {posts.count()}")

    if search_query:
        posts = posts.filter(Q(caption__icontains=search_query) | Q(user__icontains=search_query))
        print(f"After search filter: {posts.count()}")

    profile = Profile.objects.get(user=request.user)
    
    context = {
        'post': posts,  # Changed from 'posts' to 'post' to match your template
        'profile': profile,
        'user': request.user.username
    }
    
    return render(request, 'main.html', context)
    
    
