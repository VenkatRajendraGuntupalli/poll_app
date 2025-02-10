from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import UserPoll
from .forms import UserPollForm

def homepage(request):
    polls = UserPoll.objects.all()
    return render(request, 'polls/home_dark.html', {'polls': polls})

def create_poll(request):
    if request.method == 'POST':
        form = UserPollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = UserPollForm()
    return render(request, 'polls/create_dark.html', {'form': form})

def vote_poll(request, poll_id):
    poll = UserPoll.objects.get(pk=poll_id)
    if request.method == 'POST':
        selected_choice = request.POST['poll']
        if selected_choice == 'choice_x':
            poll.votes_choice_x += 1
        elif selected_choice == 'choice_y':
            poll.votes_choice_y += 1
        elif selected_choice == 'choice_z':
            poll.votes_choice_z += 1
        else:
            return HttpResponse(400, 'Invalid selection')
        poll.save()
        return redirect('poll_results', poll.id)
    return render(request, 'polls/vote_dark.html', {'poll': poll})

def poll_results(request, poll_id):
    poll = UserPoll.objects.get(pk=poll_id)
    return render(request, 'polls/results_dark.html', {'poll': poll})
