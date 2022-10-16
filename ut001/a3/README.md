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

Dentro de dicho directorio, vamos a crear el archivo "index.html", el cual va a mostrarnos una portada con una imágen resumen de la asignatura de IMW. 

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

Respecto al segundo sitio web, éste nos mostrará un listado de archivos del directorio "/var/lib", por lo que, al igual que en el caso anterior vamos a comenzar
por configurar el servidor. 

![](img/12.png)

** Ojo, que hay que hacer uso del "autoindex" para que funcione **

Una vez realizado este paso, añadimos la página al listado de hosts y reiniciamos el servicio para comprobar que funciona. 

![](img/13.png)

## Sitio Web 3

En el caso del tercer sitio web, este va a alojar un listado de los alumnos de 2º de ASIR, asi como los puestos en los que se encuentran, pero para poder acceder, se
necesita conocer un usuario y contraseña determinado. 
Para ello, vamos a definir los siguientes parámetros en el archivo de configuración del servidor. 

![](img/14.png)

Posteriormente, vamos a encriptar la clave de acceso, la cual es "2asir". 

![](img/15.png)

Vamos a añadir dicha clave al archivo ".htpasswd", el cual se aloja en el directorio "/var/www/html/students".

![](img/16.png)

Dentro del mismo directorio, vamos a configurar el "index.html" con el listado de los alumnos.

![](img/17.png)

Creamos el enlace simbólico correspondiente. 

![](img/18.png)

Comprobamos que se ha realizado correctamente.

![](img/19.png)

Añadimos el sitio web a nuestro directorio de "hosts". 

![](img/20.png)

Comprobamos que podemos acceder al sitio web y que dispone de autenticación. 

![](img/21.png)

Si accedemos al mismo, podremos ver el listado de alumnos y los puestos que ocupan. 

![](img/22.png)

## Sitio Web 4

En este último sitio web vamos a crear una página que posea una serie de redirecciones, para que en caso de errores tipográficos o actualizaciones de nombres se pueda 
acceder a la web sin problema. 
Es por ello que vamos a configuraralo de la siguiente manera.

![](img/23.png)

Como podemos observar, hemos configurado tres redirecciones diferentes, asi como los "access_log" y "error_log", los cuales veremos más adelante. 

Posteriormente, añadimos la página a nuestro archivo de "hosts".

![](img/24.png)

Creamos el enlace simbólico al igual que en los casos anteriores y comprobamos que se ha realizado correctamente. 

![](img/25.png)

Accedemos a la web para comprobar que carga correctamente el "index.html" y sus respectivas configuraciones. 

![](img/26.png)

Movemos los archivos "error_log" y "access_log" al directorio "/var/log/nginx/redirect", el cual hay que crear manualmente dado que no existe por defecto. 

![](img/27.png)

Finalmente, añadimos el sitio web de redireccionamiento al archivo "hosts" y comprobamos que se hacen las redirecciones correctamente. 

![](img/28.png)

## ***Conclusiones***. <a name="id5"></a>
