from django.shortcuts import render, get_object_or_404, redirect

from catalog.forms import RoleCreateForm, RoleEditForm, RoleDeleteForm
from catalog.models import Role


def role_list(request):
    roles = Role.objects.all()

    context = {
        'roles': roles,
    }
    return render(request, 'catalog/role-list.html', context)


def role_details(request, pk):
    role = get_object_or_404(Role, pk=pk)

    context = {
        'role': role,
    }
    return render(request, 'catalog/role-details.html', context)


def role_create(request):
    form = RoleCreateForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('role_list')

    context = {
        'form': form,
    }
    return render(request, 'catalog/role-create.html', context)



def role_edit(request, pk):
    role = get_object_or_404(Role, pk=pk)
    form = RoleEditForm(request.POST or None, instance=role)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('role_details', pk=role.pk)

    context = {
        'role': role,
        'form': form,
    }
    return render(request, 'catalog/role-edit.html', context)

def role_delete(request, pk):
    role = get_object_or_404(Role, pk=pk)
    form = RoleDeleteForm(request.POST or None, instance=role)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('role_list')

    context = {
        'role': role,
        'form': form,
    }
    return render(request, 'catalog/role-delete.html', context)

