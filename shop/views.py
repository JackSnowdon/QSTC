from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Flat, Round, RoundTube, Shader, StockReport, StockObject, Mag, Vtip
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
    StockForm,
    StockObjectForm,
    ShaderForm,
    MagForm,
    VtipForm,
)
from home.views import index
import datetime


# Create your views here.


@login_required
def shop(request):
    if request.user.profile.staff_access:
        rounds = Round.objects.order_by("name")
        shaders = Shader.objects.order_by("name")
        mags = Mag.objects.order_by("name")
        tubes = RoundTube.objects.order_by("name")
        vtips = Vtip.objects.order_by("name")
        flats = Flat.objects.order_by("name")
        return render(
            request,
            "shop.html",
            {
                "rounds": rounds,
                "shaders": shaders,
                "mags": mags,
                "tubes": tubes,
                "vtips": vtips,
                "flats": flats,
            },
        )
    else:
        messages.error(
            request, "You Don't Have The Required Permissions", extra_tags="alert"
        )
        return redirect("index")


# Rounds

@login_required
def add_round(request):
    if request.user.profile.staff_access:
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
                messages.error(
                    request, "Added {0} to Rounds".format(title), extra_tags="alert"
                )
                return redirect("shop")
        else:
            round_form = RoundForm()
        return render(request, "add_round.html", {"round_form": round_form})
    else:
        messages.error(
            request, "You Don't Have The Required Permissions", extra_tags="alert"
        )
        return redirect("index")


@login_required
def edit_round(request, id):
    if request.user.profile.staff_access:
        item = get_object_or_404(Round, pk=id)
        if request.method == "POST":
            round_form = EditRoundForm(request.POST, instance=item)
            if round_form.is_valid():
                title = get_edit_name(item)
                round_form.save()
                messages.error(request, "Edited {0}".format(title), extra_tags="alert")
                return redirect("shop")
        else:
            round_form = EditRoundForm(instance=item)
        return render(request, "edit_round.html", {"round_form": round_form, "item": item})
    else:
        messages.error(
            request, "You Don't Have The Required Permissions", extra_tags="alert"
        )
        return redirect("index")


@login_required
def plus_round(request, id):
    if request.user.profile.staff_access:
        item = get_object_or_404(Round, pk=id)
        plus_needle_stock(item)
        messages.error(request, "Added 50 {0}".format(item), extra_tags="alert")
        return redirect(reverse("shop"))
    else:
        messages.error(
            request, "You Don't Have The Required Permissions", extra_tags="alert"
        )
        return redirect("index")


@login_required
def minus_round(request, id):
    if request.user.profile.staff_access:
        item = get_object_or_404(Round, pk=id)
        minus_needle_stock(item)
        messages.error(request, "Minus 50 {0}".format(item), extra_tags="alert")
        return redirect(reverse("shop"))
    else:
        messages.error(
            request, "You Don't Have The Required Permissions", extra_tags="alert"
        )
        return redirect("index")


@login_required
def delete_round(request, pk=id):
    if request.user.profile.staff_access:
        instance = Round.objects.get(pk=pk)
        title = get_edit_name(instance)
        messages.error(request, "Deleted {0}".format(title), extra_tags="alert")
        instance.delete()
        return redirect(reverse("shop"))
    else:
        messages.error(
            request, "You Don't Have The Required Permissions", extra_tags="alert"
        )
        return redirect("index")


# Shaders


@login_required
def add_shader(request):
    if request.user.profile.staff_access:
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
                messages.error(
                    request, "Added {0} to Shaders".format(title), extra_tags="alert"
                )
                return redirect("shop")
        else:
            shader_form = ShaderForm()
        return render(request, "add_shader.html", {"shader_form": shader_form})
    else:
        messages.error(
            request, "You Don't Have The Required Permissions", extra_tags="alert"
        )
        return redirect("index")


@login_required
def edit_shader(request, id):
    if request.user.profile.staff_access:
        item = get_object_or_404(Shader, pk=id)
        if request.method == "POST":
            shader_form = EditShaderForm(request.POST, instance=item)
            if shader_form.is_valid():
                shader_form.save()
                title = get_edit_name(item)
                messages.error(request, "Edited {0}".format(title), extra_tags="alert")
                return redirect("shop")
        else:
            shader_form = EditShaderForm(instance=item)
        return render(
            request, "edit_shader.html", {"shader_form": shader_form, "item": item}
        )
    else:
        messages.error(
            request, "You Don't Have The Required Permissions", extra_tags="alert"
        )
        return redirect("index")


