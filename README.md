# De0aDjangoREST

Taller para iniciarse en el desarrollo de API REST con Django REST Framework

Autor Miguel Jiménez - www.migueljimenezgarcia.com


## Step 1 (Inicialización)

 1. Crear Entorno virtual con  `virtualenv De0aDjangoREST` en la terminal
 
 2. Entrar en la carpeta De0aDjangoREST
 
 3. Activar el virtualenv con `source bin/activate` en la terminal
 
 4. Crear archivo requirements.pip en esta carpeta con:

    <pre><code>Django==3.0.1
    djangorestframework==3.10.3
    ipdb==0.11</code></pre>

 5. Introducir `pip install -r requirements.pip` en la terminal

## Step 2 (Proyecto)

 1. Inicializamos el proyecto con `django-admin startproject De0aDjangoREST` en la terminal
 
 2. Entramos en la carpeta del proyecto llamada `De0aDjangoREST` que se acaba de crear y trabajaremos sobre esta todo lo que queda del workshop

## Step 3 (App)

 1. Creamos la app dentro del proyecto con `python manage.py startapp cars` en la terminal

## Step 4 (Settings y Urls)

 1. Abrir `De0aDjangoREST/settings.py` y modificar:
 
    <pre><code>INSTALLED_APPS = [
        ...
        'rest_framework',
        'cars',
    ]</code></pre>

 2. Seguimos en De0aDjangoREST/settings.py y añadimos al final:
 
     <pre><code>REST_FRAMEWORK = {
	     'DEFAULT_PERMISSION_CLASSES': [
            'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
        ]
    }</code></pre>

 3. Abrir `De0aDjangoREST/urls.py`, borrarlo e introducir:

    <pre><code>from django.urls import path
    from django.conf.urls import include
    
    
    urlpatterns = [
        path('v1/cars/', include(cars.urls'))
    ]</code></pre>

 4. Crear `cars/urls.py` y añadir:

    <pre><code>from django.urls import path
    
    
    urlpatterns = [
    ]</code></pre>

 5. Inicializamos el servidor con `python manage.py runserver`en la terminal
 
 6. Entramos en el navegador en [http://127.0.0.1:8000/](http://127.0.0.1:8000/) para comprobar que funcione todo hasta ahora

## Step 5 (Modelo y base de datos)

 1. Abrir cars/models.py e introducimos el primer modelo:

    <pre><code>class Brand(models.Model):
        created = models.DateTimeField(auto_now_add=True)
        updated = models.DateTimeField(auto_now=True)
        name = models.CharField(max_length=15)</code></pre>

 2. Creamos las migraciones para la base de datos con `python manage.py makemigrations` en la terminal
 
 3. Corremos las migraciones con `python manage.py migrate` en la terminal y así reflejamos los cambios en los modelos en la base de datos.

## Step 6 (Petición GET, obtener recursos)

 1. Definimos el Serializador en `cars/serializers.py`
 
    <pre><code>from rest_framework import serializers
    
    from .models import Brand
    
    
    class BrandSerializer(serializers.ModelSerializer): 
        class Meta:
            model = Brand
            fields = ('id', 'name', )</code></pre>

 2. Definimos la Vista en `cars/views.py`
 
    <pre><code>from rest_framework.generics import ListAPIView
    
    from .models import Brand
    
    from .serializers import BrandSerializer
    
    
    class BrandListView(ListAPIView):
        serializer_class = BrandSerializer
        permission_classes = ()
        queryset = Brand.objects.all()</code></pre>
 
 3. Definimos URL en `cars/urls.py`

    <pre><code>from django.urls import path
    
    from .views import BrandListView
    
    
    urlpatterns = [
        path('brands/', BrandListView.as_view(), name='brands'),
    ]</code></pre>

 4. Comprobar en [http://127.0.0.1:8000/v1/cars/brands/](http://127.0.0.1:8000/v1/cars/brands/)

## Step 7 (Petición POST, crear un recurso)

 1. Definimos Vista en `cars/views.py`
 
    <pre><code>from rest_framework.generics import CreateAPIView, ListAPIView
    ...
    class BrandCreateView(CreateAPIView):
        serializer_class = BrandSerializer
        permission_classes = ()</code></pre>

 2. Definimos URL en `cars/urls.py`
 
    <pre><code>from django.urls import path
     
    from .views import BrandCreateView, BrandListView
    
    
    urlpatterns = [
        path('brands/', BrandListView.as_view(), name='brands'),
        path('brands/create/', BrandCreateView.as_view(), name='brand_create'),
    ]</code></pre>

 3. Usar postman u otro cliente http para lanzar un POST al endpoint [http://127.0.0.1:8000/v1/cars/brands/create/](http://127.0.0.1:8000/v1/cars/brands/create/), con la variable name inicializada en el payload de un form-data.

## Step 8 (Petición GET, obtener un recurso)

 1. Definimos Vista en `cars/views.py`
 
    <pre><code>from rest_framework.generics import (CreateAPIView, ListAPIView,
                                         RetrieveAPIView)
    ...
    class BrandRetrieveView(RetrieveAPIView):
        serializer_class = BrandSerializer
        permission_classes = ()
        queryset = Brand.objects.all()
        lookup_field = 'id'</code></pre>

 2. Definimos URL en `cars/urls.py`
 
    <pre><code>from django.urls import path
    
    from .views import BrandCreateView, BrandListView, BrandRetrieveView
    
    
    urlpatterns = [
        path('brands/', BrandListView.as_view(), name='brands'),
        path('brands/create/', BrandCreateView.as_view(), name='brand_create'),
        path('brands/< int:id >/', BrandRetrieveView.as_view(), name='brand'),
    ]</code></pre>

 3. Desde el navegador o postman lanzar un GET al endpoint [http://127.0.0.1:8000/v1/cars/brands/1/](http://127.0.0.1:8000/v1/cars/brands/1/)

## Step 9 (Petición PUT/PATCH, modificar un recurso)
 1. Definimos Vista en `cars/views.py`
 
    <pre><code>from rest_framework.generics import (CreateAPIView, ListAPIView,
                                         RetrieveAPIView, UpdateAPIView)
    ...
    class BrandUpdateView(UpdateAPIView):
        serializer_class = BrandSerializer
        permission_classes = ()
        queryset = Brand.objects.all()
        lookup_field = 'id'</code></pre>

 2. Definimos URL en `cars/urls.py`
 
    <pre><code>...
    from .views import (BrandCreateView, BrandListView,
                        BrandRetrieveView, BrandUpdateView)
    
    
    urlpatterns = [
        ...
        path('brands/< int:id >/update/', BrandUpdateView.as_view(), name='brand_update'),
    ]</code></pre>

 3. Usar postman para lanzar un PUT o PATCH al endpoint [http://127.0.0.1:8000/v1/cars/brands/1/](http://127.0.0.1:8000/v1/cars/brands/1/)  con la variable name inicializada en el payload de un form-data

## Step 10 (Petición DELETE, eliminar un recurso)
 1. Definimos Vista en `cars/views.py`
 
    <pre><code>from rest_framework.generics import (CreateAPIView, DestroyAPIView, ListAPIView,
                                         RetrieveAPIView, UpdateAPIView)
    …
    class BrandDestroyView(DestroyAPIView):
        permission_classes = ()
        queryset = Brand.objects.all()
        lookup_field = 'id'</code></pre>

 2. Definimos URL en `cars/urls.py`
 
    <pre><code>...
    from .views import (BrandCreateView, BrandDestroyView, BrandListView,
                        BrandRetrieveView, BrandUpdateView)

    urlpatterns = [
        ...
        path('brands/< int:id >/delete/', BrandDestroyView.as_view(), name='brand_delete'),
    ]</code></pre>

 3. Usar postman para lanzar un DELETE al endpoint [http://127.0.0.1:8000/v1/cars/brands/3/delete/](http://127.0.0.1:8000/v1/cars/brands/3/delete/)
