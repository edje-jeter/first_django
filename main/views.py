from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from main.models import State, City, StateCapital

from main.forms import ContactForm
from main.forms import CityEditForm, CityCreateForm
from main.forms import UserSignUp, UserLogin


def state_list(request):

    context = {}

    states = State.objects.all()

    context['states'] = states

    # template name, context dictionary, context_instance variable
    return render_to_response('state_list.html', context,
                              context_instance=RequestContext(request))


def state_detail(request, pk):
    context = {}

    state = State.objects.get(pk=pk)

    context['state'] = state

    return render_to_response('state_detail.html', context,
                              context_instance=RequestContext(request))


def state_search(request):

    context = {}

    context['request'] = request

    state = request.GET.get('state', None)
    # state = request.POST.get('state', None)

    if state is not None:
        states = State.objects.filter(name__icontains=state)
    else:
        states = State.objects.all()

    context['states'] = states

    return render_to_response('state_search.html', context,
                              context_instance=RequestContext(request))


def city_search(request):

    context = {}

    context['request'] = request

    city = request.GET.get('city', None)

    context['search_term'] = city

    if city is not None:
        cities = City.objects.filter(name__icontains=city)
    else:
        cities = City.objects.all()

    context['cities'] = cities

    return render_to_response('city_search.html', context,
                              context_instance=RequestContext(request))


def city_detail(request, pk):
    context = {}

    city = City.objects.get(pk=pk)

    context['city'] = city

    return render_to_response('city_detail.html', context,
                              context_instance=RequestContext(request))


@login_required(login_url='/signup/')
def city_create(request):

    context = {}

    form_city_create = CityCreateForm()

    context['form_city_create_v'] = form_city_create

    if request.method == 'POST':
        form_city_create2 = CityCreateForm(request.POST)
        if form_city_create2.is_valid():
            form_city_create2.save()
            return HttpResponseRedirect('/state_list/')
        else:
            context['errors'] = form_city_create2.errors

    return render_to_response('city_create.html', context,
                              context_instance=RequestContext(request))

# How we did it before we knew about Forms.py
# def city_create(request):

    # context = {}

    # context['request'] = request.method

    # context['states'] = State.objects.all

    # if request.method == 'POST':
    #     name = request.POST.get('name', None)
    #     county = request.POST.get('county', None)
    #     zip_code = request.POST.get('zip_code', None)
    #     latitude = request.POST.get('latitude', None)
    #     longitude = request.POST.get('longitude', None)
    #     state_id = request.POST.get('state', None)

    #     if state_id is not None:
    #         state = State.objects.get(pk=state_id)
    #     else:
    #         state = State.objects.get(name='Texas')

    #     the_city, created = City.objects.get_or_create(name=name)

    #     the_city.county = county
    #     the_city.zip_code = zip_code
    #     the_city.latitude = latitude
    #     the_city.longitude = longitude
    #     the_city.state = state

    #     the_city.save()

    #     context['created'] = 'Operation Successful'
    # elif request.method == 'GET':
    #     print "It was a GET request."

    # return render_to_response('city_create.html', context,
    #                           context_instance=RequestContext(request))


@login_required(login_url='/signup/')
def city_edit(request, pk):

    context = {}

    city = City.objects.get(pk=pk)

    form = CityEditForm(request.POST or None, instance=city)

    context['city'] = city
    context['form_city_edit_v'] = form

    if form.is_valid():
        form.save()
        return redirect('/state_list/')

    return render_to_response('city_edit.html', context,
                              context_instance=RequestContext(request))


@login_required(login_url='/signup/')
def city_delete_func(request, pk):

    City.objects.get(pk=pk).delete()

    return HttpResponseRedirect('/state_list/')


@login_required(login_url='/signup/')
def city_delete_page(request, pk):

    context = {}

    context['city_del'] = City.objects.get(pk=pk)

    return render_to_response('city_delete_page.html', context,
                              context_instance=RequestContext(request))


