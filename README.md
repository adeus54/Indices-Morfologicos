# Indices-Morfolog�cos

### Descripci�n

La herramienta permite calcular la elongaci�n de cuencas, el calculo y la graficaci�n del gradiente de una cuenca en especifico.
Este proyecto se lo realiz� como praticas para Gesti�n Productiva 2.1 a cargo del Ing. Santiago Qui�ones y la informaci�n brindada por parte de la Ing. Mar�a Fernanda Guarderas.

### Librerias

Las librerias utilizadas para desarrollar el proyecto fueron las siguientes:

* Pandas - se encarga del manejo de la data.
* Pyshp - se encarga de leer la data de los .shp
* Arcpy - permite la interaci�n con ArcGis.
* Numpy - operaciones con la data.

### Instalaci�n de librerias

> Nota - Funcional en la versi�n ArcGis 10.5

Al poseer Arcgis 10.5 ingrese en la carpeta donde se instal�.
Busque la carpeta Scripts dentro de ella abra la consola de Windows y escriba la sentencia:

```sh
$ pip install pysys
```

Se instalar� la libreria necesaria para la lectura de los .shp.
Con las dem�s librerias no se necesita hacer eso, debido venir incorporadas en la versi�n de Python 2.7 que es utilizada por el software de ArcGis.

### Maneras de instalar (Herramienta)

* Principal

    * 1 - Descargue el repositorio,
    * 2 - Ingrese a la carpeta y busque el Script "makeaddin" (Este se encarga de compilar todos los archivos necesarios).
    * 3 - Al finalizar el punto anterior se crear� un nuevo archivo ".esriaddin"
    * 4 - De doble click y en la ventana que le aparece, haga click en el bot�n "Instalar". Esto har� que se instale en su ArcMap.

* Alterno
    * 1 - Abra ArcMap y vaya a la secci�n "Customisize".
    * 2 - Ah� de click en "Add-in Manager" y "Options"
    * 3 - Pegue o seleccione la ruta de una capeta que desee usar como almacenador del nuevo archivo.
    * 4 - En el punto 4 enves de darle doble click, copielo a la carpeta de la ruta especificada anteriormente.

### Uso

* Requisitos
    * Los campos de los puntos dentro de los shp, solo pueden tener estos nombres: "X", "Y", "Z".
    * Para el calculo de la elongaci�n el shp de los poligonos de la cuencas debe conteneer el campo "Shape-Area"(Se lo utiliza como identificador).

Para abrir la herramienta de click en un espacio vacio dentro de "Arcmap"(forma m�s rapida) y busque el nombre "MiToolBar"
Se despleglar� un peque�o recuadro con sus respectivos botones para cada calculo.



Al hacer click sobre alguno de ellos se desplegar� una nueva ventana en donde tendra que ingresar los datos solicitados.

> Nota - En el campo "Caracteristicas de salida" debe buscar la carpeta donde quiere que se guarde
> y asignarle un nombre.



Los campos a ingresar varian de acuerdo a cada calculo que desea realiazar:

* En el ingreso de los limites para el calculo del gradiente se recomienda que en el campo "L�mite inferior (Segundo eje)" se ponga una cantidad negativa para evitar el choque de la recta con los bordes.



