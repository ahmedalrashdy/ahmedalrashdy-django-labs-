from django.shortcuts import render,redirect,reverse,get_object_or_404
from .models import Doctor
from .forms import DoctorForm
import os
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    return render(request,'doctortemp/doctor_home.html')

@login_required(login_url='user:login')
def show_forms(request):
    if request.method == 'POST':
        doctor_form = DoctorForm(request.POST,request.FILES)
        if doctor_form.is_valid():
            doctor_form.save()
            return redirect(reverse('doctors:home'))
        else:
            return redirect(reverse('doctors:error_page'))
    else:
        doctor_form = DoctorForm()
        return render(request,'doctortemp/show_form.html',{'form':doctor_form})

def doctor_delete(request,pk):
    try:

        doctor = get_object_or_404(Doctor,id=pk)
        if doctor.image:
            image_path = doctor.image.path
            if os.path.isfile(image_path):
                os.remove(image_path)
        if doctor.file_report:
            file_report_path = doctor.file_report.path
            if os.path.isfile(file_report_path):
                os.remove(file_report_path)
        doctor.delete()
        return redirect(reverse('doctors:doctors_list'))
    except:
        return redirect('doctors:error_page')

def doctor_edit(request,pk):
    doctor = get_object_or_404(Doctor,id=pk)
    if request.method == 'POST':
        try:
            print(doctor.image.path)
            # if doctor.is_valid():
            doctor.first_name = request.POST.get('fname')
            doctor.last_name = request.POST.get('lname')
            doctor.specialty = request.POST.get('specialty')
            doctor.age = request.POST.get('age')
            doctor.report = request.POST.get('report')

            if request.FILES.get('image') != None:
                image_path = doctor.image.path
                if os.path.isfile(image_path):
                    os.remove(image_path)
                doctor.image = request.FILES.get('image')
            if request.FILES.get('medicalreport') != None:
                file_path = doctor.file_report.path
                if os.path.isfile(file_path):
                    os.remove(file_path)
                doctor.file_report = request.FILES.get('medicalreport')
            
            doctor.save()
            return redirect(reverse('doctors:success_message'))
        
            # return redirect(reverse('doctors:error_page'))
        except:
            return redirect(reverse('doctors:error_page'))
    else:
        return render(request,'doctortemp/doctor_update.html',{'doctor':doctor})





    return ''

def doctor_show_detail(request,pk):
    doctor = Doctor.objects.filter(id=pk)[0]
    try:
        return render(request,'doctortemp/doctor_info.html',{'doctor':doctor})
    except:
        return redirect(reverse('doctors:error_page'))

def error_page(request):
    return render(request,'doctortemp/error_page.html')

def success_message(request):
    return render(request,'doctortemp/success_message.html')

@login_required(login_url='user:login')
def doctors_list(request):
    doctor = Doctor.objects.all()
    if doctor:
        return render(request,'doctortemp/doctors_list.html',{'doctor':doctor})
    else:
        return redirect(reverse('doctors:create'))
