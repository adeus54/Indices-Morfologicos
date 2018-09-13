# Indices-Morfologícos

### Descripción

La herramienta permite calcular la elongación de cuencas, el calculo y la graficación del gradiente de una cuenca en especifico.
Este proyecto se lo realizó como praticas para Gestión Productiva 2.1 a cargo del Ing. Santiago Quiñones y la información brindada por parte de la Ing. María Fernanda Guarderas.

### Librerias

Las librerias utilizadas para desarrollar el proyecto fueron las siguientes:

* Pandas - se encarga del manejo de la data.
* Pyshp - se encarga de leer la data de los .shp
* Arcpy - permite la interación con ArcGis.
* Numpy - operaciones con la data.

### Instalación de librerias

> Nota - Funcional en la versión ArcGis 10.5

Al poseer Arcgis 10.5 ingrese en la carpeta donde se instaló.
Busque la carpeta Scripts dentro de ella abra la consola de Windows y escriba la sentencia:

```sh
$ pip install pysys
```

Se instalará la libreria necesaria para la lectura de los .shp.
Con las demás librerias no se necesita hacer eso, debido venir incorporadas en la versión de Python 2.7 que es utilizada por el software de ArcGis.

### Maneras de instalar (Herramienta)

* Principal

    * 1 - Descargue el repositorio,
    * 2 - Ingrese a la carpeta y busque el Script "makeaddin" (Este se encarga de compilar todos los archivos necesarios).
    * 3 - Al finalizar el punto anterior se creará un nuevo archivo ".esriaddin"
    * 4 - De doble click y en la ventana que le aparece, haga click en el botón "Instalar". Esto hará que se instale en su ArcMap.

* Alterno
    * 1 - Abra ArcMap y vaya a la sección "Customisize".
    * 2 - Ahí de click en "Add-in Manager" y "Options"
    * 3 - Pegue o seleccione la ruta de una capeta que desee usar como almacenador del nuevo archivo.
    * 4 - En el punto 4 enves de darle doble click, copielo a la carpeta de la ruta especificada anteriormente.

### Uso

* Requisitos
    * Los campos de los puntos dentro de los shp, solo pueden tener estos nombres: "X", "Y", "Z".
    * Para el calculo de la elongación el shp de los poligonos de la cuencas debe conteneer el campo "Shape-Area"(Se lo utiliza como identificador).

Para abrir la herramienta de click en un espacio vacio dentro de "Arcmap"(forma más rapida) y busque el nombre "MiToolBar"
Se despleglará un pequeño recuadro con sus respectivos botones para cada calculo.



Al hacer click sobre alguno de ellos se desplegará una nueva ventana en donde tendra que ingresar los datos solicitados.

> Nota - En el campo "Caracteristicas de salida" debe buscar la carpeta donde quiere que se guarde
> y asignarle un nombre.



Los campos a ingresar varian de acuerdo a cada calculo que desea realiazar:

* En el ingreso de los limites para el calculo del gradiente se recomienda que en el campo "Límite inferior (Segundo eje)" se ponga una cantidad negativa para evitar el choque de la recta con los bordes.



