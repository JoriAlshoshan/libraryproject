from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= "books.index"),
    path('list_books/', views.list_books, name= "books.list_books"),
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
    path('aboutus/', views.aboutus, name="books.aboutus"),
    path('html5/links', views.links),
    path('html5/text/formatting', views.formatting),
    path('html5/listing', views.listing),
    path('html5/tables', views.tables),
    path('search', views.search_view, name='search'),
    path('simple/query', views.simple_query, name='simple_query'),
    path('complex/query', views.complex_query, name='complex_query'),
    path('lab8/task1', views.lab8_task1),
    path('lab8/task2', views.lab8_task2),
    path('lab8/task3', views.lab8_task3),
    path('lab8/task4', views.lab8_task4),
    path('lab8/task5', views.lab8_task5),
    path('lab8/task7', views.lab8_task7),

    path('lab9/task1/', views.lab9_task1),
    path('lab9/task2/', views.lab9_task2, name='lab9_task2'),
    path('lab9/task3/', views.lab9_task3, name='lab9_task3'),
    path('lab9/task4/', views.lab9_task4, name='lab9_task4'),
    path('lab9/task5/', views.lab9_task5, name='lab9_task5'),
    path('lab9/task6/', views.lab9_task6, name='lab9_task6'),
    path('lab9_part1/listbooks', views.list_books, name='list_books'),
    path('lab9_part1/addbook', views.add_book, name='add_book'),
    path('lab9_part1/editbook/<int:id>', views.edit_book, name='edit_book'),
    path('lab9_part1/deletebook/<int:id>', views.delete_book, name='delete_book'),
    
    path('lab9_part2/listbooks', views.list_books_form, name='list_books_form'),
    path('lab9_part2/addbook', views.add_book_form, name='add_book_form'),
    path('lab9_part2/editbook/<int:id>', views.edit_book_form, name='edit_book_form'),
    path('lab9_part2/deletebook/<int:id>', views.delete_book_form, name='delete_book_form'),

    path('student-cards/', views.student_card_list, name='student_card_list'),
    path('student-cards/add/', views.add_student_card, name='add_student_card'),

    path('students/', views.student_list, name='student_list'),
    path('students/add/', views.add_student, name='add_student'),
    path('students/update/<int:id>/', views.update_student, name='update_student'),
    path('students/delete/<int:id>/', views.delete_student, name='delete_student'),


    path('students2/', views.student2_list, name='student2_list'),
    path('students2/add/', views.add_student2, name='add_student2'),
    path('students2/update/<int:id>/', views.update_student2, name='update_student2'),
    path('students2/delete/<int:id>/', views.delete_student2, name='delete_student2'),
]

