from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Round
from .forms import RoundForm
from django.contrib import messages

# Create your views here.

def shop(request):
    return render(request, 'shop.html')


def add_round(request):
    if request.method == "POST":
        round_form = RoundForm(request.POST)
        if round_form.is_valid():
            round = round_form.save(commit=False)
            size = (request.POST['size'])
            liner = (request.POST['liner'])
            title = size + liner
            round.name = title
            round_form.save()
           # messages.error(request, 'Added {0}'.format(player.name), extra_tags='alert boldest')
            return redirect('shop')
    else:
        round_form = RoundForm()
    return render(request, 'add_round.html', {'round_form': round_form})