from django.forms import ModelForm, TextInput,Textarea,NumberInput,URLInput,DateTimeInput,Select
from django.core.exceptions import ValidationError
from django.utils.html import strip_tags
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
        def clean_institution(self):
            institution = strip_tags(self.cleaned_data.get("institution", "")).strip()
            if not institution:
                raise ValidationError("Education institution can't be empty or contain only HTML tags.")
            return institution

        def clean_degree(self):
            degree = strip_tags(self.cleaned_data.get("degree", "")).strip()
            if not degree:
                raise ValidationError("Degree can't be empty or contain only HTML tags.")
            return degree

        def clean_start_year(self):
            start_year = self.cleaned_data.get("start_year")
            if start_year is None:
                raise ValidationError("Start year is required.")
            return start_year

        def clean_end_year(self):
            start_year = self.cleaned_data.get("start_year")
            end_year = self.cleaned_data.get("end_year")

            # Validasi logika: end_year tidak boleh lebih kecil dari start_year
            if start_year and end_year and end_year < start_year:
                raise ValidationError("End year cannot be earlier than start year.")

            return end_year

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
        def clean_title(self):
            title = strip_tags(self.cleaned_data["title"]).strip()
            if not title:
                raise ValidationError("Experience name can't contain only HTML tags.")
            return title

        def clean_description(self):
            return strip_tags(self.cleaned_data["description"]).strip()

        def clean_thumbnail(self):
            return strip_tags(self.cleaned_data["thumbnail"]).strip()