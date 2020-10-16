---
title: "Cloudflare y su servicio gratuito parar mejorar la disponibilidad de tu web"
date: 2020-10-16T18:00:00+02:00
description: "¿Cómo ha mejorado el rendimiento del blog?"
images:
- featuredimage.jpg

twitter:
  card: "summary"
  site: "@handle"
  title: "Cloudflare y su servicio gratuito parar mejorar la disponibilidad de tu web"
  description: "¿Cómo ha mejorado el rendimiento del blog?"
  image: "https://davidlms.com/article/cloudflare-y-su-servicio-gratuito-parar-mejorar-la-disponibilidad-de-tu-web/featuredimage.jpg"

tags: ['cloudflare', 'CDN', 'DDoS', 'Blog', 'pingdom', 'pagespeed']
categories: ['Recursos']
author: "David Romero"
noSummary: true

resizeImages: false
---
Desde que comencé el blog he sido transparente en lo que respecta a la parte técnica del mismo, y de hecho tenéis la sección [Cómo se hace](https://davidlms.com/page/como-se-hace/) **totalmente actualizada**.

Esta semana he dado de alta el dominio en el **servicio gratuito de **[Cloudflare](https://www.cloudflare.com/es-es/) para mejorar la **disponibilidad** de la web. ¿Quieres saber en qué consiste, cómo lo he hecho y qué cambios he observado? Sigue leyendo.

Cloudflare es una empresa estadounidense que ofrece varios servicios en internet. Entre ellos, dos de forma gratuita, que son el [CDN](https://www.cloudflare.com/es-es/cdn/) y la [mitigación de ataques DDoS](https://www.cloudflare.com/es-es/ddos/). Un **CDN** es una red de entrega de contenido. Simplificando, son varios servidores repartidos geográficamente de forma estratégica que almacenan tu sitio web, por lo que se mejora la rapidez (cuando hay un acceso, se le deriva al servidor más cercano) y la disponibilidad (es menos probable que el sitio deje de estar online si está replicado en varios servidores). Un **ataque DDoS**, simplificando también, se produce cuando varios dispositivos (muchos) realizan múltiples peticiones a un servidor o red concreta, con el objetivo de saturarlo y que deje de estar disponible.

Antes de activar el servicio, voy a realizar **algunas pruebas de rendimiento previo**, para poder comprobar si mejora posteriormente. Es importante recalcar que, dependiendo del estado de la red y otros factores, las pruebas pueden variar continuamente, así que solamente serán una estimación.

La primera prueba la realizaré con **el servicio **[PageSpeed Insights](https://developers.google.com/speed/pagespeed/insights/?hl=es) de Google. El resultado es una puntuación de **88/100 en el rendimiento de la web en un ordenador** y **una puntuación de 64/100 en un móvil**. Puedes acceder a los detalles de estos análisis en los siguientes enlaces:

* [Análsis de PageSpeed en un ordenador antes de activar Cloudflare](https://davidlms.github.io/ArchivosBlog/PageSpeed_antes_cloudfare_ordenador.html)
* [Análsis de PageSpeed en un móvil antes de activar Cloudflare](https://davidlms.github.io/ArchivosBlog/PageSpeed_antes_cloudfare_movil.html)

La segunda prueba la realizaré usando **el servicio **[Pingdom Website Speed Test](https://tools.pingdom.com/), que nos permite calcular el **tiempo de carga** del blog desde distintas ciudades del mundo. Tenéis un resumen de los resultados en la siguiente tabla:

| Región | Rendimiento | Tiempo de carga | Detalle |
|:------:|:------:|:------:|:------:|
|   Asia - Japón - Tokyo   |   86  | 4.53s | [link](https://tools.pingdom.com/#5d478cb750400000) |
|   Europa - Alemania - Frankfurt   |   86  | 328ms |  [link](https://tools.pingdom.com/#5d478d3443400000) |
|   Europa - Reino Unido - Londres  |   86  | 547ms |  [link](https://tools.pingdom.com/#5d478d4cca800000) |
|   América del Norte - EE.UU. - Washington D.C   |   86  | 458ms |  [link](https://tools.pingdom.com/#5d478d6612800000) |
|   América del Norte - EE.UU. - San Francisco   |   86  | 548ms |  [link](https://tools.pingdom.com/#5d478dfc36c00000) |
|   Oceanía - Australia - Sídney   |   86  | 3.95s |  [link](https://tools.pingdom.com/#5d478e1b38400000) |
|   América del Sur - Brasil - São Paulo   |   86  | 1.24s |  [link](https://tools.pingdom.com/#5d478e42d0800000) |

**El rendimiento medio en Pingdom es 86 y el tiempo medio de carga es de 1.66 segundos**.

A continuación, realizaré el procedimiento gratuito de activación de los servicios de Cloudflare. ¿Quieres saber cómo lo he hecho paso a paso? Consulta el siguiente enlace:
[Paso a paso de activación de un dominio en Cloudflare](https://davidlms.github.io/Presentaciones-HTML/cloudflare/cloudflare.html)

Ahora volveremos a realizar **el mismo análisis anterior**, para conocer cómo ha variado el rendimiento y la velocidad de carga del blog.

El resultado en PageSpeed es **una puntuación de 98/100 en el rendimiento de la web en un ordenador** y **una puntuación de 87/100 en un móvil**. Puedes acceder a los detalles de estos análisis en los siguientes enlaces:

* [Análsis de PageSpeed en un ordenador después de activar Cloudflare](https://davidlms.github.io/ArchivosBlog/PageSpeed_despues_cloudfare_ordenador.html)
* [Análsis de PageSpeed en un móvil después de activar Cloudflare](https://davidlms.github.io/ArchivosBlog/PageSpeed_despues_cloudfare_movil.html)

En la siguiente tabla tenéis el resumen de los análisis realizados en Pingdom:

| Región | Rendimiento | Tiempo de carga | Detalle |
|:------:|:------:|:------:|:------:|
|   Asia - Japón - Tokyo   |   83  | 1.75s | [link](https://tools.pingdom.com/#5d4983bda7800000) |
|   Europa - Alemania - Frankfurt   |   81  | 1.51s |  [link](https://tools.pingdom.com/#5d4984116c400000) |
|   Europa - Reino Unido - Londres  |   83  | 2.18 |  [link](https://tools.pingdom.com/#5d49844952c00000) |
|   América del Norte - EE.UU. - Washington D.C   |   83  | 736ms |  [link](https://tools.pingdom.com/#5d49846c21400000) |
|   América del Norte - EE.UU. - San Francisco   |   83  | 227ms |  [link](https://tools.pingdom.com/#5d49848a69400000) |
|   Oceanía - Australia - Sídney   |   83  | 1.09s |  [link](https://tools.pingdom.com/#5d4984a7fbc00000) |
|   América del Sur - Brasil - São Paulo   |   83  | 3.00s |  [link](https://tools.pingdom.com/#5d4984c4b8800000) |

**El rendimiento medio en Pingdom es 82.71 y el tiempo medio de carga es de 1.5 segundos**.

Vemos que **las puntuaciones en PageSpeed han mejorado considerablemente**, y eso es muy positivo para el blog, ya que es uno de los factores a considerar para situarlo en el buscador de Google. En Pingdom, **aunque el tiempo medio de carga es menor**, sí me ha llamado la atención que ahora **el tiempo de carga de las ciudades de Europa y América del Sur es más lento** que antes de activar el servicio. Es una pena, ya que la mayor parte de las visitas vienen de estas regiones. **Pero hay un detalle importante**. En Cloudflare aparece la siguiente imagen:

![Diagrama en Cloudflare sobre el tiempo de carga](/cargacloudflare.png)

El tiempo de carga total con Cloudflare es más lento, sin embargo, **se muestra contenido parcial más rápidamente**. ¿Y no es la pantalla en blanco lo que nos agobia? ¿No preferimos comprobar antes que la página se está cargando? **¿Qué posibilidades hay de que alguien abandone una web que está tratando de visitar una vez se ha cargado “algo”?**

Seguimos buscando.