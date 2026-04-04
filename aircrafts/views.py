from django.shortcuts import render, get_object_or_404, redirect
from aircrafts.forms import AircraftCreateForm, AircraftEditForm, AircraftDeleteForm
from aircrafts.models import Aircraft


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