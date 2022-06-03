from asyncio import constants
from calendar import c
from pyexpat import model
import re
from tkinter import E
from urllib import response
from django.http import HttpResponse
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .filters import *
from .decorators import *
import complaint
from .models import *

def parseDateHtml(date):
    date_obj = datetime.strptime(date, '%b %d,%Y')
    return date_obj.strftime('%d-%m-%Y')

@authenticated_user
def index(request):
   
    return HttpResponse("Hee")

@unauthenticated_user
def LoginPage(request):
    if(request.method=="POST"):
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request,user)
            return redirect("/")
        else:
           messages.info(request,"Username or password incorrect")             
     
    return render(request,"LoginPage.html")

@authenticated_user
def allComplaints(request):
    complaints=Complaint.objects.filter(Approved=True)
    myFilter=ComplaintFilter(request.GET,queryset=complaints)
    complaints=(myFilter.qs)
    return render(request,"allcomplaints.html",{"complaints":complaints,"filter":myFilter})


@authenticated_user
def Logout(request):
    logout(request)
    return redirect("/login")

@authenticated_user
def AddComplaint(request):
    if(request.method=="POST"):
        m=Complaint.objects.create(user=request.user,UniqueComplaintNumber=request.POST["UniqueComplaintNumber"],VarrocPlant=request.POST["VarrocPlant"],CustomerComplaintNumber=request.POST["CustomerComplaintNumber"],IssueReportedDate=request.POST["IssueReportedDate"],IssueReportedMonth=request.POST["IssueReportedMonth"],CustomerName=request.POST["CustomerName"],CustomerLocation=request.POST["CustomerLocation"],ReportedArea=request.POST["ReportedArea"],NewExisting=request.POST["NewExisting"],SourceOfComplaint=request.POST["SourceOfComplaint"],ProductCategory=request.POST["ProductCategory"],CustomerPartNumber=request.POST["CustomerPartNumber"],CustomerModel=request.POST["CustomerModel"],PartManufacturingDate=request.POST["PartManufacturingDate"],RejectedQuantity=request.POST["RejectedQuantity"],PPMNonPPM=request.POST["PPMNonPPM"],ComplaintRepeated=request.POST["ComplaintRepeated"],ProcessDesignSupplier=request.POST["ProcessDesignSupplier"],FourMCategory=request.POST["FourMCategory"],CustomerComplaint=request.POST["CustomerComplaint"],DefectDescription=request.POST["DefectDescription"],VarrocObservation=request.POST["VarrocObservation"],ContainmentAction=request.POST["ContainmentAction"],ICATargetDate=request.POST['ICATargetDate'],ICAActualDate=request.POST['ICAActualDate'],OutflowRootCause=request.POST['OutflowRootCause'],OutflowRootCauseSideAction=request.POST['OutflowRootCauseSideAction'],OutflowRootCauseResp=request.POST['OutflowRootCauseResp'],OutflowRootCauseTargetDate=request.POST['OutflowRootCauseTargetDate'],OutflowRootCauseActualDate=request.POST['OutflowRootCauseActualDate'],OccurenceRootCause=request.POST['OccurenceRootCause'],OccurenceRootCauseSideAction=request.POST['OccurenceRootCauseSideAction'],OccurenceRootCauseResp=request.POST['OccurenceRootCauseResp'],OccurenceRootCauseTargetDate=request.POST['OccurenceRootCauseTargetDate'],OccurenceRootCauseActualDate=request.POST['OccurenceRootCauseActualDate'],SystemAction=request.POST['SystemAction'],SustenanceAction=request.POST['SustenanceAction'],Status=request.POST['Status'],TargetDateForActionVerification=request.POST['TargetDateForActionVerification'],ActualDateForActionVerification=request.POST['ActualDateForActionVerification'],ComplaintClosureDate=request.POST['ComplaintClosureDate'],Ageing=request.POST['Ageing'],HDApplicablity=request.POST['HDApplicablity'],HDModels=request.POST['HDModels'],ProductCategoryRemark=request.POST['ProductCategoryRemark'],DocumentUploaded=request.POST['DocumentUploaded'],EffectiveMontioringM1=request.POST['EffectiveMontioringM1'],EffectiveMontioringM2=request.POST['EffectiveMontioringM2'],EffectiveMontioringM3=request.POST['EffectiveMontioringM3'],Remarks=request.POST['Remarks'])
    return render(request,"AddComplaint.html")


