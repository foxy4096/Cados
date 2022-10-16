from django.contrib import admin
from .models import Advocate, Link, Company

admin.AdminSite.site_title = "Cados Administration 💻"
admin.AdminSite.site_header = "Cados Administration 💻"
admin.AdminSite.site_url = "/api/docs"


class LinkInline(admin.StackedInline):
    """Stacked Inline View for Link"""

    model = Link
    extra = 0
    can_delete = False


class AdvocateAdmin(admin.ModelAdmin):
    """Admin View for Advocate"""

    inlines = [LinkInline]
    search_fields = [
        "name",
        "short_bio",
        "advocate_years_exp",
        "company__name",
    ]
    list_filter = (
        "company",
        "advocate_years_exp",
    )
    fields = [
        "name",
        "short_bio",
        "advocate_years_exp",
        "company",
        "avatar_display",
        "profile_pic",
    ]
    readonly_fields = [
        "avatar_display",
    ]
    list_display = [
        "avatar_display",
        "name",
        "short_bio",
        "advocate_years_exp",
        "company",
    ]
    list_display_links = [
        "avatar_display",
        "name",
    ]
    list_per_page = 20


class CompanyAdmin(admin.ModelAdmin):
    """Admin View for Company"""

    list_display = [
        "logo_display",
        "name",
        "summary",
    ]
    search_fields = [
        "name",
        "summary",
    ]
    fields = [
        "name",
        "summary",
        "logo_display",
        "logo",
    ]
    readonly_fields = [
        "logo_display",
    ]
    list_display_links = [
        "logo_display",
        "name",
    ]
    list_per_page = 20


admin.site.register(Advocate, AdvocateAdmin)
admin.site.register(Company, CompanyAdmin)
