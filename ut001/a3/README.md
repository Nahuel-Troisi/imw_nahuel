<center>

# SERVIDOR WEB - HOSTS


</center>

***Nombre:*** Nahuel Ivan Troisi 

<br>

***Curso:*** 2º de Ciclo Superior de Administración de Sistemas Informáticos en Red.

## ÍNDICE

+ [Introducción](#id1)
+ [Objetivos](#id2)
+ [Material empleado](#id3)
+ [Desarrollo](#id4)
+ [Conclusiones](#id5)


## ***Introducción***. <a name="id1"></a>

## ***Objetivos***. <a name="id2"></a>

## ***Material empleado***. <a name="id3"></a>

## ***Desarrollo***. <a name="id4"></a>

## Sitio Web 1

En este primer sitio web vamos a crear el servidor "imw.nahuel.me" el cual va a alojar una imágen en su página principal y en un subdirectorio vamos a disponer de un
link a una página web externa. 
En primer lugar vamos a crear el servidor anteriormente mencionado. 

![](img/1.png)

Posteriormente, vamos a editar el archivo de configuración del mismo. 

![](img/2.png)

Una vez realizado, crearemos el enlace simbólico correspondiente.

![](img/3.png)

Comprobamos que se ha realizado correctamente. 

![](img/4.png)

Por otro lado, procedemos a crear el subdirectorio "mec" en el directorio "/var/www/html".

![](img/5.png)

Dentro de dicho directorio, vamos a crear el archivo "index.html", el cual va mostrarnos una portada como la que vemos a continuación. 

![](img/6.png)

Añadimos el sitio web a nuestro directorio de "hosts". 

![](img/7.png)

Reiniciamos el servicio. 

![](img/8.png)

Comprobamos que ha funcionado correctamente.

![](img/9.png)
 
Para terminar, realizamos el mismo proceso de configuración del archivo "index.html" pero esta vez en el directorio "/var/www/html/mec", el cual nos va a
redirigir a un enlace externo. 

![](img/10.png)

Y comprobamos que se ha realizado correctamente. 

![](img/11.png)

## Sitio Web 2

## Sitio Web 3

## Sitio Web 4

## ***Conclusiones***. <a name="id5"></a>
