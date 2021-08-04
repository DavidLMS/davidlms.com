---
title: "Servicios en Red: Una programación didáctica en espiral (II)"
subtitle: "Ubicando los resultados de aprendizaje en el tiempo"
description: "Ubicando los resultados de aprendizaje en el tiempo"
date: 2020-08-22T10:15:00+02:00
lastmod: 2020-08-22T10:15:00+02:00
draft: false

author: "davidlms.es"

# uBlogger NEW | 1.0.0 Article Update Information
upd: ""

# uBlogger NEW | 1.0.0 Author's comment, is shown above all comments
authorComment: ""

# uBlogger  | 1.2.0 article design theme
theme: ""
# uBlogger NEW | 1.2.0 Allows you to hide the preview image on the article page
hiddenFeaturedImage: false

# uBlogger  | 1.2.0 Post display settings on the page
summaryStyle:
    # uBlogger NEW | 1.1.0 Display previews on the page of posts
    hiddenImage: false
    # uBlogger NEW | 1.1.0 Allows you to hide the description
    hiddenDescription: false
    # uBlogger NEW | 1.1.0 Allows you to hide the title
    hiddenTitle: true
    tags:
      # uBlogger NEW | 1.1.0 One of the options for displaying tags
      theme: "image"
      # uBlogger NEW | 1.1.0 Text color
      color: "white"
      # uBlogger NEW | 1.1.0 Backing color
      background: "black"
      # uBlogger NEW | 1.1.0 Tag transparency
      transparency: 0.9
tags: ['programacion didactica','servicios en red']
categories: ['Propuestas didácticas']
resources:
- name: "featured-image"
  src: "featured-image.jpg"

hiddenFromHomePage: false
hiddenFromSearch: false
twemoji: false

ruby: true
fraction: true
fontawesome: true
linkToMarkdown: true
rssFullText: false

toc:
  enable: false
  auto: true
code:
  copy: true
  # ...
math:
  enable: true
  # ...
mapbox:
  accessToken: ""
  # ...
share:
  enable: true
  # ...
comment:
  enable: true
  # ...
library:
  css:
    # someCSS = "some.css"
    # located in "assets/"
    # Or
    # someCSS = "https://cdn.example.com/some.css"
  js:
    # someJS = "some.js"
    # located in "assets/"
    # Or
    # someJS = "https://cdn.example.com/some.js"
seo:
  images: []
  # ...
aliases:
    - /article/servicios-en-red-una-programación-didáctica-en-espiral-ii/
