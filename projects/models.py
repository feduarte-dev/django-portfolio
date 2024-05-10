from django.db import models
from projects.validators import validate_profile_fields


class Profile(models.Model):
    name = models.CharField(
        max_length=100, validators=[validate_profile_fields]
    )
    github = models.URLField(validators=[validate_profile_fields])
    linkedin = models.URLField(validators=[validate_profile_fields])
    bio = models.TextField(validators=[validate_profile_fields])

    def __str__(self) -> str:
        return self.name
