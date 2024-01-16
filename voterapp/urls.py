from django.urls import path
from .views import CreateVoterView, AddPollingCenterView, UpdateDataView, ListVotersView, GetPollingCenterView

urlpatterns = [
    # Assuming you are using path() for your URL patterns
    path('create_voter/', CreateVoterView.as_view(), name='create-voter'),
    path('add_polling_center/', AddPollingCenterView.as_view(), name='add-polling-center'),
    path('update_data/<int:nid>/', UpdateDataView.as_view(), name='update-data'),
    path('list_voters/<int:polling_center_id>/', ListVotersView.as_view(), name='list-voters'),
    path('get_polling_center/<int:nid>/', GetPollingCenterView.as_view(), name='get-polling-center'),
]