@login_required
def plus_shader(request, id):
    if request.user.profile.staff_access:
        item = get_object_or_404(Shader, pk=id)
        plus_needle_stock(item)
        messages.error(request, "Added 50 {0}".format(item), extra_tags="alert")
        return redirect(reverse("shop"))
    else:
        messages.error(
            request, "You Don't Have The Required Permissions", extra_tags="alert"
        )
        return redirect("index")


@login_required
def minus_shader(request, id):
    if request.user.profile.staff_access:
        item = get_object_or_404(Shader, pk=id)
        minus_needle_stock(item)
        messages.error(request, "minus 50 {0}".format(item), extra_tags="alert")
        return redirect(reverse("shop"))
    else:
        messages.error(
            request, "You Don't Have The Required Permissions", extra_tags="alert"
        )
        return redirect("index")


@login_required
def delete_shader(request, pk=id):
    if request.user.profile.staff_access:
        instance = Shader.objects.get(pk=pk)
        title = get_edit_name(instance)
        messages.error(request, "Deleted {0}".format(title), extra_tags="alert")
        instance.delete()
        return redirect(reverse("shop"))
    else:
        messages.error(
            request, "You Don't Have The Required Permissions", extra_tags="alert"
        )
        return redirect("index")


# Mags

@login_required
def add_mag(request):
    if request.user.profile.staff_access:
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
                messages.error(
                    request, "Added {0} to Mags".format(title), extra_tags="alert"
                )
                return redirect("shop")
        else:
            mag_form = MagForm()
        return render(request, "add_mag.html", {"mag_form": mag_form})
    else:
        messages.error(
            request, "You Don't Have The Required Permissions", extra_tags="alert"
        )
        return redirect("index")


@login_required
def edit_mag(request, id):
    if request.user.profile.staff_access:
        item = get_object_or_404(Mag, pk=id)
        if request.method == "POST":
            mag_form = EditMagForm(request.POST, instance=item)
            if mag_form.is_valid():
                mag_form.save()
                title = get_edit_name(item)
                messages.error(request, "Edited {0}".format(title), extra_tags="alert")
                return redirect("shop")
        else:
            mag_form = EditMagForm(instance=item)
        return render(request, "edit_mag.html", {"mag_form": mag_form, "item": item})
    else:
        messages.error(
            request, "You Don't Have The Required Permissions", extra_tags="alert"
        )
        return redirect("index")


@login_required
def plus_mag(request, id):
    if request.user.profile.staff_access:
        item = get_object_or_404(Mag, pk=id)
        plus_needle_stock(item)
        messages.error(request, "Added 50 {0}".format(item), extra_tags="alert")
        return redirect(reverse("shop"))
    else:
        messages.error(
            request, "You Don't Have The Required Permissions", extra_tags="alert"
        )
        return redirect("index")


@login_required
def minus_mag(request, id):
    if request.user.profile.staff_access:
        item = get_object_or_404(Mag, pk=id)
        minus_needle_stock(item)
        messages.error(request, "Minus 50 {0}".format(item), extra_tags="alert")
        return redirect(reverse("shop"))
    else:
        messages.error(
            request, "You Don't Have The Required Permissions", extra_tags="alert"
        )
        return redirect("index")


@login_required
def delete_mag(request, pk=id):
    if request.user.profile.staff_access:
        instance = Mag.objects.get(pk=pk)
        title = get_edit_name(instance)
        messages.error(request, "Deleted {0}".format(title), extra_tags="alert")
        instance.delete()
        return redirect(reverse("shop"))
    else:
        messages.error(
            request, "You Don't Have The Required Permissions", extra_tags="alert"
        )
        return redirect("index")


# Round Tube


@login_required
def add_round_tube(request):
    if request.user.profile.staff_access:
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
                messages.error(
                    request, "Added {0} to Tubes".format(title), extra_tags="alert"
                )
                return redirect("shop")
        else:
            round_form = RoundTubeForm()
        return render(request, "add_round_tube.html", {"round_form": round_form})
    else:
        messages.error(
            request, "You Don't Have The Required Permissions", extra_tags="alert"
        )
        return redirect("index")


@login_required
def edit_round_tube(request, id):
    if request.user.profile.staff_access:
        item = get_object_or_404(RoundTube, pk=id)
        if request.method == "POST":
            round_form = EditRoundTubeForm(request.POST, instance=item)
            if round_form.is_valid():
                round_form.save()
                title = get_edit_name(item)
                messages.error(request, "Edited {0}".format(title), extra_tags="alert")
                return redirect("shop")
        else:
            round_form = EditRoundTubeForm(instance=item)
        return render(
            request, "edit_round_tube.html", {"round_form": round_form, "item": item}
        )
    else:
        messages.error(
            request, "You Don't Have The Required Permissions", extra_tags="alert"
        )
        return redirect("index")


