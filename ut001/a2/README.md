<center>

# SERVIDOR WEB - LISTADO DE DIRECTORIOS


</center>

***Nombre:*** Nahuel Ivan Troisi
<br>
***Curso:*** 2º de Ciclo Superior de Administración de Sistemas Informáticos en Red.

### ÍNDICE

+ [Introducción](#id1)
+ [Objetivos](#id2)
+ [Material empleado](#id3)
+ [Desarrollo](#id4)
+ [Conclusiones](#id5)


#### ***Introducción***. <a name="id1"></a>

Aquí explicamos brevemente la parte teórica que tiene que ver con la práctica que se va a realizar

#### ***Objetivos***. <a name="id2"></a>

Aquí explicamos los objetivos que se pretenden alcanzar al realizar la práctica.

#### ***Material empleado***. <a name="id3"></a>

Enumeramos el material empleado tanto hardware como software y las conficuraciones que hacemos (configuraciones de red por ejemplo) 

#### ***Desarrollo***. <a name="id4"></a>

Para crear un listado de directorios, primero deberemos dirigirnos al fichero de configuración "nahuel.me", el cual se encuentra
en "/etc/nginx/sites-avaliable". 

![](img/1.png)

Una vez localizado el archivo, vamos a editarlo, por lo que deberemos añadir las siguientes líneas. 

![](img/2.png)

Como podemos observar, hemos creado otra ruta, la cual hemos definido con el nombre "/shared". 

Una vez realizado este paso, vamos a dirigirnos al directorio "/var/www/html", donde vamos a crear la carpeta "shared", la cual
hace referencia al punto anterior ya que, para que funcione correctamente, deben de tener el mismo nombre. De lo contrario, podrían surgir conflictos. 

![](img/3.png)

Posteriormente, vamos a entrar en la carpeta "shared" y vamos a realizar una serie de enlaces simbólicos hacia las rutas que se muestran a continuación. 

![]/img/4.png)

Ahora vamos a dirigirnos de nuevo al fichero "nahuel.me" y vamos a habilitar el "autoindex". 

![](img/5.png)

Una vez realizado este paso, vamos a reiniciar el servidor de nginx. 

![](img/6.png)

Finalmente, comprobamos que funciona correctamente. 

![](img/7.png)


#### ***Conclusiones***. <a name="id5"></a>

En esta parte debemos exponer las conclusiones que sacamos del desarrollo de la prácica.