@authenticated_user
def UpdateComplaint(request,pk):
    
    s=Complaint.objects.get(id=pk)
    date=s.IssueReportedDate
    date=(datetime.strptime(str(date), "%Y-%m-%d").strftime('%Y-%m-%d'))
    date2=(datetime.strptime(str(s.IssueReportedMonth), "%Y-%m-%d").strftime('%Y-%m-%d'))
    if(request.user==s.user):
        if(request.method=="POST"):
            s.UniqueComplaintNumber=request.POST["UniqueComplaintNumber"]
            s.VarrocPlant=request.POST["VarrocPlant"]
            s.CustomerComplaintNumber=request.POST["CustomerComplaintNumber"]
            s.IssueReportedDate=request.POST["IssueReportedDate"]
            s.IssueReportedMonth=request.POST["IssueReportedMonth"]
            s.CustomerName=request.POST["CustomerName"]
            s.CustomerLocation=request.POST["CustomerLocation"]
            s.ReportedArea=request.POST["ReportedArea"]
            s.NewExisting=request.POST["NewExisting"]
            s.SourceOfComplaint=request.POST["SourceOfComplaint"]
            s.ProductCategory=request.POST["ProductCategory"]
            s.CustomerPartNumber=request.POST["CustomerPartNumber"]
            s.CustomerModel=request.POST["CustomerModel"]
            s.PartManufacturingDate=request.POST["PartManufacturingDate"]
            s.RejectedQuantity=request.POST["RejectedQuantity"]
            s.PPMNonPPM=request.POST['PPMNonPPM']
            s.ComplaintRepeated=request.POST['ComplaintRepeated']
            s.ProcessDesignSupplier=request.POST['ProcessDesignSupplier']
            s.FourMCategory=request.POST['FourMCategory']
            s.CustomerComplaint=request.POST['CustomerComplaint']
            s.DefectDescription=request.POST['DefectDescription']

            print(request.POST["DefectDescription"],"hwh")
            s.VarrocObservation=request.POST['VarrocObservation']
            s.ContainmentAction=request.POST['ContainmentAction']
            s.ICATargetDate=request.POST['ICATargetDate']
            s.ICAActualDate=request.POST['ICAActualDate']
            s.OutflowRootCause=request.POST['OutflowRootCause']
            s.OutflowRootCauseSideAction=request.POST['OutflowRootCauseSideAction']
            s.OutflowRootCauseResp=request.POST['OutflowRootCauseResp']
            s.OutflowRootCauseTargetDate=request.POST['OutflowRootCauseTargetDate']
            s.OutflowRootCauseActualDate=request.POST['OutflowRootCauseActualDate']
            s.OccurenceRootCause=request.POST['OccurenceRootCause']
            s.OccurenceRootCauseSideAction=request.POST['OccurenceRootCauseSideAction']
            s.OccurenceRootCauseResp=request.POST['OccurenceRootCauseResp']
            s.OccurenceRootCauseTargetDate=request.POST['OccurenceRootCauseTargetDate']
            s.OccurenceRootCauseActualDate=request.POST['OccurenceRootCauseActualDate']
            s.SystemAction=request.POST['SystemAction']
            s.SustenanceAction=request.POST['SustenanceAction']
            s.Status=request.POST['Status']
            s.TargetDateForActionVerification=request.POST['TargetDateForActionVerification']
            s.ActualDateForActionVerification=request.POST['ActualDateForActionVerification']
            s.ComplaintClosureDate=request.POST['ComplaintClosureDate']
            s.Ageing=request.POST['Ageing']
            s.HDApplicablity=request.POST['HDApplicablity']
            s.HDModels=request.POST['HDModels']
            s.ProductCategoryRemark=request.POST['ProductCategoryRemark']
            s.DocumentUploaded=request.POST['DocumentUploaded']
            s.EffectiveMontioringM1=request.POST['EffectiveMontioringM1']
            s.EffectiveMontioringM2=request.POST['EffectiveMontioringM2']
            s.EffectiveMontioringM3=request.POST['EffectiveMontioringM3']
            s.Remarks=request.POST['Remarks']
            s.save()
            print("Aaa")
            return redirect("/viewcomplaint")
        return render(request,"updateComplaint.html",{"Complaint":s,"date1":date,"date2":date2})
    else:
        return HttpResponse("Not Authorised")


