from django.http import HttpResponse
from .models import Question
from django.template import loader


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        "latest_question_list": latest_question_list
    }
    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)