def statecapital_detail(request, pk):

    context = {}

    statecapital = StateCapital.objects.get(pk=pk)

    context['statecapital'] = statecapital

    return render_to_response('statecapital_detail.html', context,
                              context_instance=RequestContext(request))


def statecapital_list(request):

    context = {}

    statecapitals_v = StateCapital.objects.all()

    context['statecapitals_c'] = statecapitals_v

    return render_to_response('statecapital_list.html', context,
                              context_instance=RequestContext(request))


def contact_view(request):

    context = {}

    form = ContactForm()

    context['form'] = form

    if request.method == 'POST':
        form = ContactForm(request.POST)
        context['form'] = form
        if form.is_valid():
            name_v = form.cleaned_data['name']
            email_v = form.cleaned_data['email']
            phone_v = form.cleaned_data['phone']
            message_v = form.cleaned_data['message']
            # message_v = "Message from: %s\n Phone: %s\n Email: %s\n Message: %s\n" % name_v, phone_v, email_v, form.cleaned_data['message']

            send_mail('STATES SITE MESSAGE FROM %s' % name_v,
                      message_v,
                      email_v,
                      [settings.EMAIL_HOST_USER],
                      fail_silently=False
                      )
            context['message_success'] = "email sent"
        else:
            context['message_success'] = form.errors
    elif request.method == 'GET':
        form = ContactForm()
        context['form'] = form

    return render_to_response('contact_view.html', context,
                              context_instance=RequestContext(request))


def signup(request):

    # Create New User ----------------------------------------

    context = {}

    form = UserSignUp()

    context['form_signup'] = form

    if request.method == 'POST':
        form = UserSignUp(request.POST)
        if form.is_valid():
            print form.cleaned_data

            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            user_name = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            try:
                new_user = User.objects.create_user(user_name,
                                                    email,
                                                    password
                                                    )
                new_user.first_name = first_name
                new_user.last_name = last_name
                context['valid'] = "Thank You For Signing Up!"
                new_user.save()

                auth_user = authenticate(username=user_name,
                                         password=password,
                                         )
                login(request, auth_user)

                return HttpResponseRedirect('/state_list/')

            except IntegrityError, e:
                context['valid'] = "A User With That Name Already Exists"

        else:
            context['valid'] = form.errors

    if request.method == 'GET':
        context['valid'] = "Please Sign Up!"

    # Login existing user ----------------------------------------

    context['form_login'] = UserLogin()

    username = request.POST.get('username', None)
    password = request.POST.get('password', None)

    if username is not None or password is not None:

        auth_user = authenticate(username=username, password=password)

        context['auth_user'] = auth_user

        if auth_user is not None and auth_user.is_active:
            login(request, auth_user)
            return render_to_response('login_success.html', context,
                                      context_instance=RequestContext(request))
        else:
            context['login_fail'] = "Log in failed. Please try again."
            # return render_to_response('login_fail.html', context,
            #                           context_instance=RequestContext(request))

    return render_to_response('signup.html', context,
                              context_instance=RequestContext(request))


# I originally had separate login and signup pages
# def login_view(request):

#     # Login function ----------------------------------------

#     context = {}

#     context['form_login'] = UserLogin()

#     username = request.POST.get('username', None)
#     password = request.POST.get('password', None)

#     auth_user = authenticate(username=username, password=password)

#     if auth_user is not None:
#         if auth_user.is_active:
#             login(request, auth_user)
#             context['valid'] = "Login Successful"

#             return HttpResponseRedirect('/state_list/')
#         else:
#             context['valid'] = "Invalid User"
#     else:
#         context['valid'] = "Please enter a User Name"

#     return render_to_response('signup.html', context,
#                               context_instance=RequestContext(request))


def logout_view(request):

    logout(request)

    return HttpResponseRedirect('/signup/')
