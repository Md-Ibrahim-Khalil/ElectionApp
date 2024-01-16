from django.contrib import admin
from . models import Voter, PollingCenter

# Register your models here.


# Register your models here.
@admin.register(Voter)
class VoterAdmin(admin.ModelAdmin):
    list_display = ['id','nid','name','fathers_name','date_of_birth',]
    
@admin.register(PollingCenter)
class PollingCenterAdmin(admin.ModelAdmin):
    list_display = ['id', 'voter', 'center_name', 'slip_number']

# Register your models here.
