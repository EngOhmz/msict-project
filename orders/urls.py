from django.urls import path
from . import views

urlpatterns = [
    # Home page
    path('', views.home, name='home'),
    # Login page
    path('login/', views.custom_login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
     # New pages
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
     # Dashboard stats API
    path('api/dashboard-stats/', views.dashboard_stats, name='dashboard_stats'),
    path('api/request-status/<int:request_id>/', views.get_request_status, name='get_request_status'),
    # Department (HZO)
    path('department/dashboard/', views.department_dashboard, name='department_dashboard'),
    path('department/submit/', views.submit_request, name='submit_request'),
    path('department/mark-response-read/<int:response_id>/', views.mark_response_read, name='mark_response_read'),
    path('my-requests/', views.my_requests_view, name='my_requests'),
    path('notifications/', views.notifications_view, name='notifications'),
    path('feedbacks/', views.feedback_view, name='feedback'),
    # QM (Store Keeper)
    path('qm/dashboard/', views.qm_dashboard, name='qm_dashboard'),
    path('qm/forward/', views.qm_forward, name='qm_forward'),
    path('qm/forward-to-co/', views.forward_to_co, name='forward_to_co'),
    path('qm/respond-to-department/', views.respond_to_department, name='respond_to_department'),
    path('qm/mark-feedback-read/<int:feedback_id>/', views.mark_feedback_read, name='mark_feedback_read'),
    path('qm/feedbacks/', views.view_feedbacks, name='qm_feedbacks'),
    path('qm/incoming/', views.qm_incoming_requests, name='qm_incoming_requests'),
    path('qm/forwarded-requests/', views.forwarded_requests_view, name='forwarded_requests'),
    path('qm/decisions/', views.co_decisions_view, name='co_decisions'),
    path('co-feedback/', views.co_feedback_view, name='co_feedback'),
    # CO (Commanding Officer)
    path('co/dashboard/', views.co_dashboard, name='co_dashboard'),
    path('co/action/', views.co_action, name='co_action'),
    path('co/send-feedback/', views.send_feedback, name='send_feedback'),
    path('review-requests/', views.review_requests_view, name='review_requests'),
    path('decision-history/', views.decision_history_view, name='decision_history'),
    path('send-feedback/', views.send_feedback_view, name='send_feedback'),

]
