from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout


# homepage
def homepage(request):
    blog=Blog.objects.all()[:2]
    post=About.objects.all()[:2]
    return render(request,'index.html',{
        "blog":blog,
        "post":post,
    })

# blogpage
def blogpage(request):
    blogs=Blog.objects.all()
    return render(request,'blogpage.html',
                  {
                      "blogs":blogs,
                  })

# induvidualblog
@login_required(login_url='login')
def blog(request,blogid):
    blogs=get_object_or_404(Blog,id=blogid)
    comments=blogs.comment.all()

    if request.method=="POST":
        comment_txt=request.POST.get('comment')
        if comment_txt:
            new_comment=Comment.objects.create(comment_user=request.user,comment=comment_txt)
            new_comment.save()
            blogs.comment.add(new_comment)
            
            return redirect ('blog', blogid=blogid)

    return render(request,'blog.html',
                  {
                      "blog":blogs,
                      "comments":comments,
                  })

@login_required(login_url='login')
def delete_cmnt(request,blogid,cmntid):
    comment=get_object_or_404(Comment,id=cmntid)
    if request.user==comment.comment_user:
        if request.method=="POST":
            comment.delete()
            return redirect('blog',blogid=blogid)
        return redirect('blog',blogid=blogid)


# contactpage
def contactpage(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        comment=request.POST.get('comment')

        new_contact=Contact(
            name=name,
            email=email,
            subject=subject,
            description=comment,
        )
        new_contact.save()
    return render(request,'contact.html')

# aboutpage
def aboutpage(request):
    post=About.objects.all()
    return render(request,'about.html',
                  {
                      "post":post,
                  })

# login
def login(request):
    message=""
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)
        if user is not None:
            auth_login(request,user)
            return redirect("home")
        else:
            message="Error, Couldn't Connect !!"

    return render(request,'login.html',
                  {
                       "message":message,
                  })


# logout
@login_required(login_url='login')
def logout(request):
    auth_logout(request)
    return redirect("home")

@login_required(login_url='login')
def presslike(request,id):
    if request.method == "POST":
        post = Blog.objects.get(id=int(id))

        if not post.post_likes.filter(liked_user=request.user):
            newlike = Like(liked_user=request.user)
            newlike.save()

            post.post_likes.add(newlike)
            post.save()

        return redirect('blog',id=id)




#addcomment
@login_required(login_url='login')
def addcomment(request,id):
    if request.method == "POST":
        comment = request.POST.get('comment')

        post = Blog.objects.get(id=int(id))

        newcomment = Comment(comment_user=request.user,comment=comment)
        newcomment.save()

        post.comment.add(newcomment)
        post.save()
        
        return redirect('blog')


def press_c_likes(request,postid,commentid):
    if request.method == "POST":
        post = Blog.objects.get(id=int(postid))
        comment = Comment.objects.get(id=int(commentid))

        if not comment.comment_likes.filter(c_liked_user=request.user):
            new_clike = C_Like(c_liked_user=request.user)
            new_clike.save()

            comment.comment_likes.add(new_clike)
            comment.save()

    return redirect("blog",id=post.id)