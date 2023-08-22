from django.shortcuts import render, redirect
import json
import os
from django.contrib import messages

# Create your views here.
def jsons(userjson):
    with open('user.json', 'w') as file:
        json.dump(userjson, file, indent=4)

def index(request):
    context = {}
    return render(request, 'mychatapp/index.html', context)

def userlog(request):
    if not os.path.exists('user.json'):
        jsons({})

    with open('user.json', 'r') as file:
        jsondata = json.load(file)
    
    if request.method == 'POST' and request.POST.get('uname'):
        name = request.POST['uname']
        mail = request.POST['umail']
        password = request.POST['upass']
        user = {
            'username': name,
            'usermail': mail,
            'userpass': password
        }
        user_id = 'user_id:{}'.format(len(jsondata) + 1)
        jsondata[user_id] = user

        with open("user.json", "w", encoding='utf-8') as json_file:
            json.dump(jsondata, json_file, indent=4)
        
        
        return redirect('userlog')
    
    elif request.method == 'POST' and request.POST.get('email'):
        email = request.POST['email']
        passw = request.POST['password']
        with open('user.json', 'r') as file:
                json_data = json.dumps(json.load(file))
                user_data = json.loads(json_data)
                for i in range(1,len(user_data)+1):
                    if email == user_data['user_id:{}'.format(i)]['usermail'] and passw in user_data['user_id:{}'.format(i)]['userpass']:
                        return redirect('dashboard')
                    else:
                        x = 'Нууц үг эсвэл мэйл хаяг буруу байна'
                messages.warning(request,x)
    return render(request, 'login.html')

def google_login(request):
    return render(request, 'google.html')

def facebook_login(request):
    return render(request, 'facebook.html')

def dashboard(request):
    userlog_context = request.session.get('user')
    return render(request, 'dashboard.html', {'userlog': userlog_context})
