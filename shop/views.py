from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import Round
from .forms import EditRoundForm, RoundForm


# Create your views here.


def shop(request):
    rounds = Round.objects.all()
    return render(request, "shop.html", {"round": rounds})


def add_round(request):
    if request.method == "POST":
        round_form = RoundForm(request.POST)
        if round_form.is_valid():
            rounds = round_form.save(commit=False)
            size = request.POST["size"]
            liner = request.POST["liner"]
            title = size + liner
            rounds.name = title
            rounds.save()
            # messages.error(request, 'Added {0}'.format(player.name), extra_tags='alert boldest')
            return redirect("shop")
    else:
        round_form = RoundForm()
    return render(request, "add_round.html", {"round_form": round_form})


def edit_round(request, id):
    item = get_object_or_404(Round, pk=id)
    if request.method == "POST":
        round_form = EditRoundForm(request.POST, instance=item)
        if round_form.is_valid():
            round_form.save()
            return redirect("shop")
    else:
        round_form = EditRoundForm(instance=item)
    return render(request, "edit_round.html", {"round_form": round_form})

def delete_round(request, pk=id):
    instance = Round.objects.get(pk=pk)
    instance.delete()
    return redirect(reverse('shop'))