@login_required
def plus_round_tube(request, id):
    if request.user.profile.staff_access:
        item = get_object_or_404(RoundTube, pk=id)
        plus_tube_stock(item)
        messages.error(request, "Added 20 {0}".format(item), extra_tags="alert")
        return redirect(reverse("shop"))
    else:
        messages.error(
            request, "You Don't Have The Required Permissions", extra_tags="alert"
        )
        return redirect("index")


@login_required
def minus_round_tube(request, id):
    if request.user.profile.staff_access:
        item = get_object_or_404(RoundTube, pk=id)
        minus_tube_stock(item)
        messages.error(request, "Minus 20 {0}".format(item), extra_tags="alert")
        return redirect(reverse("shop"))
    else:
        messages.error(
            request, "You Don't Have The Required Permissions", extra_tags="alert"
        )
        return redirect("index")


@login_required
def delete_round_tube(request, pk=id):
    if request.user.profile.staff_access:
        instance = RoundTube.objects.get(pk=pk)
        title = get_edit_name(instance)
        messages.error(request, "Deleted {0}".format(title), extra_tags="alert")
        instance.delete()
        return redirect(reverse("shop"))
    else:
        messages.error(
            request, "You Don't Have The Required Permissions", extra_tags="alert"
        )
        return redirect("index")


# Vtips


@login_required
def add_vtip(request):
    if request.user.profile.staff_access:
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
                messages.error(
                    request, "Added {0} to VTips".format(title), extra_tags="alert"
                )
                return redirect("shop")
        else:
            vtip_form = VtipForm()
        return render(request, "add_vtip.html", {"vtip_form": vtip_form})
    else:
        messages.error(
            request, "You Don't Have The Required Permissions", extra_tags="alert"
        )
        return redirect("index")


@login_required
def edit_vtip(request, id):
    if request.user.profile.staff_access:
        item = get_object_or_404(Vtip, pk=id)
        if request.method == "POST":
            vtip_form = EditVtipForm(request.POST, instance=item)
            if vtip_form.is_valid():
                vtip_form.save()
                title = get_edit_name(item)
                messages.error(request, "Edited {0}".format(title), extra_tags="alert")
                return redirect("shop")
        else:
            vtip_form = EditVtipForm(instance=item)
        return render(request, "edit_vtip.html", {"vtip_form": vtip_form, "item": item})
    else:
        messages.error(
            request, "You Don't Have The Required Permissions", extra_tags="alert"
        )
        return redirect("index")


@login_required
def plus_vtip(request, id):
    if request.user.profile.staff_access:
        item = get_object_or_404(Vtip, pk=id)
        plus_tube_stock(item)
        messages.error(request, "Added 20 {0}".format(item), extra_tags="alert")
        return redirect(reverse("shop"))
    else:
        messages.error(
            request, "You Don't Have The Required Permissions", extra_tags="alert"
        )
        return redirect("index")


@login_required
def minus_vtip(request, id):
    if request.user.profile.staff_access:
        item = get_object_or_404(Vtip, pk=id)
        minus_tube_stock(item)
        messages.error(request, "Minus 20 {0}".format(item), extra_tags="alert")
        return redirect(reverse("shop"))
    else:
        messages.error(
            request, "You Don't Have The Required Permissions", extra_tags="alert"
        )
        return redirect("index")


@login_required
def delete_vtip(request, pk=id):
    if request.user.profile.staff_access:
        instance = Vtip.objects.get(pk=pk)
        title = get_edit_name(instance)
        messages.error(request, "Deleted {0}".format(title), extra_tags="alert")
        instance.delete()
        return redirect(reverse("shop"))
    else:
        messages.error(
            request, "You Don't Have The Required Permissions", extra_tags="alert"
        )
        return redirect("index")


# Flats


@login_required
def add_flat(request):
    if request.user.profile.staff_access:
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
                messages.error(
                    request, "Added {0} to Flats".format(title), extra_tags="alert"
                )
                return redirect("shop")
        else:
            flat_form = FlatForm()
        return render(request, "add_flat.html", {"flat_form": flat_form})
    else:
        messages.error(
            request, "You Don't Have The Required Permissions", extra_tags="alert"
        )
        return redirect("index")


@login_required
def edit_flat(request, id):
    if request.user.profile.staff_access:
        item = get_object_or_404(Flat, pk=id)
        if request.method == "POST":
            flat_form = EditFlatForm(request.POST, instance=item)
            if flat_form.is_valid():
                flat_form.save()
                title = get_edit_name(item)
                messages.error(request, "Edited {0}".format(title), extra_tags="alert")
                return redirect("shop")
        else:
            flat_form = EditFlatForm(instance=item)
        return render(request, "edit_flat.html", {"flat_form": flat_form, "item": item})
    else:
        messages.error(
            request, "You Don't Have The Required Permissions", extra_tags="alert"
        )
        return redirect("index")


