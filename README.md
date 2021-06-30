# De0aDjangoREST

Taller para iniciarse en el desarrollo de API REST con Django REST Framework

- Vídeo Parte 1: https://youtu.be/1eQjkdJI9e4
- Vídeo Parte 2: https://youtu.be/B7ehNojsjyk

- Diapositivas Parte 1: https://docs.google.com/presentation/d/1BMlLldDGxuSOZ3WSHzqGhakTpPLD3KzY2ixU25gpeOc/
- Diapositivas Parte 2: https://docs.google.com/presentation/d/1X_pNijQj0DBbR5lYc-pQlECGSSKEtlm5EM5L_uwOMhw/

- Colección de peticiones para importar en Postman: https://drive.google.com/file/d/1SALDsUzpykG9QktJKN8mdYGpteBLJWlW/

Autor Miguel Jiménez - www.migueljimenezgarcia.com


## Step 1 (Inicialización)

 1. Crear Entorno virtual con  `virtualenv .` en la terminal
 
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
        path('v1/cars/', include('cars.urls'))
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
 
 
## Step 11 (Más sobre Modelos)

 1. Definimos un nuevo modelo con más fantasía en `cars/models.py`:
 
    <pre><code>class Car(models.Model):
        created = models.DateTimeField(auto_now_add=True)
        updated = models.DateTimeField(auto_now=True)
        model = models.CharField(max_length=25)
        manufacturing_date = models.DateField()
        brand = models.ForeignKey(
            'Brand',
            related_name='cars',
            on_delete=models.CASCADE
        )
    </code></pre>

 2. Y le añadimos el orden y el índice:

     <pre><code>class Car(models.Model):
     ...
        class Meta:
            ordering = ['updated']
            indexes = [models.Index(fields=['brand'])]</code></pre>
     

 3. Ejecutamos en la terminal

     <pre><code>python manage.py makemigrations
    python manage.py migrate</code></pre>


## Step 12 (Mejorando Serializadores)

 1. Modificamos el serializador en `cars/serializers.py`:

    <pre><code>from rest_framework import serializers
     ...
    class BrandSerializer(serializers.ModelSerializer):
        total_cars = serializers.SerializerMethodField()
        
        class Meta:
            model = Brand
            fields = ('id', 'name', 'total_cars', )
            read_only_fields = ('id', )
    
        def get_total_cars(self, obj):
            return obj.cars.count()</code></pre>

 2. Añadimos un nuevo serializador en `cars/serializers.py`:
 
     <pre><code>...
    from .models import Brand, Car
    ...
    class CarSerializer(serializers.ModelSerializer):
     
        class Meta:
            model = Car
            fields = ('id', 'model', 'brand', 'manufacturing_date', )
            read_only_fields = ('id', )
            extra_kwargs = {
                'manufacturing_date': {'write_only': True},
            }</code></pre>

## Step 13 (Paginación)

 1.Creamos un archivo `cars/paginations.py`:

    from rest_framework.pagination import PageNumberPagination
     
    class SmallResultsSetPagination(PageNumberPagination):
        page_size = 10
        page_query_param = 'page'
         
 2. Abrimos `cars/views.py` y modificamos `BrandListView`:

     <pre><code>from .paginations import SmallResultsSetPagination
    ...
    class BrandListView(ListAPIView):
        serializer_class = BrandSerializer
        permission_classes = ()
        queryset = Brand.objects.all()
        pagination_class = SmallResultsSetPagination</code></pre>

 3. Lo probamos en postman haciendo un GET como http://127.0.0.1:8000/v1/cars/brands/?page=< page-num >, siendo < page-num > el número de la página, quedando para pedir la primera: http://127.0.0.1:8000/v1/cars/brands/?page=1

## Step 14 (Filtros y Orden)

 1. Abrimos `cars/views.py` y modificamos `BrandListView` para introducir los filtros:

     <pre><code>from rest_framework import generics
     from rest_framework import filters as df
     ...
     class BrandListView(generics.ListAPIView):
        serializer_class = BrandSerializer
        permission_classes = ()
        queryset = Brand.objects.all()
        pagination_class = SmallResultsSetPagination
        filter_backends = (df.SearchFilter, )
        search_fields = ('name', )</code></pre>

 2. Seguimos modificando `BrandListView`:

     <pre><code>class BrandListView(generics.ListAPIView):
        serializer_class = BrandSerializer
        permission_classes = ()
        queryset = Brand.objects.all()
        pagination_class = SmallResultsSetPagination
        filter_backends = (df.OrderingFilter, df.SearchFilter, )
        search_fields = ('name', )
        ordering_fields = ('name', )</code></pre>

 3. Lo probamos en postman haciendo un GET de: http://127.0.0.1:8000/v1/cars/brands/?search=< str-search > , siendo < str-search > la cadena por la que se quiere buscar, quedando por ejemplo: http://127.0.0.1:8000/v1/cars/brands/?search=for

 4. Y combinandolo: http://127.0.0.1:8000/v1/cars/brands/?page=1&search=olks

