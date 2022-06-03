
from django import views
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.index),
    path("login/",views.LoginPage),
    path("logout/",views.Logout),
    path("all/",views.allComplaints),
    path("addcomplaint/",views.AddComplaint),
    path("updatecomplaint/<str:pk>",views.UpdateComplaint),
    path("viewcomplaint/",views.ViewAllComplaint),
    path("viewsinglecomplaint/<str:pk>",views.ViewSingleComplaint),
    path("viewdetailedcomplaint/<str:pk>",views.ViewPastSingleComplaint),
    path("approveComplaints/",views.ApproveComplaintsView),
    path("approve/<str:pk>",views.ApproveComplaint),
    path("search",views.Search),
    path("openComplaints/",views.ViewOpenComplaint)
]

