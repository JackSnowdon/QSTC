from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import Round, RoundTube, Shader, Mag
from .forms import (
    EditRoundForm,
    EditRoundTubeForm,
    EditShaderForm,
    EditMagForm,
    RoundForm,
    RoundTubeForm,
    ShaderForm,
    MagForm,
)


# Create your views here.


def shop(request):
    rounds = Round.objects.order_by('name')
    shaders = Shader.objects.order_by('name')
    mags = Mag.objects.order_by('name')
    tubes = RoundTube.objects.order_by('name')
    return render(request, "shop.html", {"round": rounds, "shaders": shaders, "mags": mags, "tubes": tubes})


def add_round(request):
    if request.method == "POST":
        round_form = RoundForm(request.POST)
        if round_form.is_valid():
            rounds = round_form.save(commit=False)
            size = request.POST["size"]
            liner = request.POST["liner"]
            title = size + liner
            rounds.name = title
            rounds.ton = "Needles"
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
    return render(request, "edit_round.html", {"round_form": round_form, "item": item})


def delete_round(request, pk=id):
    instance = Round.objects.get(pk=pk)
    instance.delete()
    return redirect(reverse("shop"))


def add_shader(request):
    if request.method == "POST":
        shader_form = ShaderForm(request.POST)
        if shader_form.is_valid():
            shader = shader_form.save(commit=False)
            size = request.POST["size"]
            shader.liner = "RS"
            title = size + shader.liner
            shader.name = title
            shader.ton = "Needles"
            shader.save()
            # messages.error(request, 'Added {0}'.format(player.name), extra_tags='alert boldest')
            return redirect("shop")
    else:
        shader_form = ShaderForm()
    return render(request, "add_shader.html", {"shader_form": shader_form})


def edit_shader(request, id):
    item = get_object_or_404(Shader, pk=id)
    if request.method == "POST":
        shader_form = EditShaderForm(request.POST, instance=item)
        if shader_form.is_valid():
            shader_form.save()
            return redirect("shop")
    else:
        shader_form = EditShaderForm(instance=item)
    return render(request, "edit_shader.html", {"shader_form": shader_form, "item": item})


def delete_shader(request, pk=id):
    instance = Shader.objects.get(pk=pk)
    instance.delete()
    return redirect(reverse("shop"))


def add_mag(request):
    if request.method == "POST":
        mag_form = MagForm(request.POST)
        if mag_form.is_valid():
            mag = mag_form.save(commit=False)
            size = request.POST["size"]
            mag.liner = "M"
            title = size + mag.liner
            mag.name = title
            mag.ton = "Needles"
            mag.save()
            # messages.error(request, 'Added {0}'.format(player.name), extra_tags='alert boldest')
            return redirect("shop")
    else:
        mag_form = MagForm()
    return render(request, "add_mag.html", {"mag_form": mag_form})


def edit_mag(request, id):
    item = get_object_or_404(Mag, pk=id)
    if request.method == "POST":
        mag_form = EditMagForm(request.POST, instance=item)
        if mag_form.is_valid():
            mag_form.save()
            return redirect("shop")
    else:
        mag_form = EditMagForm(instance=item)
    return render(request, "edit_mag.html", {"mag_form": mag_form, "item": item})


def delete_mag(request, pk=id):
    instance = Shader.objects.get(pk=pk)
    instance.delete()
    return redirect(reverse("shop"))


def add_round_tube(request):
    if request.method == "POST":
        round_form = RoundTubeForm(request.POST)
        if round_form.is_valid():
            rounds = round_form.save(commit=False)
            size = request.POST["size"]
            rounds.liner = "RT"
            title = size + rounds.liner
            rounds.name = title
            rounds.ton = "Tubes"
            rounds.save()
            # messages.error(request, 'Added {0}'.format(player.name), extra_tags='alert boldest')
            return redirect("shop")
    else:
        round_form = RoundTubeForm()
    return render(request, "add_round_tube.html", {"round_form": round_form})


def edit_round_tube(request, id):
    item = get_object_or_404(RoundTube, pk=id)
    if request.method == "POST":
        round_form = EditRoundTubeForm(request.POST, instance=item)
        if round_form.is_valid():
            round_form.save()
            return redirect("shop")
    else:
        round_form = EditRoundTubeForm(instance=item)
    return render(request, "edit_round_tube.html", {"round_form": round_form, "item": item})


def delete_round_tube(request, pk=id):
    instance = RoundTube.objects.get(pk=pk)
    instance.delete()
    return redirect(reverse("shop"))
