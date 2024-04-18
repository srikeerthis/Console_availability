from django.shortcuts import render,redirect,get_object_or_404
from .models import Console
from .forms import ConsoleForms
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

# Create your views here.
@login_required
def console_list(request):
    if request.method == 'POST':
        for console in Console.objects.all():
            new_status = request.POST.get(f'status_{console.id}')
            if new_status and new_status in dict(Console.STATUS_CHOICES):
                console.status = new_status
                console.save()
        return redirect('console_list')
    
    consoles = Console.objects.all()
    return render(request, 'rental/console_list.html', {'consoles': consoles})

# @login_required
# def toggle_rental_status(request,console_id):
#     console = Console.objects.get(id=console_id)
#     console.is_rented = not console.is_rented
#     console.save()
#     return redirect('console_list')

@login_required
def add_console(request):
    if not request.user.is_staff and not request.user.is_superuser:
        return HttpResponseForbidden()
    
    if request.method == 'POST':
        form = ConsoleForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('console_list')
    else:
        form = ConsoleForms()
        return render(request,'rental/add_console.html',{'form':form})

@login_required
def edit_consoles(request,console_id):
    console = get_object_or_404(Console,id=console_id)
    if request.method == 'POST':
        form = ConsoleForms(request.POST,instance=console)
        if form.is_valid():
            form.save()
            return redirect('console_list')
    else:
        form = ConsoleForms(instance=console)
    return render(request,'rental/add_console.html',{'form':form})

@login_required
def delet_console(request,console_id):
    console = get_object_or_404(Console,id=console_id)
    console.delete()
    return redirect('console_list')

# @login_required
# def toggle_repair_status(request,console_id):
#     console = get_object_or_404(Console,id=console_id)
#     console.is_repair = not console.is_repair
#     console.save()
#     return redirect('console_list')

def view_consoles(request):
    available_consoles = Console.objects.filter(status = 'available')
    rented_consoles = Console.objects.filter(status = 'rented')
    under_repair_consoles = Console.objects.filter(status='repair')
    return render(request, 'rental/view_consoles.html',{'available_consoles': available_consoles,'rented_consoles':rented_consoles,'under_repair_consoles':under_repair_consoles })

