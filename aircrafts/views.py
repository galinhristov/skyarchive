from django.shortcuts import render, get_object_or_404, redirect
from aircrafts.forms import AircraftCreateForm, AircraftEditForm, AircraftDeleteForm
from aircrafts.models import Aircraft
from catalog.models import Role, Country


def aircraft_list(request):
    aircraft = Aircraft.objects.all()
    context = {
        'aircraft': aircraft,
    }
    return render(request, 'aircrafts/aircraft-list.html', context)


def aircraft_details(request, pk):
    aircraft = get_object_or_404(Aircraft, pk=pk)
    context = {
        'aircraft': aircraft,
    }
    return render(request, 'aircrafts/aircraft-details.html', context)


def aircraft_create(request):
    form = AircraftCreateForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('aircraft_list')


    context = {
        'form': form,
    }
    return render(request, 'aircrafts/aircraft-create.html', context)


def aircraft_edit(request, pk):
    aircraft = get_object_or_404(Aircraft, pk=pk)
    form = AircraftEditForm(request.POST or None, instance=aircraft)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('aircraft_details', pk=aircraft.pk)

    context = {
        'aircraft': aircraft,
        'form': form,
    }
    return render(request, 'aircrafts/aircraft-edit.html', context)


def aircraft_delete(request, pk):
    aircraft = get_object_or_404(Aircraft, pk=pk)
    form = AircraftDeleteForm(request.POST or None, instance=aircraft)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('aircraft_list')

    context = {
        'aircraft': aircraft,
        'form': form,
    }
    return render(request, 'aircrafts/aircraft-delete.html', context)


def aircraft_filter(request):
    aircraft = Aircraft.objects.all().select_related("role").prefetch_related(
        "manufacturers",
        "origin_countries",
        "features",
    )

    role_id = request.GET.get("role")
    country_id = request.GET.get("country")
    service_status = request.GET.get("status")
    sort_by = request.GET.get("sort")

    selected_role = int(role_id) if role_id else None
    selected_country = int(country_id) if country_id else None

    if selected_role:
        aircraft = aircraft.filter(role_id=selected_role)

    if selected_country:
        aircraft = aircraft.filter(origin_countries__id=selected_country)

    if service_status == "active":
        aircraft = aircraft.filter(is_active_service=True)
    elif service_status == "retired":
        aircraft = aircraft.filter(is_active_service=False)

    if sort_by == "name":
        aircraft = aircraft.order_by("name")
    elif sort_by == "year":
        aircraft = aircraft.order_by("first_flight_year")
    elif sort_by == "speed":
        aircraft = aircraft.order_by("-max_speed_kmh")

    context = {
        "aircraft": aircraft.distinct(),
        "roles": Role.objects.all(),
        "countries": Country.objects.all(),
        "selected_role": selected_role,
        "selected_country": selected_country,
        "selected_status": service_status,
        "selected_sort": sort_by,
    }

    return render(request, "aircrafts/aircraft-filter.html", context)