def ViewAllComplaint(request):
    complaints=Complaint.objects.filter(user=request.user)
    return render(request,"ViewComplaint.html",{"complaints":complaints})

@authenticated_user
def ViewSingleComplaint(request,pk):
    s=Complaint.objects.get(id=pk)
    if(request.user==s.user):
        return render(request,"ViewSpecificComplaint.html",{"Complaint":s})
    else:
        return HttpResponse("Not Authorised")



def ViewPastSingleComplaint(request,pk):

    s=Complaint.objects.get(id=pk)
    
    return render(request,"ViewSpecificComplaint.html",{"Complaint":s})



@authenticated_user
def ApproveComplaintsView(request):

    group=request.user.groups.all()
    if(group[0].name=="Approver"):
        complaints=Complaint.objects.filter(VarrocPlant=group[1].name,Approved=False)
        
        return  render(request,"ApproveList.html",{"complaints":complaints})
    else:
        return HttpResponse("You are not an approver")


@authenticated_user
def ApproveComplaint(request,pk):
    group=request.user.groups.all()
    
    Complaints=Complaint.objects.get(id=pk)
    print(group[1].name,Complaints.VarrocPlant)
    if(group[1].name!=Complaints.VarrocPlant):
        return HttpResponse("Not Authorised")
    if(group[0].name=="Approver"):
        print(request.POST)
        if(request.method=="POST"):
            if 'Approve' in request.POST:    
                ApproverRemarks=request.POST["ApproverRemarks"]
                Complaints.ApproverRemarks=ApproverRemarks
                Complaints.Approved=True
                Complaints.save()
            
            # do some listing...
            else:
                ApproverRemarks=request.POST["ApproverRemarks"]
                Complaints.ApproverRemarks=ApproverRemarks
       
        # do something else
            return render(request,"ApproveSpecificComplaint.html",{"Complaint":Complaints})
        else:
            return render(request,"ApproveSpecificComplaint.html",{"Complaint":Complaints})
    else:
        return HttpResponse("You are not an approver")


def ViewOpenComplaint(request):
    group=request.user.groups.all()
    complaints=Complaint.objects.filter(VarrocPlant=group[1].name)
    return render(request,'ViewOpenComplaints.html',{'complaints':complaints})


def Search(request):
    query=request.GET["query"]
    a=Complaint.objects.filter(DefectDescription__contains=query)
    b=Complaint.objects.filter(CustomerName__contains=query)
    c=Complaint.objects.filter(ProductCategory__contains=query)
    d=Complaint.objects.filter(UniqueComplaintNumber__contains=query)
    e=Complaint.objects.filter(CustomerPartNumber__contains=query)
    f=Complaint.objects.filter(CustomerComplaintNumber__contains=query)
    complaint=a.union(b).union(c).union(d).union(e).union(f)
    complaints=complaint
    return render(request,"search.html",{"complaints":complaints}) 
    