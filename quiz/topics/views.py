from django.shortcuts import render, HttpResponseRedirect
from .models import LoginUsers, QuizTopic
from django.views.decorators.csrf import csrf_exempt


def login(request):
    return render(request, 'login.html')


@csrf_exempt
def home(request):
    if request.POST:
        email = request.POST.get('email')
        password = request.POST.get('pass')
        try:
            user_profile = LoginUsers.objects.get(email=email, password=password)
        except Exception as e:
            return HttpResponseRedirect("/")
        quiz_topics = QuizTopic.objects.all()
        return render(request, 'home.html', {'first_name': user_profile.first_name,
                                             'last_name': user_profile.last_name,
                                             'quiz_topics': quiz_topics})