## Step 15 (Vistas Conjuntas)

  ### Obtener y Crear Recursos (GET y POST)

   1. En `cars/views.py` introducimos:

    from .models import Brand, Car
    ...
    from .serializers import BrandSerializer, CarSerializer
    ...
    class CarListCreateView(generics.ListCreateAPIView):
        serializer_class = CarSerializer
        permission_classes = ()
        queryset = Car.objects.all()
        pagination_class = SmallResultsSetPagination
        filter_backends = (df.OrderingFilter, df.SearchFilter, )
        search_fields = ('model', )
        ordering_fields = ('model', )

   2. Y en `cars/urls.py` introducimos:
 
     from . import views
	 urlpatterns = [
        ...
        path('cars/', views.CarListCreateView.as_view(), name='cars'),
    ]

   3. Y lo probamos haciendo GET y POST de: http://127.0.0.1:8000/v1/cars/cars/

  ### Obtener, Editar, Eliminar un Recurso (GET, PUT/PATCH y DELETE)

   1. En `cars/views.py` introducimos:

    class CarRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
        serializer_class = CarSerializer
        permission_classes = ()
        queryset = Car.objects.all()
        lookup_field = 'id'

   2. Y en `cars/urls.py` introducimos:

    urlpatterns = [
        ...
        path('cars/<int:id>/', views.CarRetrieveUpdateDestroyView.as_view(), name='car'),
    ]


   3. Y lo probamos haciendo GET, PATCH y DELETE de: http://127.0.0.1:8000/v1/cars/cars/< id >/ , siendo id por ejemplo 1


## Step 16 (Permisos)

 1. Entramos en `cars/views.py`:

     <pre><code>from rest_framework.permissions import IsAuthenticated
     
    class BrandCreateView(generics.CreateAPIView):
        ...
        permission_classes = (IsAuthenticated, )
        ...</code></pre>



## Step 17 (Oauth2)

Recordad que hay que tener el virtualenv activo: `source bin/activate`

 1. Abrimos requirements.pip que está en la carpeta principal e incluimos:

     <pre><code>django-oauth-toolkit==1.3.2</code></pre>

 2. Y volvemos a instalar los módulos introduciendo en la terminal:

     <pre><code>pip install -r requirements.pip</code></pre>

 3. Abrimos De0aDjangoREST/settings.py y cambiamos:

     <pre><code>INSTALLED_APPS = [
        'django.contrib.admin',
        ...
        'rest_framework',
        'cars',
        'oauth2_provider',
    ] </code></pre>

 4. Abrimos De0aDjangoREST/settings.py y cambiamos:


     <pre><code>REST_FRAMEWORK = {
        ...
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
        ),
        'DEFAULT_PERMISSION_CLASSES': (
            'rest_framework.permissions.IsAuthenticated',
        )
    }
    ...
    OAUTH2_PROVIDER = {
        'SCOPES': {'read': 'Read scope', 'write': 'Write scope'}
    }</code></pre>

 5. Abrimos De0aDjangoREST/urls.py y cambiamos:

     <pre><code>from django.conf.urls import include
     
    urlpatterns = [
         ...
        path('v1/o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    ]</code></pre>

 6. Corremos las nuevas migraciones para usar oauth2 ejecutando en la terminal:

     <pre><code>python manage.py migrate</code></pre>

 7. Abrimos la shell de django (Recordad que hay que tener el virtualenv activo: `source bin/activate`):

     <pre><code>python manage.py shell</code></pre>


8. Introducimos en la shell de Django:

     <pre><code>from oauth2_provider.models import get_application_model
     Application = get_application_model()
     Application.objects.create(
        name="Application",
        client_type=Application.CLIENT_CONFIDENTIAL,
        authorization_grant_type=Application.GRANT_PASSWORD,
    )
    vars(Application.objects.first())
    quit()</code></pre>

Y copiamos el client id y el secret id

9. Creamos un superuser:

     <pre><code>python manage.py createsuperuser</code></pre>

10. Obtenemos el token desde postman o haciendo: 

<pre><code>curl -X POST -d "grant_type=password&username=< user_name >&password=< password >" -u"< client_id >:< client_secret >" http://localhost:8000/v1/o/token/</code></pre>
   Sustituyendo los campose entre <> por los datos correspondientes.

12. A partir de aquí, para validar el usuario habra que meter una cabecera en las peticiones con el token que nos devuelve.

`Authorization: Bearer <your_access_token>`

Más info: https://django-oauth-toolkit.readthedocs.io/en/latest/rest-framework/getting_started.html


## Step 18 (Testing)

Recordad que hay que tener el virtualenv activo: `source bin/activate`

 1. Abrimos requirements.pip que está en la carpeta principal e incluimos:

     <pre><code>model_bakery==1.1.1</code></pre>

2. Y volvemos a instalar los módulos ejecutando en la terminal:

     <pre><code>pip install -r requirements.pip</code></pre>

 3. Abrimos `cars/test.py`

     <pre><code>from model_bakery import baker
    from rest_framework import status
    from rest_framework.test import APITestCase
     
    from django.urls import reverse
     
     
    class GetBrandsTest(APITestCase):
    """ Test module for GET brands """ 
        def setUp(self):
            self.brands = []
            self.brands.append(baker.make('cars.Brand', name='a'))
            self.brands.append(baker.make('cars.Brand', name='b'))
            self.brands_counter = len(self.brands)
            self.url = reverse('brands')
            
        def test_get_brands_valid(self):
            response = self.client.get(self.url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(len(response.data['results']), self.brands_counter)
            self.assertEqual(response.data['results'][0]['id'], self.brands[0].id)
            self.assertEqual(response.data['results'][1]['id'], self.brands[1].id) </code></pre>

4. Ejecuta los tests en la terminal:

     <pre><code>python manage.py test</code></pre>


No todo en la vida es tan fácil como en este workshop, para seguir aprendiendo: https://www.django-rest-framework.org/api-guide/generic-views/

Y algo más de testing:

- https://docs.djangoproject.com/en/3.1/topics/testing/
- https://www.django-rest-framework.org/api-guide/testing/
- https://model-bakery.readthedocs.io/
