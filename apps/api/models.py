from django.db import models
from django.urls import reverse
from django.contrib import admin
from django_resized import ResizedImageField
from django.utils.safestring import mark_safe


class Company(models.Model):
    """
    The Company Model
    """

    name = models.CharField(max_length=100)
    logo = ResizedImageField(
        size=[600, 600], crop=["middle", "center"], upload_to="images/company"
    )
    summary = models.TextField(blank=True)

    @admin.display(description="Logo Display")
    def logo_display(self):
        """
        Special Function for displaying the logo in the admin panel
        """
        return mark_safe(
            f'<img src="{self.logo.url}" height=40px / style="border-radius: 10%">'
        )

    def get_absolute_url(self):
        """
        Get absolute url for admin site
        """
        return reverse("api:company_details", kwargs={"company_id": self.id})

    class Meta:
        """
        Meta Configuration for this Model
        """

        verbose_name_plural = "Companies"

    def __str__(self):
        """
        String reperesentation for the Object
        """
        return self.name


class Advocate(models.Model):
    """
    The Advocate Model
    """

    name = models.CharField("Full Name", max_length=100)
    profile_pic = ResizedImageField(
        "Avatar",
        size=[600, 600],
        crop=["middle", "center"],
        upload_to="images/advocate",
    )
    short_bio = models.CharField("Short Biography", max_length=100)
    long_bio = models.TextField("Long Biography", blank=True, null=True)
    advocate_years_exp = models.PositiveIntegerField("Advocate Year Experience")
    company = models.ForeignKey(
        Company,
        null=True,
        blank=True,
        related_name="advocates",
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        """
        String reperesentation for the Object
        """
        return self.name

    @admin.display(description="Avatar Display")
    def avatar_display(self):
        """
        Special Function for displaying the avater in the admin panel
        """
        return mark_safe(
            f'<img src="{self.profile_pic.url}" height=40px / style="border-radius: 10%">'
        )

    def get_absolute_url(self):
        """
        Get absolute url for admin site
        """
        return reverse("api:advocate_details", kwargs={"advocate_id": self.id})


class Link(models.Model):
    """
    The Link Model

    Connected to `api.Advocate` with one-to-one relationship
    """

    advocate = models.OneToOneField(
        Advocate, related_name="links", on_delete=models.CASCADE
    )
    youtube = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)

    def __str__(self):
        """
        String reperesentation for the Object
        """
        return f"{self.advocate.name}'s Links"
