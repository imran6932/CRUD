from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import Registration
from django.contrib import messages

# Create your views here.

# Input Function
def addStudent(request):
    if request.method == 'POST':
        form = StudentRegistration(request.POST)
        if form.is_valid():
            form.save()
            form = StudentRegistration()
            messages.success(request, 'Student Added Successfully')
            
    else:
        form = StudentRegistration()
    stu = Registration.objects.all()
    return render(request, 'student/addandshow.html', {'form':form, 'fm':stu})

# delete function

def delete_data(request,id):
    if request.method == 'POST':
        pi = Registration.objects.get(pk=id)
        pi.delete()
        messages.warning(request, 'Form Deleted Successfully')
        return HttpResponseRedirect('/')

# update function

def update_data(request,id):
    if request.method == 'POST':
        pi = Registration.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Form updated Successfully')
            
    else:
        pi = Registration.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
    return render(request, 'student/update.html', {'form':fm})