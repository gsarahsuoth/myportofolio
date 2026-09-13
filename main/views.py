from django.shortcuts import render

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
    context = {
        "name": "Gavrila Sarah Kartika Suoth",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def show_education(request):
    context = {
        "name": "Gavrila Sarah Kartika Suoth",
        "education_list": Education.objects.all(),
    }
    return render(request, "education.html", context)