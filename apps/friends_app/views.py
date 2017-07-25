from django.shortcuts import render, redirect
from .models import User

# Create your views here.
def home(request):
    if not request.session['userId']:
        return redirect('/')
    context = {
        'people':User.objects.all().order_by('-created_at').exclude(id=request.session['userId'])[:3]
    }   
    return render(request, 'friends_app/home.html', context)

def addFriend(request):
    if not request.session['userId']:
        return redirect('/')
    user = User.objects.get(id=request.session['userId'])
    context = {
        'friends':User.objects.all().exclude(friends = user.id).exclude(id=request.session['userId'])
    }
    return render(request, 'friends_app/addFriend.html', context)

def add(request):
    if not request.session['userId']:
        return redirect('/')
    user = User.objects.get(id=request.session['userId'])
    friend = User.objects.get(id=request.POST['friendId'])
    user.friends.add(friend)
    user.save()
    friend.friends.add(user)
    print user.friends.all()[0].first_name
    return redirect('/addFriend')

def show(request):
    if not request.session['userId']:
        return redirect('/')
    user = User.objects.get(id=request.session['userId'])
    context = {
        'friends':user.friends.all(),
        'count':user.friends.count()
    }
    return render(request, 'friends_app/show.html', context)

def deleteFriend(request):
    if not request.session['userId']:
        return redirect('/')
    user = User.objects.get(id=request.session['userId'])
    friend = User.objects.get(id=request.POST['friendId'])
    user.friends.remove(friend)
    user.save()
    friend.friends.remove(user)
    return redirect('/show')

def logout(request):
    request.session['userId']=None
    return redirect('/')

