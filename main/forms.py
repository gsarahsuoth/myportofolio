from django.forms import ModelForm, TextInput,Textarea,NumberInput,URLInput,DateTimeInput,Select
from main.models import Education, Experience


class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = [
            "institution",
            "degree",
            "start_year",
            "end_year",
        ]

        labels = {
            "institution": "Institution Name",
            "degree": "Degree",
            "start_year": "Start Year",
            "end_year": "End Year",
        }

        widgets = {
            "institution": TextInput(
                attrs={
                    "placeholder": "Universitas Indonesia",
                    "maxlength": 255,
                }
            ),
            "degree": Textarea(
                attrs={
                    "placeholder": "Bachelor of Computer Science",
                    "rows": 3,
                }
            ),
            "start_year": NumberInput(
                attrs={
                    "placeholder": "2025",
                }
            ),
            "end_year": NumberInput(
                attrs={
                    "placeholder": "2029 (Leave it blank if it's still on going)",
                }
            ),
        }

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = [
            "title",
            "description",
            "category",
            "thumbnail",
            "start_month",
            "start_year",
            "end_month",
            "end_year",
        ]

        labels = {
            "title": "Experience Name",
            "description": "Description",
            "category": "Category",
            "thumbnail": "Thumbnail",
            "start_month": "Start Month",
            "start_year": "Start Year",
            "end_month": "End Month",
            "end_year": "End Year",

        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Title",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Describe your experience",
                    "rows": 5,
                }
            ),
            "thumbnail": URLInput(
                attrs={
                    "placeholder": "https://example.com/image.jpg",
                    "rows": 5,
                }
            ),
            "category": Select(
                attrs={
                    "class": "form-input",
                }
            ),
            "start_month": Select(
                choices=[
                    (1, "January"),
                    (2, "February"),
                    (3, "March"),
                    (4, "April"),
                    (5, "May"),
                    (6, "June"),
                    (7, "July"),
                    (8, "August"),
                    (9, "September"),
                    (10, "October"),
                    (11, "November"),
                    (12, "December"),
                ]
            ),

            "start_year": NumberInput(
                attrs={
                    "placeholder": "2026",
                }
            ),

            "end_month": Select(
                choices=[
                    ("", "---------"),
                    (1, "January"),
                    (2, "February"),
                    (3, "March"),
                    (4, "April"),
                    (5, "May"),
                    (6, "June"),
                    (7, "July"),
                    (8, "August"),
                    (9, "September"),
                    (10, "October"),
                    (11, "November"),
                    (12, "December"),
                ]
            ),

            "end_year": NumberInput(
                attrs={
                    "placeholder": "2027",
                }
            ),
        }