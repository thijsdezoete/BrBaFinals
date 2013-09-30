from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from models import People, Result, Contestant
from forms import ContestantForm, TestQuestion
from django.db.models import Q


def questionnaire(request, contestant):
    characters = People.objects.filter(~Q(name='Nobody'))
    cont = Contestant.objects.get(name=contestant)

    if request.method == 'POST':
        for person in characters:
            x = TestQuestion(request.POST, prefix=person)

            if x.is_valid():
                test = Result()
                test.name = cont
                test.character = person
                test.killed_by = x.cleaned_data['killed_by']
                test.is_survivor = x.cleaned_data['is_survivor']
                test.save()
                print person

        return HttpResponseRedirect('/done')
    else:
        forms = {}
        for person in characters:
            x = TestQuestion(initial={'character':person, 'name':cont}, prefix=person)
            forms[person] = x


    return render_to_response('brbappl/questions.html', 
        {'forms': forms}, 
        context_instance=RequestContext(request)
    )


def participate(request):
    if request.method == 'POST':
        formset = ContestantForm(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect('/' + formset.data['name'])
    else:
        formset = ContestantForm()
    
    return render_to_response("brbappl/index.html", {
        "form": formset,
    },  context_instance=RequestContext(request))


def index(request):
    context = {
        "form": ContestantForm,
    }

    return render_to_response('brbappl/index.html', 
        context, 
        context_instance=RequestContext(request))


def done(request):
    return render_to_response('brbappl/done.html', {}, context_instance=RequestContext(request))
