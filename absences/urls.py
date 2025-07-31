from django.urls import path
from . import views



urlpatterns = [
    path('', views.accueil_public, name='accueil_public'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('changer_mot_de_passe/', views.changer_mot_de_passe, name='changer_mot_de_passe'),
# -----------------------------#
# Partie pour les collaborateur#
# -----------------------------#
    path('dashboard/', views.dashboard_collaborateur, name='dashboard_collaborateur'),
    path('soumettre/', views.soumettre_absence, name='soumettre_absence'),
    path('mes-absences/', views.mes_absences, name='mes_absences'),
    path('calendrier/', views.calendrier_absences, name='calendrier_absences'), 
    path('mes-quotas/', views.mon_quota, name='mon_quota'),
# -----------------------------#
# Partie pour les superieurs   #
# -----------------------------#
    path('superieur/dashboard/', views.dashboard_superieur, name='dashboard_superieur'),
    path('absence/<int:absence_id>/approuver/', views.approuver_absence, name='approuver_absence'),
    path('absence/<int:absence_id>/rejeter/', views.rejeter_absence, name='rejeter_absence'),
# -----------------------------#
# Partie DRH                   #
# -----------------------------#    
    path('drh/dashboard/', views.dashboard_drh, name='dashboard_drh'),
    path('absence/<int:absence_id>/verifier/', views.verifier_absence, name='verifier_absence'),
    path('absence/<int:absence_id>/rejeter_drh/', views.rejeter_absence_drh, name='rejeter_absence_drh'),


# -----------------------------#
# Partie DP                    #
# -----------------------------#   
    path('dp/dashboard/', views.dashboard_dp, name='dashboard_dp'),
    path('absence/<int:absence_id>/valider_dp/', views.valider_absence_dp, name='valider_absence_dp'),
    path('absence/<int:absence_id>/rejeter_dp/', views.rejeter_absence_dp, name='rejeter_absence_dp'),  
    path('dashboard/dp/export/', views.exporter_absences_excel, name='exporter_absences_excel'),
  
    
# -----------------------------#
# Partie Admin                  #
# -----------------------------# 
    path('dashboard/admingestion', views.admin_users, name='admin_users'),
    # path('admin_dashboard/', views.dashboard_admin, name='dashboard_admin'),
    # path('admin_users/', views.admin_users, name='admin_users'),
    # path('admin_users/ajouter/', views.admin_user_create, name='admin_user_create'),
    # path('admin_users/<int:user_id>/modifier/', views.admin_user_edit, name='admin_user_edit'),
    # path('admin_users/ajouter/', views.admin_user_create, name='admin_user_create'),
    # path('admin_users/<int:user_id>/supprimer/', views.admin_user_delete, name='admin_user_delete'),
    path('configurations/', views.configuration_view, name='configuration_view'),  
    # path('admin_quotas/', views.quotas_view, name='quotas_views'),        
    # path('admin/absences/', views.admin_absences_view, name='admin_absences'),
    # path('admin/types/', views.admin_types_view, name='admin_types'),     
    # path('admin/feries/', views.admin_feries_view, name='admin_feries'),  
               
               
               
]