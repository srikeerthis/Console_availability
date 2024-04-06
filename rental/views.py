from django.shortcuts import render,redirect
from .models import Console
from .forms import ConsoleForms
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

# Create your views here.
def console_list(request):
    consoles = Console.objects.all()
    return render(request,'rental/console_list.html',{'consoles':consoles})

def toggle_rental_status(request,console_id):
    console = Console.objects.get(id=console_id)
    console.is_rented = not console.is_rented
    console.save()
    return redirect('console_list')

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

def view_consoles(request):
    available_consoles = Console.objects.filter(is_rented = False)
    rented_consoles = Console.objects.filter(is_rented = True)
    return render(request, 'rental/view_consoles.html',{'available_consoles': available_consoles,'rented_consoles':rented_consoles})
