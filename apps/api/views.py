from typing import List
from ninja import NinjaAPI
from django.db.models import Q
from .authenticate import ApiKey
from ninja.pagination import paginate
from .models import Advocate, Company
from ninja.security import django_auth
from django.shortcuts import get_object_or_404
from .schema import AdvocateSchema, CompanySchema

api = NinjaAPI(
    title="Cados 💻", urls_namespace="api", csrf=True, auth=[django_auth, ApiKey()]
)


@api.get("/advocates", response=List[AdvocateSchema])
@paginate
def advocates_list(request):
    """
    Return All the Advocates from the Database
    """
    return Advocate.objects.all()


@api.get("/advocates/{advocate_id}", response=AdvocateSchema)
def advocate_details(request, advocate_id: int):
    """
    Return the Advocate with the given id
    """
    return get_object_or_404(Advocate, id=advocate_id)


@api.get("/companies", response=List[CompanySchema])
@paginate
def companies_list(request):
    """
    Return All the Companies from the Database
    """
    return Company.objects.all()


@api.get("/companies/{company_id}", response=CompanySchema)
def company_details(request, company_id: int):
    """
    Return the Company with the given id
    """
    return get_object_or_404(Company, id=company_id)


@api.get("/search/advocates", response=List[AdvocateSchema])
@paginate
def search_advocates(request, query: str):
    """
    Search the Advocates in the database with the given query
    """
    queryset = Advocate.objects.filter(
        Q(name__icontains=query)
        | Q(short_bio__icontains=query)
        | Q(long_bio__icontains=query)
    )
    return queryset


@api.get("/search/companies", response=List[CompanySchema])
@paginate
def search_companies(request, query: str):
    """
    Search the Companies in the database with the given query
    """
    queryset = Company.objects.filter(
        Q(name__icontains=query) | Q(summary__icontains=query)
    )
    return queryset
