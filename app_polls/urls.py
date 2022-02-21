from django.urls import path
from .import views




app_name = 'app_polls'

urlpatterns = [
    
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('details/<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('results/<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('votes/<int:question_id>/vote/', views.vote, name='vote'),
]




