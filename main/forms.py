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
            "started_at",
            "ended_at",
        ]

        labels = {
            "title": "Experience Name",
            "description": "Description",
            "category": "Category",
            "thumbnail": "Thumbnail",
            "started_at": "Start Date",
            "ended_at": "End Date",

        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Title",
                    "maxlength": 255,
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
            "started_at": DateTimeInput(
                attrs={
                    "type": "datetime-local",
                }
            ),
            "ended_at": DateTimeInput(
                attrs={
                    "type": "datetime-local",
                }
            ),
        }