from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from main.forms import EducationForm,ExperienceForm
from main.models import Experience, Education


def show_main(request):
    context = {
        "name": "Gavrila Sarah Kartika Suoth",
        "npm": "2506559071",
        "study_program": "S1 Kelas Internasional Ilmu Komputer",
        "bio": (
            "Greetings! I'm Sarah, a CS Student at Universitas Indonesia actively shaping student tech experiences as a Teaching Assistant and taking an active role on COMPFEST and various student initiatives"
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    json_response = get_experience_json(request)

    experiences = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    experiences = [experiences.object for experiences in experiences]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Gavrila Sarah Kartika Suoth",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def show_education(request):
    json_response = get_education_json(request)

    educations = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    educations = [educations.object for educations in educations]
    institute_query = request.GET.get("institution", "").strip()

    context = {
        "name": "Gavrila Sarah Kartika Suoth",
        "education_list": Education.objects.all(),
    }
    return render(request, "education.html", context)

def create_education(request):
    form = EducationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Edukasi baru berhasil ditambahkan!")
        return redirect("main:show_education")

    context = {
        "name": "Gavrila Sarah Kartika Suoth",
        "form": form,
    }
    return render(request, "education_form.html", context)

def delete_education(request, education_id):
    education = get_object_or_404(Education, pk=education_id)

    if request.method == "POST":
        education.delete()
        messages.success(request, "Education berhasil dihapus!")
        return redirect("main:show_education")

    return redirect("main:show_education")

def get_education_json(request):
    institute_query = request.GET.get("institution", "").strip()
    educations = Education.objects.all()

    if institute_query:
        educations = educations.filter(title__icontains=institute_query)

    educations_json = serializers.serialize("json", educations)
    return HttpResponse(educations_json, content_type="application/json")

def create_experience(request):
    form = ExperienceForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Experience baru berhasil ditambahkan!")
        return redirect("main:show_experience")

    context = {
        "name": "Gavrila Sarah Kartika Suoth",
        "form": form,
    }
    return render(request, "experience_form.html", context)

def delete_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        experience.delete()
        messages.success(request, "Experience berhasil dihapus!")
        return redirect("main:show_experience")

    return redirect("main:show_experience")

def get_experience_json(request):
    title_query = request.GET.get("title", "").strip()
    experience = Experience.objects.all()

    if title_query:
        experience = experience.filter(title__icontains=title_query)

    experience_json = serializers.serialize("json", experience)
    return HttpResponse(experience_json, content_type="application/json")

def update_experience(request, id):
    experience = get_object_or_404(Experience, pk=id)

    form = ExperienceForm(request.POST or None, instance=experience)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("main:show_experience")

    context = {
        "name": "Gavrila Sarah Kartika Suoth",
        "form": form,
        "experience": experience,
    }

    return render(request, "experience_form.html", context)