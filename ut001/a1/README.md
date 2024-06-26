<center>

# SERVIDOR WEB - MIS SERIES FAVORITAS


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

En esta práctica vamos a crear un sevidor web con la herramienta de Nginx y en ella vamos a alojar distintos servicios, entre ellos, una página web. 

## ***Objetivos***. <a name="id2"></a>

La finalidad de dicha práctica es conseguir crear la página web y alojar cierta información en la misma. En nuestro caso, vamos a crear un listado de
nuestras series favoritas, con sus respectivas carátulas y si hacemos click en las imágenes, nos redigirá a una página web donde podemos encontrar
información sobre ésta. 

## ***Material empleado***. <a name="id3"></a>

En este caso, vamos a hacer uso de tres máquinas virtuales, una con Ubuntu, otra con Ubuntu Server y la última será con Kali Linux 
(aunque en el caso de ésta última se puede utilizar cualquier otra si se desea).
En la MV de Ubuntu Server vamos a configurar y administrar nuestro servidor web, además de crear la página web.
Respecto a la MV de Ubuntu, la usaremos para conectarnos por SSH a la MV de Ubuntu Server para poder hacer la instalación y configuración del servidor
de una manera más dinámica, además de poder hacer las comprobaciones pertinentes al contar con entorno gráfico. 
Por otro lado, la máquina de Kali Linux nos servirá para poder detallar toda la documentación necesaria para elaborar el informe sobre la misma. 

## ***Desarrollo***. <a name="id4"></a>

## 1 - Configuración del Servidor Web

Primero que nada, partimos de haber descargado previamente Nginx, pero antes de nada deberemos hacer una serie de configuraciones.

<br>

En primer lugar, debemos asignar una IP fija en la MV de Ubuntu Server, para poder trabajar de una manera más cómoda y eficaz cada vez que hagamos uso de ésta. Por lo
que vamos a dirigirnos al siguiente directorio para editar el archivo de configuración.

~~~
/etc/netplan
~~~

Y procedemos a configurar el fichero de la siguiente manera:

<br>

![](img/img002.PNG)

<br>

Asímismo, vamos a añadir la dirección IP de Ubuntu Server y sus dominios en nuestra MV de Ubuntu de la siguiente forma:

~~~
sudo nano /etc/hosts
~~~

<br>

![](img/img001.PNG)

<br>

Una vez configurado este apartado, procedemos a crear un nuevo servidor, pero debemos hacerlo en la siguiente ruta:

~~~
/etc/nginx/sites-avaliable
~~~

En nuestro caso, se llamará ***"nahuel.me"***, pero puedes ponerle el nombre que gustes. Finalmente, debería quedar configurado de la siguiente forma:

<br>

![](img/img003.PNG)

<br>

![](img/img004.PNG)

<br>

Una vez realizado este paso, vamos a crear un enlace simbólico en la carpeta ***sites-enabled*** mediante el comando ***ln -s*** , quedando de la siguiente manera:

<br>

~~~
sudo ln -s ../sites-avaliable/nahuel.me
~~~

***Ojo, porque hay que encontrarse dentro de la ruta "sites-enabled"*** 

<br>

Si hemos realizado el paso correctamente, debería de resaltar con otro color, azul en nuestro caso. 

<br>

![](img/img005.PNG)


## 2 - Creación de la Página Web

En este punto, vamos a dirigirnos a la siguiente ruta:

~~~
/var/www/html
~~~

Aqui es donde se almacenan todas la configuraciones de las distintas páginas web que nosotros vayamos a crear, organizadas por carpetas. En nuestro caso, vamos a
crear la carpeta ***"series"*** y dentro de la misma vamos a crear el archivo ***"index.html"*** con el que vamos a darle forma y color a nuestra página web. 

<br>

![](img/img006.PNG)

<br>

![](img/img007.PNG)

## 3 - Configuración de la Página Web

Para concluir, en este archivo ***html*** vamos a configurar nuestra página web, donde vamos a añadir cinco series que más nos gusten, con la condición de que
al hacer click en la imágen, ésta nos redirija a una página web externa que nos proporcione información sobre la misma (número de temporadas, capítulos, sinopsis,
etc...).

<br>

![](img/img008.PNG)

<br>

Una vez terminado, debería quedar algo así:

<br>

![](img/resultado.gif)

## ***Conclusiones***. <a name="id5"></a>
En esta práctica hemos podido aprender lo sencillo que puede ser alojar una página web en un servidor y poder acceder a la misma desde distintos dispositivos,
así como crear infinidad de servidores web para distintos usos con muy pocos recursos, algo bastante parecido a lo que nos podemos encontrar en el aula
como es el caso de "Leela". 

