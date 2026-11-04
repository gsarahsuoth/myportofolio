from django.utils.html import strip_tags
from rest_framework import serializers

from main.models import Experience


class ExperienceSerializer(serializers.ModelSerializer):
    star_count = serializers.SerializerMethodField()
    is_starred = serializers.SerializerMethodField()
    starred_by_names = serializers.SerializerMethodField()

    class Meta:
        model = Experience
        fields = [
            "id",
            "title",
            "description",
            "category",
            "thumbnail",
            "start_month",
            "start_year",
            "end_month",
            "end_year",
            "is_ongoing",
            "star_count",
            "is_starred",
            "starred_by_names",
        ]
        read_only_fields = ["id"]

    def validate_title(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError("Title cannot be empty.")
        return value

    def validate_description(self, value):
        return strip_tags(value)

    def validate_category(self, value):
        valid_choices = [choice[0] for choice in Experience.EXPERIENCE_CHOICES]
        if value not in valid_choices:
            raise serializers.ValidationError("Invalid category choice.")
        return value

    def get_star_count(self, obj):
        return obj.starred_by.count()

    def get_is_starred(self, obj):
        request = self.context.get("request")
        if request is None or not request.user.is_authenticated:
            return False
        return request.user in obj.starred_by.all()

    def get_starred_by_names(self, obj):
        return ", ".join(user.username for user in obj.starred_by.all())
    
from main.models import Experience
from main.serializers import ExperienceSerializer

experiences = Experience.objects.all()
print(ExperienceSerializer(experiences, many=True).data)

candidate = ExperienceSerializer(
    data={
        "title": "Software Engineer Intern",
        "description": "Building web apps using Django and React",
        "category": "internship",
        "thumbnail": "https://example.com/image.png",
        "start_month": 6,
        "start_year": 2025,
        "end_month": 12,
        "end_year": 2025,
    }
)
print(candidate.is_valid())
print(candidate.validated_data)

invalid = ExperienceSerializer(data={"title": "", "category": "invalid-choice"})
print(invalid.is_valid())
print(invalid.errors)