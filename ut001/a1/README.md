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

En primer lugar, debemos asignar una IP fija en la MV de Ubuntu Server, para poder trabajar de una manera más cómoda y eficaz cada vez que hagamos uso de ésta. 

<br>

![](/img/img002.PNG)

<br>

Asímismo, vamos a añadir la dirección IP de Ubuntu Server y sus dominios en nuestra MV de Ubuntu de la siguiente forma:

~~~
sudo nano /etc/hosts
~~~

![](/img/img001.PNG)

## 2 - Creación de la Página Web

## 3 - Configuración de la Página Web

## ***Conclusiones***. <a name="id5"></a>


