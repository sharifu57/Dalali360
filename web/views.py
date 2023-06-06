from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth import login
from django.contrib import messages
from web.forms import *
from django.shortcuts import redirect
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required,permission_required
from web.user_manager import *
from django.contrib.auth.models import User
from dalali.models import *
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
import json


# Create your views here.

class MainView(View):
    @method_decorator(never_cache)
    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)



class UserLoginView(View):
    def get(self, request, *args, **kwargs):
        form = UserLoginForm()
        context = {
            'form': form,
        }
        return render(request,'authentication/login.html', context)

    def post(self, request, *args, **kwargs):
        form = UserLoginForm(request.POST)

        if form.is_valid():
            user = form.login(request)
            if user:
                login(request, user)
                # messages.info(request,'User login successful')
                return redirect("dashboard")
            else:
                messages.error(request, 'User not found')
                return redirect("login_page")

        else:
            messages.error(request, 'User login failed')
            context = {
                'form': form
            }
            return render(request,'authentication/login.html', context)


class HomeView(View):
    @method_decorator(never_cache)
    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    
    def dispatch(self, request, *args, **kwargs):
        return super(HomeView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        user = request.user
        properties = Property.objects.filter(user=user, is_active=True, is_deleted=False)
        users = User.objects.all()
        customers = Customer.objects.filter(dalali=user, is_active=True, is_deleted=False)
        # requests = UserRequest.objects.filter(dalali=user, is_active=True, is_deleted=False)
    
        context = {
            'properties': properties,
            'users':users,
            'customers':customers,
            # 'requests': requests
        }

        return render(request, 'home/home.html', context)


class PropertyIndexView(MainView):
    
    def get(self, request, *args, **kwargs):

        title = "PROPERTY DASHBOARD"

        properties = Property.objects.filter(user = self.request.user, is_active=True, is_deleted=False).order_by('-id')
        contracts = Contract.objects.filter(content_type=ContentType.objects.get_for_model(Property), object_id=3)
        print("====get")
        print(contracts)
        context = {
            'title': title,
            'properties': properties,
            'contracts': contracts
        }
        return render(request, 'property/index.html',context)


class CreateNewPropertyView(MainView):
    
    def get(self, request, *args, **kwargs):
        form = PropertyForm()

        context = {
            'form': form
        }
        return render(request,'property/create.html', context)

class LogoutView(MainView):
    def get(self, request):
        # Do some stuff
        logout(request)
        # Redirect to some page
        return redirect('user_login')


class DashboardView(MainView):
    def get(self, request, *args, **kwargs):
        title = "Dashboard"
        properties = Property.objects.filter(is_active=True, is_deleted = False)
        users = User.objects.all()
        few_users = users.order_by('last_login')[:10]
        customers = Customer.objects.all()
        print(UserManager().show_all_users())
        context = {
            'title': title,
            'properties': properties,
            'get_few': properties.all().order_by('-created')[:5],
            'users': users,
            'few_users': few_users,
            'customers': customers,
            'total_users': len(User.objects.all()) + len(customers),
            'app_users': migrate_data()
        }
        return render(request, 'web/dashboard.html', context)

class PropertyView(MainView):
    def get(self, request, *args, **kwargs):
        title = "Properties"

        context = {
            'title': title,
            'properties': Property.objects.all().order_by('-created')
        }

        return render(request, 'web/properties.html', context)

class ViewProperty(MainView):
    def get(self, request, *args, **kwargs):
        property_id = Property.objects.get(id = kwargs.get('property_id'))
        print(property_id)
         
        context = {

        }

        return render(request, 'property/view_property.html', context)


class SystemUsers(MainView):
    def get(self, request, *args, **kwargs):
        title = "SYSTEM USERS"
        system_users = UserManager().get_system_users()
        roles = SystemRole.objects.filter(is_active=True, is_deleted=False)
        context = {
            'users': system_users,
            'title': title,
            'roles': roles
        }
        return render(request, 'users/all_users.html', context)


class BlockUser(MainView):
    def get(self, request, *args, **kwargs):

        user_id = kwargs.pop('user', None)
        user = User.objects.get(id=16)
        if user is not None:
            user.is_active = False
            user.save()
            
            context = {
                'Status': True,
                'Message': "Blocked Successfully"
            }

            return HttpResponse(json.dumps(context))

        context = {
            'Status': False,
            'Message': "Blocked Failure"
        }

        return HttpResponse(json.dumps(context))



