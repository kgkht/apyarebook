from django.urls import path, include
from .views import ebook_category, ebook_series, ebook_home, ebook_detail, single_serie, single_category

app_name = 'ebooks'

urlpatterns = [
    path('', ebook_home , name='ebookhome'),
    path('category/', ebook_category, name='category'),
    path('category/<int:category_id>/', single_category, name='singlecategory'),
    path('popularbooks/', ebook_category, name='popularbooks'),
    path('series/', ebook_series, name='series'),
    path('series/<int:serie_id>/', single_serie, name='singleserie'),
    path('<int:book_id>/', ebook_detail, name='bookpost'),
]
