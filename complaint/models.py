
from datetime import datetime
from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Complaint(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    UniqueComplaintNumber=models.CharField(max_length=200,blank=True,null=True)
    VarrocPlant=models.CharField(max_length=200,blank=True,null=True)#Prefix+customername+plantCode+Year+Time
    CustomerComplaintNumber=models.CharField(max_length=200,blank=True,null=True)
    IssueReportedDate=models.DateField(blank=True,null=True)
    IssueReportedMonth=models.DateField(blank=True,null=True)
    CustomerName=models.CharField(max_length=200,blank=True,null=True)
    CustomerLocation=models.CharField(max_length=200,blank=True,null=True)
    ReportedArea=models.CharField(max_length=200,blank=True,null=True)
    NewExisting=models.CharField(max_length=200,blank=True,null=True)
    SourceOfComplaint=models.CharField(max_length=200,blank=True,null=True)
    ProductCategory=models.CharField(max_length=200,blank=True,null=True)
    CustomerPartNumber=models.CharField(max_length=200,blank=True,null=True)
    CustomerModel=models.CharField(max_length=200,blank=True,null=True)
    PartManufacturingDate=models.CharField(max_length=200,blank=True,null=True,default=datetime.now())
    RejectedQuantity=models.CharField(max_length=200,blank=True,null=True)
    PPMNonPPM=models.CharField(max_length=200,blank=True,null=True)
    ComplaintRepeated=models.CharField(max_length=200,blank=True,null=True)
    ProcessDesignSupplier=models.CharField(max_length=200,blank=True,null=True)
    FourMCategory=models.CharField(max_length=200,blank=True,null=True)
    CustomerComplaint=models.TextField(blank=True,null=True)
    DefectDescription=models.CharField(max_length=200,blank=True,null=True)
    VarrocObservation=models.TextField(blank=True,null=True)
    ContainmentAction=models.TextField(blank=True,null=True)
    ICATargetDate=models.TextField(blank=True,null=True)
    ICAActualDate=models.TextField(blank=True,null=True)
    OutflowRootCause=models.TextField(blank=True,null=True)
    OutflowRootCauseSideAction=models.TextField(blank=True,null=True)
    OutflowRootCauseResp=models.CharField(max_length=200,blank=True,null=True)
    OutflowRootCauseTargetDate=models.TextField(blank=True,null=True)
    OutflowRootCauseActualDate=models.TextField(blank=True,null=True)
    OccurenceRootCause=models.TextField(blank=True,null=True)
    OccurenceRootCauseSideAction=models.TextField(blank=True,null=True)
    OccurenceRootCauseResp=models.CharField(max_length=200,blank=True)
    OccurenceRootCauseTargetDate=models.TextField(blank=True,null=True)
    OccurenceRootCauseActualDate=models.TextField(blank=True,null=True)
    SystemAction=models.TextField(blank=True,null=True)
    SustenanceAction=models.TextField(blank=True)
    Status=models.CharField(max_length=200,blank=True,null=True)
    TargetDateForActionVerification=models.TextField(blank=True,null=True)
    ActualDateForActionVerification=models.TextField(blank=True,null=True)
    ComplaintClosureDate=models.TextField(blank=True,null=True)
    Ageing=models.CharField(max_length=200,blank=True,null=True)
    HDApplicablity=models.CharField(max_length=200,blank=True,null=True)
    HDModels=models.CharField(max_length=200,blank=True,null=True)
    ProductCategoryRemark=models.TextField(blank=True,null=True)
    DocumentUploaded=models.TextField(blank=True,null=True)
    EffectiveMontioringM1=models.CharField(max_length=200,blank=True,null=True)
    EffectiveMontioringM2=models.CharField(max_length=200,blank=True,null=True)
    EffectiveMontioringM3=models.CharField(max_length=200,blank=True,null=True)
    Remarks=models.TextField(blank=True,null=True)
    File=models.FileField(null=True,blank=True)
    ApproverRemarks=models.TextField(null=True,blank=True)
    Approved=models.BooleanField(default=False)
    def __str__(self):
        return str(self.CustomerComplaintNumber)






