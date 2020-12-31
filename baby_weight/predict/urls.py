from django.urls    import path
from predict        import views

app_name = 'predict'
urlpatterns = [
    path( ''        , views.predict, name= 'index'   ),
    path( 'predict/', views.predict, name= 'predict' ),


]