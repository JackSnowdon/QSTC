from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import Flat, Round, RoundTube, Shader, Mag, Vtip
from .forms import (
    EditFlatForm,
    EditRoundForm,
    EditRoundTubeForm,
    EditShaderForm,
    EditMagForm,
    EditVtipForm,
    FlatForm,
    RoundForm,
    RoundTubeForm,
    ShaderForm,
    MagForm,
    VtipForm,
)


# Create your views here.


def shop(request):
    rounds = Round.objects.order_by('name')
    shaders = Shader.objects.order_by('name')
    mags = Mag.objects.order_by('name')
    tubes = RoundTube.objects.order_by('name')
    vtips = Vtip.objects.order_by('name')
    flats = Flat.objects.order_by('name')
    return render(request, "shop.html", {"rounds": rounds, "shaders": shaders, "mags": mags, "tubes": tubes, "vtips": vtips, "flats":flats})


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
            messages.error(request, 'Added {0} to Rounds'.format(title), extra_tags='alert')
            return redirect("shop")
    else:
        round_form = RoundForm()
    return render(request, "add_round.html", {"round_form": round_form})  


def edit_round(request, id):
    item = get_object_or_404(Round, pk=id)
    if request.method == "POST":
        round_form = EditRoundForm(request.POST, instance=item)
        if round_form.is_valid():
            title = get_edit_name(item)
            round_form.save()
            messages.error(request, 'Edited {0}'.format(title), extra_tags='alert')
            return redirect("shop")
    else:
        round_form = EditRoundForm(instance=item)
    return render(request, "edit_round.html", {"round_form": round_form, "item": item})


def delete_round(request, pk=id):
    instance = Round.objects.get(pk=pk)
    title = get_edit_name(instance)
    messages.error(request, 'Deleted {0}'.format(title), extra_tags='alert')
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
            messages.error(request, 'Added {0} to Shaders'.format(title), extra_tags='alert')
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
            title = get_edit_name(item)
            messages.error(request, 'Edited {0}'.format(title), extra_tags='alert')
            return redirect("shop")
    else:
        shader_form = EditShaderForm(instance=item)
    return render(request, "edit_shader.html", {"shader_form": shader_form, "item": item})


def delete_shader(request, pk=id):
    instance = Shader.objects.get(pk=pk)
    title = get_edit_name(instance)
    messages.error(request, 'Deleted {0}'.format(title), extra_tags='alert')
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
            messages.error(request, 'Added {0} to Mags'.format(title), extra_tags='alert')
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
            title = get_edit_name(item)
            messages.error(request, 'Edited {0}'.format(title), extra_tags='alert')
            return redirect("shop")
    else:
        mag_form = EditMagForm(instance=item)
    return render(request, "edit_mag.html", {"mag_form": mag_form, "item": item})


def delete_mag(request, pk=id):
    instance = Mag.objects.get(pk=pk)
    title = get_edit_name(instance)
    messages.error(request, 'Deleted {0}'.format(title), extra_tags='alert')
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
            messages.error(request, 'Added {0} to Tubes'.format(title), extra_tags='alert')
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
            title = get_edit_name(item)
            messages.error(request, 'Edited {0}'.format(title), extra_tags='alert')
            return redirect("shop")
    else:
        round_form = EditRoundTubeForm(instance=item)
    return render(request, "edit_round_tube.html", {"round_form": round_form, "item": item})


def delete_round_tube(request, pk=id):
    instance = RoundTube.objects.get(pk=pk)
    title = get_edit_name(instance)
    messages.error(request, 'Deleted {0}'.format(title), extra_tags='alert')
    instance.delete()
    return redirect(reverse("shop"))

def add_vtip(request):
    if request.method == "POST":
        vtip_form = VtipForm(request.POST)
        if vtip_form.is_valid():
            vtip = vtip_form.save(commit=False)
            size = request.POST["size"]
            vtip.liner = "VT"
            title = size + vtip.liner
            vtip.name = title
            vtip.ton = "Tubes"
            vtip.save()
            messages.error(request, 'Added {0} to VTips'.format(title), extra_tags='alert')
            return redirect("shop")
    else:
        vtip_form = VtipForm()
    return render(request, "add_vtip.html", {"vtip_form": vtip_form})


def edit_vtip(request, id):
    item = get_object_or_404(Vtip, pk=id)
    if request.method == "POST":
        vtip_form = EditVtipForm(request.POST, instance=item)
        if vtip_form.is_valid():
            vtip_form.save()
            title = get_edit_name(item)
            messages.error(request, 'Edited {0}'.format(title), extra_tags='alert')
            return redirect("shop")
    else:
        vtip_form = EditVtipForm(instance=item)
    return render(request, "edit_vtip.html", {"vtip_form": vtip_form, "item": item})


def delete_vtip(request, pk=id):
    instance = Vtip.objects.get(pk=pk)
    title = get_edit_name(instance)
    messages.error(request, 'Deleted {0}'.format(title), extra_tags='alert')
    instance.delete()
    return redirect(reverse("shop"))


def add_flat(request):
    if request.method == "POST":
        flat_form = FlatForm(request.POST)
        if flat_form.is_valid():
            flat = flat_form.save(commit=False)
            size = request.POST["size"]
            flat.liner = "F"
            title = size + flat.liner
            flat.name = title
            flat.ton = "Tubes"
            flat.save()
            messages.error(request, 'Added {0} to Flats'.format(title), extra_tags='alert')
            return redirect("shop")
    else:
        flat_form = FlatForm()
    return render(request, "add_flat.html", {"flat_form": flat_form})


def edit_flat(request, id):
    item = get_object_or_404(Flat, pk=id)
    if request.method == "POST":
        flat_form = EditFlatForm(request.POST, instance=item)
        if flat_form.is_valid():
            flat_form.save()
            title = get_edit_name(item)
            messages.error(request, 'Edited {0}'.format(title), extra_tags='alert')
            return redirect("shop")
    else:
        flat_form = EditFlatForm(instance=item)
    return render(request, "edit_flat.html", {"flat_form": flat_form, "item": item})


def delete_flat(request, pk=id):
    instance = Flat.objects.get(pk=pk)
    title = get_edit_name(instance)
    messages.error(request, 'Deleted {0}'.format(title), extra_tags='alert')
    instance.delete()
    return redirect(reverse("shop"))



"""
Helper Functions
"""

def get_edit_name(x):
    size = str(x.size)
    liner = x.liner
    title = size + liner
    return title  