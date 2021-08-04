---
title: "Una guía para probar WireGuard con tu alumnado"
subtitle: "Aprende a crear y configurar tu propio servidor VPN"
description: "Aprende a crear y configurar tu propio servidor VPN"
date: 2021-02-11T18:03:00+02:00
lastmod: 2021-02-11T18:03:00+02:00
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
tags: ['wireguard', 'practica']
categories: ['Recursos']
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
    - /article/una-guía-para-probar-wireguard-con-tu-alumnado/
---

**Vuelvo**, después de bastante tiempo. De hecho, este es la primera publicación del 2021. Y vuelvo, porque tengo algo que quizás os interese. Si no fuera así **no volvería**.

Hace unos meses, quizás algún año (mi percepción del tiempo empeora por momentos) escuché hablar por primera vez de **WireGuard**. Y he querido probarlo desde entonces. Si aún no sabes lo que es, te lo cuento. Si ya lo sabes, **sáltate el párrafo siguiente**.

WireGuard es a la vez **una aplicación y un protocolo de comunicación** que se utiliza para crear **redes privadas virtuales** o, como se les conoce habitualmente por sus siglas en inglés, VPN. Un concepto al que se le ha prestado mucha atención los últimos meses, por la rápida expansión del teletrabajo. Simplificando, una VPN permite **crear un túnel cifrado** para que un cliente que se encuentre en Internet pueda acceder a una red privada local **como si físicamente estuviera conectado a la misma**. Así, puedes conectarte a otros equipos de esa red local y acceder a Internet usando la IP pública que tenga esa red local. Por poner un ejemplo, puedes dejar un disco duro con información conectado en red en la empresa y acceder al mismo desde tu casa de una forma segura. También puedes dejar configurado un servidor VPN en tu casa y conectarte al mismo con tu móvil o portátil desde cualquier red wifi pública a la que accedas. De esta manera el tráfico sin cifrar pasará por la red privada de tu casa y no por esa red pública.

Entonces me encontré con [este curso](https://serversideup.net/courses/gain-flexibility-and-increase-privacy-with-wireguard-vpn/) creado por [Jay Rogers](https://jaydrogers.com/) en la web [ServerSide UP](https://serversideup.net/) y estaba tan detalladamente explicado que tuve que pedirle que me dejara hacer algo similar en castellano para mi alumnado.

Si también queréis utilizarlo con el vuestro, **lo tenéis accesible** en [este enlace](https://davidlms.github.io/Practicas/SERRED/wireguard-ubuntu-server-20).

Puede serte especialmente útil para trabajar el resultado de aprendizaje 8 del módulo **Servicios en Red** de 2ºCFGM SMR, en concreto los criterios:

i) Se ha comprobado el acceso a una red determinada desde los sistemas conectados a otra red distinta.

j) Se ha implantado y verificado la configuración para acceder desde una red pública a un servicio localizado en una máquina de una red privada local.

También si impartes el módulo **Seguridad y Alta Disponibilidad** de 2ºCFGS ASIR, ya que puede servirte para impartir el resultado de aprendizaje 3, en concreto el criterio:

d) Se han configurado redes privadas virtuales mediante protocolos seguros a distintos niveles.

Siempre que pueda, y me apetezca, por aquí me tendréis **compartiendo recursos con vosotros**.

**Nos vemos por videoconferencia**.

**Actualización 11/07/2021**: He cambiado el enlace de la guía, [este es el original publicado](https://davidlms.github.io/Practicas/SERRED/wireguard.html), modificado gracias a la [publicación sobre el formato CodeLab](https://davidlms.com/article/en-busca-de-un-formato-para-las-gu%C3%ADas-pr%C3%A1cticas-codelab/).