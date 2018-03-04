from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import Post, Category, Comment, Reply
from datetime import datetime

# Create your views here.

# Post Views
def Pindex(request):
    
    list = Post.objects.all()
    context = {
        'list':list,
    }
    
    return render(request, 'Articles/post/index.html',context)



def Pshow(request, post_id):
    
    post    = get_object_or_404(Post, pk = post_id)
    
    context = {'post':post}

    return render(request, 'Articles/post/details.html', context)



def Pcreate(request):
    
    categories = Category.objects.all()
    
    context = {
        'categories' : categories,
    }
    
    return render(request, 'Articles/post/create.html',context)



def Pupdate(request, post_id):
    if request.method == 'POST':
        
        p = Post.objects.get(pk=post_id)
        
        p.title       = request.POST.get("title")
        p.body        = request.POST.get("body")
        p.category_id = request.POST.get("category")
        p.categor     = Category.objects.get(pk=p.category_id)
        p.user_id     = request.user.id
        p.Author      = request.user
        p.updated_at  = datetime.now()
        p.save()
        
        return render(request, 'Articles/post/details.html', { 'post' : p } )
    
    else:
        return HttpResponse("Sorry you aren't allowed.")
    
    
    
def Pedit(request, post_id):
    
    if request.method == 'POST':
        p = Post.objects.get(pk=post_id)
        
        categories = Category.objects.all()
        
        context = {
            'categories' : categories,
            'post'       : p,
        }
        return render(request,'Articles/post/edit.html', context)
    
    else:
        return HttpResponse("Sorry you aren't allowed.")




def Pstore(request):
    
    if request.method == 'POST':
        
        p = Post(
            title       = request.POST.get("title"),
            body        = request.POST.get("body"),
            category_id = request.POST.get("category"),
            user_id     = request.user.id,
        )
        
        p.Author        = request.user
        p.categor       = Category.objects.get(pk=p.category_id)
        
        p.save()
        
        return render(request, 'Articles/post/details.html',{'post':p})
    
    else:
        return HttpResponse("Sorry you aren't allowed.")
    


def Pdelete(request, post_id):
    
    if request.method == 'POST':
        
        p = Post.objects.get(pk=post_id)
        p.delete()
        return redirect('/Articles')
    
    else:
        return HttpResponse("Sorry you aren't allowed.")
    




# Comment Views

def Cstore(request, post_id):
    
    if request.method == 'POST':
        
        c = Comment(
            body    = request.POST.get("body"),
        )
        
        c.Author    = request.user
        c.post      = Post.objects.get(pk=post_id)
        
        c.save()
        
        return render(request,'Articles/post/details.html',{"post":c.post})
    
    else:
        return HttpResponse("Sorry you aren't allowed.")
    
    
    
    
# Reply Views

def Rstore(request, comment_id):
    
    if request.method == 'POST':
        
        r = Reply(
            body    = request.POST.get("body"),
        )
        
        r.Author    = request.user
        r.comment      = Comment.objects.get(pk=comment_id)
        
        r.save()
        
        return render(request,'Articles/post/details.html',{"post":r.comment.post})
    
    else:
        return HttpResponse("Sorry you aren't allowed.")