@login_required
def plus_flat(request, id):
    if request.user.profile.staff_access:
        item = get_object_or_404(Flat, pk=id)
        plus_tube_stock(item)
        messages.error(request, "Added 20 {0}".format(item), extra_tags="alert")
        return redirect(reverse("shop"))
    else:
        messages.error(
            request, "You Don't Have The Required Permissions", extra_tags="alert"
        )
        return redirect("index")


@login_required
def minus_flat(request, id):
    if request.user.profile.staff_access:
        item = get_object_or_404(Flat, pk=id)
        minus_tube_stock(item)
        messages.error(request, "Minus 20 {0}".format(item), extra_tags="alert")
        return redirect(reverse("shop"))
    else:
        messages.error(
            request, "You Don't Have The Required Permissions", extra_tags="alert"
        )
        return redirect("index")


@login_required
def delete_flat(request, pk=id):
    if request.user.profile.staff_access:
        instance = Flat.objects.get(pk=pk)
        title = get_edit_name(instance)
        messages.error(request, "Deleted {0}".format(title), extra_tags="alert")
        instance.delete()
        return redirect(reverse("shop"))
    else:
        messages.error(
            request, "You Don't Have The Required Permissions", extra_tags="alert"
        )
        return redirect("index")


# Stock


@login_required()
def get_all_stock(request):
    if request.user.profile.staff_access:

        rounds = Round.objects.values("name", "stock").order_by("name")
        shaders = Shader.objects.values("name", "stock").order_by("name")
        mags = Mag.objects.values("name", "stock").order_by("name")
        tubes = RoundTube.objects.values("name", "stock").order_by("name")
        vtips = Vtip.objects.values("name", "stock").order_by("name")
        flats = Flat.objects.values("name", "stock").order_by("name")
        reports = StockReport.objects.order_by("-date")

        return render(
            request,
            "stock.html",
            {
                "rounds": rounds,
                "shaders": shaders,
                "mags": mags,
                "tubes": tubes,
                "vtips": vtips,
                "flats": flats,
                "reports": reports,
            },
        )
    
    else:
        messages.error(
            request, "You Don't Have The Required Permissions", extra_tags="alert"
        )
        return redirect("index")


@login_required()
def save_stock_report(request):
    if request.user.profile.staff_access:
        stock_form = StockForm()
        stock = stock_form.save(commit=False)
        date = datetime.datetime.now()
        stock.date = date
        stock.done_by = request.user.profile
        stock.save()
        report_no = stock.id

        rounds = Round.objects.order_by("name")
        shaders = Shader.objects.order_by("name")
        mags = Mag.objects.order_by("name")
        tubes = RoundTube.objects.order_by("name")
        vtips = Vtip.objects.order_by("name")
        flats = Flat.objects.order_by("name")

        save_stock_items(rounds, report_no)
        save_stock_items(shaders, report_no)
        save_stock_items(mags, report_no)
        save_stock_items(tubes, report_no)
        save_stock_items(vtips, report_no)
        save_stock_items(flats, report_no)

        

        stock.save()

        return redirect("check_report", report_no)
    
    else:
        messages.error(
            request, "You Don't Have The Required Permissions", extra_tags="alert"
        )
        return redirect("index")


@login_required()
def check_report(request, id):
    if request.user.profile.staff_access:
        reports = StockObject.objects.filter(report_number=id)
        this_report = StockReport.objects.get(id=id)
        all_reports = StockReport.objects.order_by("date")

        return render(
            request,
            "single_report.html",
            {"reports": reports, "this_report": this_report, "all_reports": all_reports},
        )
    else:
        messages.error(
            request, "You Don't Have The Required Permissions", extra_tags="alert"
        )
        return redirect("index")


# Helper Functions


def get_edit_name(x):
    size = str(x.size)
    liner = x.liner
    title = size + liner
    return title


def plus_needle_stock(x):
    x.stock += 50
    x.save()


def minus_needle_stock(x):
    x.stock -= 50
    x.save()


def plus_tube_stock(x):
    x.stock += 20
    x.save()


def minus_tube_stock(x):
    x.stock -= 20
    x.save()


def save_stock_items(x, z):
    for y in x:
        stock_item = StockObjectForm()
        sitem = stock_item.save(commit=False)
        name = y.name
        s = y.stock
        sitem.name = name
        sitem.stock = s
        sitem.report_number = StockReport.objects.get(id=z)
        sitem.save()


def unpack_stock(x):
    name = [y.name for y in x]
    stock = [y.stock for y in x]
    full_dict = dict(zip(name, stock))
    return full_dict