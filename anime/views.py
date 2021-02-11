from django.shortcuts import render,redirect
from airtable import Airtable
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required

# Create your views here.
AT = Airtable(base_key='', table_name='', api_key='')

def home_page(request):
    user_query = str(request.GET.get('query'))
    search_result = AT.get_all(formula="FIND('"+ user_query.lower() + "',LOWER({Name}))") or AT.get_all(sort='Name')
    return render(request,'animes/home.html',{'search_result':search_result})

def create_page(request):
    return render(request,'animes/create_anime.html')

def create(request):
    if request.method == 'POST':
        data = {
            'Name': request.POST.get('name'),
            'Image': [{'url': request.POST.get('url') or "https://www.telegraphcomics.com/images/NoImage.jpg"}],
            'Rating': int(request.POST.get('rating')),
            'Genre': request.POST.get('desc'),
            'Votes': 0,
        }
        try:
            response = AT.insert(data)
            messages.success(request,'New Anime Added: {}'.format(response['fields'].get('Name')))
        except Exception as e:
            messages.error(request,'{}'.format(e))
    return redirect('/')

def edit(request,anime_id):
    if request.method == 'POST':
        data = {
            'Name': request.POST.get('name'),
            'Image': [{'url':request.POST.get('url')}],
            'Rating': int(request.POST.get('rating')),
            'Genre': request.POST.get('desc'),
        }
        try: 
            response = AT.update(anime_id,data)
            messages.success(request,'{} Updated'.format(response['fields'].get('Name')))
        except Exception as e:
            messages.error(request,'{}'.format(e))
    return redirect('/')

def delete(request,anime_id):
    try:
        response = AT.delete(anime_id)
        messages.success(request,'Anime Deleted Successfully')
    except Exception as e:
        messages.error(request,'{}'.format(e))
    return redirect('/')


def register(request):
    if request.method == 'POST':
        username = request.POST["username"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
                return redirect('/')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email already in use")
                return redirect('/')
            else:
                user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password1)
                user.save();
                messages.success(request,'Registration Successful, Please Login Now')
                return redirect('/')
        else:
            messages.info(request,"Both password not matching")
            return redirect('/')

def login(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username,password=password)
        if user is not None: 
            auth.login(request,user)
            messages.success(request,'Hello {}'.format(username))
            return redirect('/')
        else:
            messages.info(request,"Invalid credentials")    
            return redirect('/')

def logout(request): 
    auth.logout(request)
    return redirect('/')

@login_required
def upvote(request,anime_id):
    curr = AT.get(record_id=anime_id)
    vote = (curr['fields']['Votes'])
    vote+=1
    AT.update(anime_id,{'Votes':vote})
    messages.success(request,"Your Vote Was Successfully Registered")
    return redirect('/')

def sortAnime(request,type):
    AT.get_all(sort=type)
    return redirect('/')