
from django.urls import path
from .views import  person_view, patient_view, doctor_view,  vital_view, doctor_view,doctor_account_view, user_account_view
from .views import user_phone_numbers_view, diagnostic_view
app_name = "w_page"

urlpatterns = [
    path('persons/', person_view.as_view(), name = "person_list"),
    path('persons/<int:person_id>', person_view.as_view(), name = "single_person"),
    
    path('patients/', patient_view.as_view(), name = 'patient'),
    path('patients/<int:patient_id>', patient_view.as_view(), name = 'patient'),
    
    path('doctors/', doctor_view.as_view(), name = 'doc_list'),
    path('doctors/<int:doctor_id>', doctor_view.as_view(), name = 'doc'),
    
    path('doctor_accounts/', doctor_account_view.as_view(), name = 'doc_accounts'),
    path('doctor_accounts/<int:doctor_account_id>', doctor_account_view.as_view(), name = 'doc_account'),
    
    path('user_accounts/', user_account_view.as_view(), name = 'usr_accounts'),
    path('user_accounts/<int:user_account_id>', user_account_view.as_view(), name = 'usr_account'),
    
    path('user_phones/', user_phone_numbers_view.as_view(), name = 'usr_phones'),
    path('user_phones/<int:patient_id>', user_phone_numbers_view.as_view(), name = 'usr_phone'),
    
    path('diagnostic/', diagnostic_view.as_view(), name = 'usr_phones'),
    path('diagnostic/<int:patient>', diagnostic_view.as_view(), name = 'usr_phone'),
    
    path('vitals/', vital_view.as_view(), name = 'vital_list'),
    path('vitals/<int:patient_id>', vital_view.as_view(), name = 'vital'),

]
