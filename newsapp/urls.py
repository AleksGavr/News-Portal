from django.urls import path
# Импортируем созданное нами представление
from .views import PostsList, PostDetail


urlpatterns = [
   # path — означает путь.
   # Путь ко всем постам остается пустым
   # Т.к. наше объявленное представление является классом,
   # а Django ожидает функцию, нам надо представить этот класс в виде view.
   # Для этого вызываем метод as_view.
   path('', PostsList.as_view()),
   # pk - первичный ключ поста, который будут выводится в шаблон
   # int - целочисленное значение
   path('<int:pk>', PostDetail.as_view())
]