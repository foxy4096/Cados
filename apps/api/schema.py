from typing import List
from ninja import ModelSchema
from .models import Advocate, Company, Link


class NestedAdvocateSchema(ModelSchema):
    """
    API Schema for Nested `Advocate` Object to be displayed in the `CompanySchema`
    """

    class Config:
        model = Advocate
        model_fields = [
            "id",
            "name",
            "profile_pic",
            "short_bio",
            "long_bio",
            "advocate_years_exp",
        ]


class CompanySchema(ModelSchema):
    """
    API Schema for `Company` Object
    """

    advocates: List[NestedAdvocateSchema] = []

    class Config:
        model = Company
        model_fields = "__all__"


class NestedComapnySchema(ModelSchema):
    """
    API Schema for Nested `Company` Object to be displayed in the `AdvocateSchema`
    """

    class Config:
        model = Company
        model_fields = [
            "id",
            "logo",
            "summary",
        ]


class LinkSchema(ModelSchema):
    """
    API Schema for Nested `Link` Object to be displayed in the `AdvocateSchema`
    """

    class Config:
        model = Link
        model_fields = "__all__"


class AdvocateSchema(ModelSchema):
    """
    API Schema for `Advocate` Object
    """

    company: NestedComapnySchema = None
    links: LinkSchema

    class Config:
        model = Advocate
        model_fields = "__all__"
