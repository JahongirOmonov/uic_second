from django.urls import path
from polls import views

urlpatterns = [
    # path('OperatonFilter/', views.OperationFilter.as_view()),
    path('StudentListView/', views.StudentListView.as_view()),
    path('StudentDetailView/<int:pk>', views.StudentDetailView.as_view()),
    path('StudentEdit/<int:pk>', views.StudentEdit.as_view()),
    path('StudentCreate/', views.StudentCreate.as_view()),
    path('InvestorListView/', views.InvestorListView.as_view()),
    path('InvestorEdit/<int:pk>', views.InvestorEdit.as_view()),
    path('InvestorCreate/', views.InvestorCreate.as_view()),
    path('InvestorDetailView/<int:pk>', views.InvestorDetailView.as_view()),
    path('OperationListView/', views.OperationListView.as_view())

]