---
title: "Servicios en Red: Una programación didáctica en espiral"
subtitle: "Todo tiene un comienzo... ¿y un fin?"
description: "Todo tiene un comienzo... ¿y un fin?"
date: 2020-08-04T19:03:00+02:00
lastmod: 2020-08-04T19:03:00+02:00
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
    - /article/servicios-en-red-una-programación-didáctica-en-espiral/
---

Siguiendo la estela del guante lanzado en [esta publicación](https://davidlms.com/article/girando-alrededor-del-aprendizaje-una-programaci%C3%B3n-did%C3%A1ctica-en-espiral/), ha llegado el momento de comenzar **a esbozar una nueva programación** para el módulo Servicios en Red.

Voy a partir de los criterios de evaluación de los distintos resultados de aprendizaje, dividiéndolos primero en **conceptuales** (cosas que el alumnado debe saber) y **procedimentales** (cosas que el alumnado debe saber hacer). Aunque directamente **prefiero hacer la diferenciación entre teóricos (T) y prácticos (P)**. Os sonará muy antiguo todo, pero también queda antiguo ya lo de conceptual y procedimental, y así creo que nos entendemos mucho mejor. A poco que echéis un vistazo a los criterios, os daréis cuenta de que la categorización en un grupo u otro es muy sencilla. Los teóricos **utilizan verbos** como reconocer, identificar, ilustrar, describir…, etc. Los prácticos, por otra parte, usan verbos como instalar, comprobar, verificar, crear, configurar, implementar…, etc. Si no estáis de acuerdo con alguno de los criterios clasificados **siempre podemos discutirlo**.

La otra categorización es más compleja, **ya que es totalmente subjetiva**. Me refiero al peso que va a tener cada criterio en la evaluación: básico, intermedio o avanzado. Si queréis saber por qué lo hago de esta manera, tenéis la explicación completa en [esta publicación](https://davidlms.com/article/evaluar-por-resultados-de-aprendizaje-y-criterios-de-evaluaci%C3%B3n-sin-morir-en-el-intento/). He considerado que la instalación, configuración básica y verificación de cada servicio sería un **criterio básico** y, por lo tanto, mínimo. Una configuración un poco más compleja o un concepto que requiere tener conocimientos básicos de cómo funciona el servicio lo he clasificado como **intermedio**. Los criterios **avanzados** son aquellos que tienen la máxima complejidad y son totalmente complementarios. Esta clasificación está totalmente **abierta al debate**, es más, me ayudaría muchísimo que se discutiera y que todos los docentes que impartimos el módulo estableciésemos un criterio similar, ya que contribuiría a hacer **la evaluación más justa** independientemente del centro educativo en el que estudie el alumnado.

Tenéis **la tabla completa** con todos los criterios clasificados del módulo a continuación:

| Criterio de evaluación | Tipo | Peso propuesto |
|:------:|:------:|:------:|:-------:|
|   1a. Se ha reconocido el funcionamiento de los mecanismos automatizados de configuración de los parámetros de red   |   T   |   B |
|   1b. Se han identificado las ventajas que proporcionan   |   T   |   B |
|   1c. Se han ilustrado los procedimientos y pautas que intervienen en una solicitud de configuración de los parámetros de red   |   T   |   I |
|   1d. Se ha instalado un servicio de configuración dinámica de los parámetros de red   |   P   |   B |
|   1e. Se ha preparado el servicio para asignar la configuración básica a los sistemas de una red local   |   P   |   B |
|   1f. Se han realizado asignaciones dinámicas y estáticas   |   P   |   B |
|   1g. Se han integrado en el servicio opciones adicionales de configuración   |   P   |   I |
|   1h. Se ha verificando la correcta asignación de los parámetros   |   P   |   B |
|   2a. Se han identificado y descrito escenarios en los que surge la necesidad de un servicio de resolución de nombres   |   T   |   B |
|   2b. Se han clasificado los principales mecanismos de resolución de nombres   |   T   |   I |
|   2c. Se ha descrito la estructura, nomenclatura y funcionalidad de los sistemas de nombres jerárquicos   |   T   |   I |
|   2d. Se ha instalado un servicio jerárquico de resolución de nombres   |   P   |   B |
|   2e. Se ha preparado el servicio para almacenar las respuestas procedentes de servidores de redes públicas y servirlas a los equipos de la red local   |   P   |   B |
|   2f. Se han añadido registros de nombres correspondientes a una zona nueva, con opciones relativas a servidores de correo y alias   |   P   |   I |
|   2g. Se ha trabajado en grupo para realizar transferencias de zona entre dos o más servidores   |   P   |   A |
|   2h. Se ha comprobado el funcionamiento correcto del servidor   |   P   |   B |
|   3a. Se ha establecido la utilidad y modo de operación del servicio de transferencia de ficheros   |   T   |   B |
|   3b. Se ha instalado un servicio de transferencia de ficheros   |   P   |   B |
|   3c. Se han creado usuarios y grupos para acceso remoto al servidor   |   P   |   I |
|   3d. Se ha configurado el acceso anónimo   |   P   |   I |
|   3e. Se han establecido límites en los distintos modos de acceso   |   P   |   A |
|   3f. Se ha comprobado el acceso al servidor, tanto en modo activo como en modo pasivo   |   P   |   B |
|   3g. Se han realizado pruebas con clientes en línea de comandos y en modo gráfico   |   P   |   B |
|   4a. Se han descrito los diferentes protocolos que intervienen en el envío y recogida del correo electrónico   |   T   |   B |
|   4b. Se ha instalado un servidor de correo electrónico   |   P   |   B |
|   4c. Se han creado cuentas de usuario y verificado el acceso de las mismas   |   P   |   B |
|   4d. Se han definido alias para las cuentas de correo   |   P   |   I |
|   4e. Se han aplicado métodos para impedir usos indebidos del servidor de correo electrónico   |   P   |   A |
|   4f. Se han instalado servicios para permitir la recogida remota del correo existente en los buzones de usuario   |   P   |   I |
|   4g. Se han usado clientes de correo electrónico para enviar y recibir correo   |   P   |   B |
|   5a. Se han descrito los fundamentos y protocolos en los que se basa el funcionamiento de un servidor web   |   T   |   B |
|   5b. Se ha instalado un servidor web   |   P   |   B |
|   5c. Se han creado sitios virtuales  |   P   |   I |
|   5d. Se han verificado las posibilidades existentes para discriminar el sitio destino del tráfico entrante al servidor   |   P   |   A |
|   5e. Se ha configurado la seguridad del servidor   |   P   |  A  |
|   5f. Se ha comprobando el acceso de los usuarios al servidor   |   P   |   B |
|   5g. Se ha diferenciado y probado la ejecución de código en el servidor y en el cliente   |   P   |   B |
|   5h. Se han instalado módulos sobre el servidor   |   P   |   I |
|   5i. Se han establecido mecanismos para asegurar las comunicaciones entre el cliente y el servidor   |   P   |  A  |
|   6a. Se han descrito métodos de acceso y administración remota de sistemas   |   T   |   B |
|   6b. Se ha instalado un servicio de acceso remoto en línea de comandos   |   P   |   B |
|   6c. Se ha instalado un servicio de acceso remoto en modo gráfico   |   P   |   B |
|   6d. Se ha comprobado el funcionamiento de ambos métodos   |   P   |   B |
|   6e. Se han identificado las principales ventajas y deficiencias de cada uno   |   T   |   I |
|   6f. Se han realizado pruebas de acceso remoto entre sistemas de distinta naturaleza   |   P   |   I |
|   6g. Se han realizado pruebas de administración remota entre sistemas de distinta naturaleza   |   P   |   I |
|   7a. Se ha instalado un punto de acceso inalámbrico dentro de una red local   |   P   |   B |
|   7b. Se han reconocido los protocolos, modos de funcionamiento y principales parámetros de configuración del punto de acceso   |   T   |   B |
|   7c. Se ha seleccionado la configuración más idónea sobre distintos escenarios de prueba   |   P   |   I |
|   7d. Se ha establecido un mecanismo adecuado de seguridad para las comunicaciones inalámbricas   |   P   |   I |
|   7e. Se han usado diversos tipos de dispositivos y adaptadores inalámbricos para comprobar la cobertura   |   P   |   B |
|   7f. Se ha instalado un encaminador inalámbrico con conexión a red pública y servicios inalámbricos de red local   |   P   |   A |
|   7g. Se ha configurado y probado el encaminador desde los ordenadores de la red local   |   P   |   I |
|   8a. Se ha instalado y configurado el hardware de un sistema con acceso a una red privada local y a una red pública   |   P   |   B |
|   8b. Se ha instalado una aplicación que actúe de pasarela entre la red privada local y la red pública   |   P   |   B |
|   8c. Se han reconocido y diferenciado las principales características y posibilidades de la aplicación seleccionada   |   T   |   I |
|   8d. Se han configurado los sistemas de la red privada local para acceder a la red pública a través de la pasarela   |   P   |   I |
|   8e. Se han establecido los procedimientos de control de acceso para asegurar el tráfico que se transmite a través de la pasarela   |   P   |   A |
|   8f. Se han implementado mecanismos para acelerar las comunicaciones entre la red privada local y la pública   |   P   |   A |
|   8g. Se han identificado los posibles escenarios de aplicación de este tipo de mecanismos  |   T   |   I |
|   8h. Se ha establecido un mecanismo que permita reenviar tráfico de red entre dos o más interfaces de un mismo sistema   |   P   |   I |
|   8i. Se ha comprobado el acceso a una red determinada desde los sistemas conectados a otra red distinta   |   P   |   I |
|   8j. Se ha implantado y verificado la configuración para acceder desde una red pública a un servicio localizado en una máquina de una red privada local   |   P   |   I |

Este **es el punto de partida**, y sobre esta base construiremos una nueva programación didáctica. Próximamente en sus mejores dispositivos.

**Actualización**: Ya tenéis disponible la segunda publicación de esta serie [aquí](https://davidlms.com/article/servicios-en-red-una-programaci%C3%B3n-did%C3%A1ctica-en-espiral-ii/) y el desenlace [aquí](https://davidlms.com/article/servicios-en-red-una-programaci%C3%B3n-did%C3%A1ctica-en-espiral-y-iii/).
