from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
import datetime as dt
from .models import Project,NewsLetterRecipients,Profile
from .forms import NewProjectForm,NewsLetterForm,NewsProfileForm
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .email import send_welcome_email
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import AwardSerializer,UserSerializer
from rest_framework import status
from .permissions import IsAdminOrReadOnly
from django.contrib.auth.decorators import login_required
from .forms import NewProjectForm, NewsLetterForm, NewsProfileForm 
from django.contrib.auth.models import User

@login_required(login_url='/accounts/login/')
def index(request):
    user =request.user
    post = Project.objects.all()
    profile = Profile.objects.all()
    users = Profile.objects.all()
    views = Profile.objects.all()
    return render(request, 'index.html', {"post":post,"profile":profile, "users":users,})





@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewsProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
        
            profile.username = current_user
            profile.user_id=current_user.id
            profile.save()
        return redirect('user')
    else:
        form = NewsProfileForm()
    return render(request, 'profile.html', {"form":form})

@login_required(login_url='/accounts/login/')
def user(request):
    user = request.user
    profile = Profile.objects.get(username=user)
    projects=Project.objects.filter(id=user.id)
    return render(request, 'project.html',{"profile":profile,"projects":projects})



@login_required(login_url='/accounts/login/')
def new_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.editor = current_user
            project.save()
        return redirect('user')

    else:
        form = NewProjectForm()
    return render(request, 'new-project.html', {"form": form}) 


@login_required(login_url='/accounts/login/')
def comment(request):
    current_user = request.user
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.editor = current_user
            comment.save()
        return redirect('user')

    else:
        form = CommentForm()
    return render(request, 'comment.html', {"form": form}) 


class ProjectList(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get(self, request, format=None):
        all_project = Project.objects.all()
        serializers = AwardSerializer(all_project, many=True)
        return Response(serializers.data)
    def post(self, request, format=None):
        serializers = AwardSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_project(self, pk):
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        project = self.get_project(pk)
        serializers = AwardSerializer(project)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        project = self.get_project(pk)
        serializers = AwardSerializer(project, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        project = self.get_project(pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserList(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get(self, request, format=None):
        all_user = Profile.objects.all()
        serializers = UserSerializer(all_user, many=True)
        return Response(serializers.data)
    def post(self, request, format=None):
        serializers = UserSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        
class UserDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_user(self, pk):
        try:
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        user = self.get_user(pk)
        serializers = UserSerializer(merch)
        return Response(serializers.data)
    def put(self, request, pk, format=None):
        user = self.get_user(pk)
        serializers = UserSerializer(merch, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        user = self.get_user(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@login_required(login_url='/accounts/login/')
def newsletter(request):
    name = request.POST.get('your_name')
    email = request.POST.get('email')

    recipient = NewsLetterRecipients(name=name, email=email)
    recipient.save()
    send_welcome_email(name, email)
    data = {'success': 'You have been successfully added to mailing list'}
    return JsonResponse(data)



def search_results(request):

    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_articles = Article.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})






