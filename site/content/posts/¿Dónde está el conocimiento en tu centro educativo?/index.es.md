---
title: "¿Dónde está el conocimiento en tu centro educativo?"
subtitle: "Un centro que no conoce su historia, está condenado a repetirla"
description: "Un centro que no conoce su historia, está condenado a repetirla"
date: 2020-07-10T17:20:00+01:00
lastmod: 2020-07-10T17:20:00+01:00
draft: false

author: "davidlms"

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
tags: ['wiki', 'organizacion']
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
    - /article/dónde-está-el-conocimiento-en-tu-centro-educativo/
---
Quiero que pienses, **si necesitas obtener información** referente a los siguientes puntos, **a dónde o a quién acudirías**:
* Instrucciones de acceso y normas de utilización de la conexión Wifi del centro.
* Cómo realizar algún procedimiento concreto en la plataforma educativa de gestión que te proporciona la administración (poner calificaciones, realizar algún tipo de informe, gestionar una formación…).
* Conocer qué docente impartió determinada asignatura o módulo en un curso concreto.
* Qué tareas debes realizar como tutor\/coordinador TIC\/jefe de estudios\/jefe de departamento\/cualquier otro cargo y cómo realizarlas.
* Proyectos de innovación y concursos que se están llevando a cabo en el centro y un histórico de los que ya se hicieron.
* Fechas importantes a tener en cuenta.

Podría seguir aumentando la lista, pero creo que se entiende la idea. Si la respuesta la obtendrías **preguntando a una persona de referencia, consultando unas notas personales o incluso rebuscando en la bandeja de entrada de tu correo… Malo, muy malo**. Esa persona puede no estar disponible, las notas personales se quedarán contigo y no podrán ayudar a los demás y en el correo podemos encontrarnos con información desactualizada.

Alguien (no está claro quién) dijo una vez que **un pueblo que no conoce su historia, está condenado a repetirla**. De la misma forma, un centro educativo que carece de un registro accesible de su historia y no tiene al alcance de cualquier docente la información sobre fechas, tareas y procedimientos, **está condenado a repetir errores, hacer perder tiempo al personal y a caminar hacia un futuro totalmente improductivo**.

Todas las organizaciones necesitan una buena base de conocimiento, y el caso de los centros educativos no es distinto. Ahora bien, **¿Qué software podemos usar para ello?**

La opción más básica será utilizar **algún gestor de documentos** tipo Google Drive, aunque será un infierno ordenar, gestionar y encontrar rápidamente la información que necesitas en un momento determinado.

Sin duda deberíamos avanzar a algo **más estructurado** como un Wiki, aunque requiere cierta curva de aprendizaje, y queremos dar todas las facilidades posibles.

Podemos encontrar **software específico para crear una base de conocimiento**. El ideal personal que he encontrado dentro de esta categoría es [Nuclino](https://www.nuclino.com/), aunque la principal pega es que, aunque tiene una opción limitada gratuita, un uso serio requiere de un pago mensual bastante elevado para un centro educativo.

Después de buscar y comparar otras opciones, he llegado a [Wiki.js](https://wiki.js.org/). Tiene un diseño muy limpio e intuitivo, utilizando el motor de búsqueda gratuito de [Algolia](https://www.algolia.com/) la búsqueda de información es casi inmediata, permite limitar el acceso a determinadas páginas en base a grupos de usuarios (un poco complejo de configurar, pero permite un alto grado de personalización) y resuelve muy bien los conflictos cuando editan la misma página dos usuarios al mismo tiempo. **Por supuesto, es open source y podemos instalarla en un servidor propio**.

El siguiente paso lógico sería utilizar esa información como fuente de datos para alimentar un bot, **que te proporcione la información que necesitas en cualquier momento a base de preguntas en lenguaje natural**.

¿Y en tu centro educativo? ¿Utilizáis algún software para este propósito? ¿Conoces una mejor opción? **Me interesa**.

Nos vemos en los bares.
