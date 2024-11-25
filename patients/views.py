from django.shortcuts import render, redirect,reverse,get_object_or_404
import os
from .models import Patients
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='user:login')
def home(request):
    return render(request,'patients_home.html')

@login_required(login_url='user:login')
def patients_create(request):
    if request.method == 'POST':
        try:
            patient = Patients.objects.create(
                first_name = request.POST.get('fname'),
                last_name  = request.POST.get('lname'),
                age = request.POST.get('age'),
                image = request.FILES.get('image'),
                file_report = request.FILES.get('medicalreport'),
                report = request.POST.get('report')
            )
            return redirect(reverse('patients:success_message'))
        except IntegrityError:
            return redirect(reverse('patients:error_page'))
    else:
        return render(request, 'patients_create.html')

@login_required(login_url='user:login')
def patients_list(request):
    patients = Patients.objects.all()
    if patients:
        return render(request,'patients_list.html',{'patients':patients})
    else:
        return redirect(reverse('patients:error_page'))

def success_message(request):
    return render(request,'success_message.html')

@login_required(login_url='user:login')
def error_page(request):
    return render(request,'error_page.html')

def patient_show_detail(request,pk):
    patient = Patients.objects.filter(id=pk)[0]
    try:
        return render(request,'patient_info.html',{'patient':patient})
    except:
        return redirect(reverse('patients:error_page'))

@login_required(login_url='user:login')
def patient_edit(request,pk):
    patient = get_object_or_404(Patients,id=pk)
    if request.method == 'POST':
        try:
            patient.first_name = request.POST.get('fname')
            patient.last_name = request.POST.get('lname')
            patient.age = request.POST.get('age')
            patient.report = request.POST.get('report')

            if request.FILES.get('medicalreport') != None:
                file_path = patient.file_report.path
                if os.path.isfile(file_path):
                    os.remove(file_path)
                patient.file_report = request.FILES.get('medicalreport')
                
            if request.FILES.get('image') != None:
                image_path = patient.image.path
                if os.path.isfile(image_path):
                    os.remove(image_path)
                patient.image = request.FILES.get('image')

            patient.save()
            return redirect(reverse('patients:success_message'))
        except IntegrityError:
            return redirect(reverse('patients:error_page'))
    else:
        return render(request,'patients_update.html',{'patient':patient})


def patient_delete(request,pk):
    try:
        patient = get_object_or_404(Patients,id=pk)

        if patient.image:
            image_path = patient.image.path 
            if os.path.isfile(image_path):
                os.remove(image_path)
        if patient.file_report:
            file_report_path = patient.file_report.path 
            if os.path.isfile(file_report_path):
                os.remove(file_report_path)
        patient.delete()
        return redirect(reverse('patients:success_message'))
    except:
        return redirect(reverse('patients:error_page'))
from .forms import PatientsForm

@login_required(login_url='user:login')
def show_forms(request):
    if request.method == 'POST':
        patient_form = PatientsForm(request.POST,request.FILES)
        if patient_form.is_valid():
            patient_form.save()
            return HttpResponse('Created')
        else:
            return HttpResponse('Field!!')
    else:
        patient_form = PatientsForm()
        return render(request,'other_type_forms.html',{'form':patient_form})