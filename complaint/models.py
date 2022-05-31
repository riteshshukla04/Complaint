
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Complaint(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    UniqueComplaintNumber=models.CharField(max_length=200)
    VarrocPlant=models.CharField(max_length=200)#Prefix+customername+plantCode+Year+Time
    CustomerComplaintNumber=models.CharField(max_length=200)
    IssueReportedDate=models.DateField()
    IssueReportedMonth=models.DateField()
    CustomerName=models.CharField(max_length=200)
    CustomerLocation=models.CharField(max_length=200)
    ReportedArea=models.CharField(max_length=200)
    NewExisting=models.CharField(max_length=200)
    SourceOfComplaint=models.CharField(max_length=200)
    ProductCategory=models.CharField(max_length=200)
    CustomerPartNumber=models.CharField(max_length=200)
    CustomerModel=models.CharField(max_length=200)
    PartManufacturingDate=models.DateField()
    RejectedQuantity=models.CharField(max_length=200)
    PPMNonPPM=models.CharField(max_length=200)
    ComplaintRepeated=models.CharField(max_length=200)
    ProcessDesignSupplier=models.CharField(max_length=200)
    FourMCategory=models.CharField(max_length=200)
    CustomerComplaint=models.TextField()
    DefectDescription=models.TextField()
    VarrocObservation=models.TextField()
    ContainmentAction=models.TextField()
    ICATargetDate=models.DateField()
    ICAActualDate=models.DateField()
    OutflowRootCause=models.TextField()
    OutflowRootCauseSideAction=models.TextField()
    OutflowRootCauseResp=models.CharField(max_length=200)
    OutflowRootCauseTargetDate=models.DateField()
    OutflowRootCauseActualDate=models.DateField()
    OccurenceRootCause=models.TextField()
    OccurenceRootCauseSideAction=models.TextField()
    OccurenceRootCauseResp=models.CharField(max_length=200)
    OccurenceRootCauseTargetDate=models.DateField()
    OccurenceRootCauseActualDate=models.DateField()
    SystemAction=models.TextField()
    SubstenceAction=models.TextField()
    Status=models.CharField(max_length=200)
    TargetDateForActionVerification=models.DateField()
    ActualDateForActionVerification=models.DateField()
    ComplaintClosureDate=models.DateField()
    Ageing=models.CharField(max_length=200)
    HDApplicablity=models.CharField(max_length=200)
    HDModels=models.CharField(max_length=200)
    DocumentUploaded=models.TextField()
    EffectiveMontioringM1=models.CharField(max_length=200)
    EffectiveMontioringM2=models.CharField(max_length=200)
    EffectiveMontioringM3=models.CharField(max_length=200)
    Remarks=models.TextField()
    def __str__(self) -> str:
        return self.UniqueComplaintNumber