---
Después de definir el  [objetivo de esta programación](https://davidlms.com/article/girando-alrededor-del-aprendizaje-una-programaci%C3%B3n-did%C3%A1ctica-en-espiral/)  y  [clasificar los criterios de evaluación](https://davidlms.com/article/servicios-en-red-una-programaci%C3%B3n-did%C3%A1ctica-en-espiral/) , toca desglosar en términos generales **a qué vamos a dedicar cada semana**.

Lo ideal hubiese sido **trabajar todos los resultados de aprendizaje en paralelo**, de forma que se fuera profundizando en cada uno de ellos durante el curso. Sin embargo, al tratarse de un grado medio, he pensado que quizás sería demasiado abrumador, por lo que he optado por agrupar los resultados de aprendizaje. De esta forma, se aprenderán en paralelo **un conjunto de los mismos**. Esto no significa que, una vez trabajado un grupo, no se volverán a usar durante el curso. **Las evaluaciones y proyectos están diseñados para que se vayan repasando los contenidos** tratados anteriormente a lo largo de todo el curso escolar.

Para fomentar la evaluación formativa, **se realizarán evaluaciones todas las semanas**. En cada evaluación, un porcentaje se destinará al repaso de algunos de los resultados de aprendizaje previos y otro porcentaje a la evaluación de nuevos criterios.

Creo que es bueno que los alumnos **no trabajen con un solo software para un determinado servicio, ni con un solo sistema operativo**, pero tampoco tiene tantas horas el módulo como para dedicar el tiempo suficiente a ver los más utilizados. Por eso recomiendo **coordinarse con los profesores de otros módulos** como aplicaciones web o sistemas operativos en red. Por ejemplo, en aplicaciones web puede usarse Apache en Windows y en servicios en red usar Nginx en Ubuntu Server. También se puede impartir el módulo de sistemas operativos en red centrado en Windows y el de servicios en red centrado en Linux.

En este caso, **he optado por centrar el módulo en Ubuntu Server**, usando las siguientes aplicaciones:
* OpenSSH y Webmin en el servicio de acceso remoto.
* Vsftpd en el servicio de transferencia de ficheros.
* Nginx en el servicio web.
* Bind9 en el servicio de nombres de dominio.
* Isc-dhcp-server en el servicio de configuración dinámica de la red.
* Postfix y Squirrelmail en el servicio de correo.
* FreeRadius en seguridad de redes inalámbricas.
* Squid como proxy y WireGuard como VPN para la conexión de redes privadas y públicas.

Esto no quiere decir que **puntualmente no utilice otras herramientas y otros sistemas operativos**, así como soluciones de paneles de control de empresas dedicadas al hosting.

A continuación, tenéis una **propuesta de trabajo para cada una de las semanas** del módulo:

| Semana | Contenido |
|:------:|:------:|:------:|:-------:|
|   1   |   Repaso de redes y funcionamiento de Linux   |
|   2   |   Repaso de redes y comandos de Linux*   |
|   3   |   Introducción a SSH, FTP y servicio web   |
|   4   |   Configuración básica de SSH, vsftpd y nginx   |
|   5  |   Acceso remoto y vsftpd avanzado   |
|   6   |   Nginx avanzado   |
|   7   |   Afianzando la teoría (Acceso remoto, servicio de transferencia de ficheros y servicio web)   |
|   8   |   Proyecto de integración (SSH, FTP y servicio web en un hosting)   |
|   9   |   Introducción a DNS y DHCP   |
|   10   |   Configuración básica de bind9 e introducción al servicio de correo   |
|   11   |   Configuración avanzada de bind9 y isc-dhcp-server   |
|   12   |   Configuración avanzada de postfix y squirrelmail   |
|   13   |   Afianzando la teoría (DNS, DHCP y servicio de correo)   |
|   14   |   Introducción a Proxy y VPN con configuración básica de Squid y  WireGuard   |
|   15   |   Configuración avanzada de Squid y WireGuard   |
|   16   |   Introducción e instalación de un servidor Radius   |
|   17   |   Teoría sobre la seguridad en redes inalámbricas   |
|   18   |   Proyecto de repaso - Configuración de servicios en una red local (I)   |
|   19   |   Pruebas de evaluación finales   |
|   20   |   Proyecto de repaso - Configuración de servicios en una red local (II)   |
|   21   |   Recuperación / Proyectos de repaso - Creación de una red con ZeroTier   |

*Normalmente dedico una sola semana al repaso, pero dado que el alumnado de este nivel tuvo una instrucción de emergencia durante el tercer trimestre del pasado curso, he creído conveniente dedicar el doble de tiempo para evitar lagunas que dificulten la asimilación de nuevos contenidos.

El orden y la agrupación de resultados de aprendizaje está realizado en base a **criterios subjetivos**. Si alguien tiene interés especial en eso, podría dar una explicación al respecto.

Me gustaría que aquellos profesores que han impartido el módulo alguna vez, **me comentaran sus opiniones sobre esta distribución temporal, así como formas alternativas de plantearlo**.

Una vez llegados a un consenso aquí, tocará decidir **en cada sesión qué contenido se trabaja y/o qué criterio se evalúa**.

**Actualización**: Ya tenéis disponible el desenlace de esta serie [aquí](https://davidlms.com/article/servicios-en-red-una-programaci%C3%B3n-did%C3%A1ctica-en-espiral-y-iii/).

