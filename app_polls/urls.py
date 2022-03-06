from django.urls import path
from . import views

app_name = 'app_polls'

urlpatterns = [

    # ex: /polls/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /polls/5/
    path('details/<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    path('results/<int:pk>/results/',
         views.ResultsView.as_view(),
         name='results'),
    # ex: /polls/5/vote/
    path('votes/<int:question_id>/vote/', views.vote, name='vote'),
]
