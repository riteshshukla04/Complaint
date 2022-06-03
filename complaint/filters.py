#!/usr/bin/python
# -*- coding: utf-8 -*-
import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

from django import forms


class DateInput(forms.DateInput):

    input_type = 'date'


class ComplaintFilter(django_filters.FilterSet):
    start_date = django_filters.DateFilter(
        field_name="IssueReportedDate",lookup_expr='gte',widget=DateInput(
            attrs={
                'IssueReportedDate': 'datepicker'
            }
        )
    )
    enddate = django_filters.DateFilter(
        field_name="IssueReportedDate",lookup_expr='lte',widget=DateInput(
            attrs={
                'IssueReportedDate': 'datepicker'
            }
        )
    )

    class Meta:

        model = Complaint
        fields = ['IssueReportedDate']
        widgets = {'IssueReportedDate': DateInput(), 'end_date': DateInput()}
