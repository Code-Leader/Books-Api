from django.urls import path

from .views import BookListApiView,\
                   book_list_view,\
                   BookDetailApiView

urlpatterns = [
    path('', BookListApiView.as_view()),
    path('<int:pk>/', BookDetailApiView.as_view(),),
    path(' ', book_list_view)
]