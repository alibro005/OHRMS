from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Property
from .forms import PropertyForm

@login_required
def property_list(request):
    if request.user.role == 'admin':
        properties = Property.objects.all()
    else:
        properties = Property.objects.filter(owner=request.user)
    return render(request, 'properties/property_list.html', {'properties': properties})


@login_required
def property_create(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST,request.FILES)
        if form.is_valid():
            prop = form.save(commit=False)
            prop.owner = request.user
            prop.save()
            return redirect('property_list')
        else:
            print(form.errors)      # optional: debug errors
            print(request.FILES) 
    else:
        form = PropertyForm()
    return render(request, 'properties/property_form.html', {'form': form})


@login_required
def property_update(request, pk):
    prop = get_object_or_404(Property, pk=pk, owner=request.user)
    form = PropertyForm(request.POST or None, request.FILES or None, instance=prop)
    if form.is_valid():
        form.save()
        return redirect('property_list')
    return render(request, 'properties/property_form.html', {'form': form})


@login_required
def property_delete(request, pk):
    prop = get_object_or_404(Property, pk=pk, owner=request.user)
    if request.method == 'POST':
        prop.delete()
        return redirect('property_list')
    return render(request, 'properties/property_confirm_delete.html', {'property': prop})

