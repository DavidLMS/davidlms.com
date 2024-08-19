---
title: "ZoltarScript: Un pequeño programa para la planificación sesiones"
subtitle: "¿Te gustaría saber de un vistazo qué clase tienes a continuación y qué tienes planificado hacer en la misma?"
description: "¿Te gustaría saber de un vistazo qué clase tienes a continuación y qué tienes planificado hacer en la misma?"
date: 2020-09-25T19:00:00+02:00
lastmod: 2020-09-25T19:00:00+02:00
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
tags: ['sesiones','calendario']
categories: ['Pequeños programas']
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
    - /article/zoltarscrip-un-pequeño-programa-para-la-planificación-sesiones/
---

La semana pasada estuve [imaginando una aplicación ideal para planificar y mejorar las sesiones de una formación](https://davidlms.com/article/imagina-una-aplicaci%C3%B3n-ideal-para-planificar-y-mejorar-las-sesiones-de-clase/). Como no la encontré, decidí crear un **pequeño script** que pudiera utilizar para ese propósito.

Aunque tiene **muchos defectos y limitaciones**, porque no le podido dedicar más que el tiempo justo, de momento **cumple decentemente** con la mayoría de cosas que buscaba para planificar el curso. Realiza únicamente dos funciones:

- **Genera todas las sesiones de una asignatura para todo un curso**. Indicando una fecha de inicio de curso, otra de fin de curso, los días festivos y los días y horas de la semana en los que hay una sesión de la clase, **muestra todas las sesiones que habrá a lo largo del curso**, creando una fila por cada una con el número de sesión, la fecha, el día de la semana y la hora concreta. En la fila de cada sesión hay una columna para planificar **qué se hará en la misma**.
- **Traslada todas las sesiones de la asignatura a un Calendario de Google**, incluyendo el desarrollo de esa sesión **en la descripción** del evento. De esta manera, teniendo el calendario sincronizado, **puedo consultar qué tengo que hacer** en la próxima sesión **en todo momento**, mirando en el reloj, la tablet o el ordenador. También se puede exportar en formato .icalc, por si quieres llevártelo a tu aplicación favorita.

Todo se realiza en una Hoja de Cálculo de Google, por ser un formato muy fácil de manipular. Para el próximo curso, simplemente puede copiarse la columna de las sesiones en las nuevas que se generen, teniendo en cuenta los comentarios que se hayan puesto para mejorarlas.

**¿Te gustaría probarlo para planificar tus clases?** Puedes hacerlo siguiendo las instrucciones que encontrarás en el [repositorio del proyecto](https://github.com/DavidLMS/ZoltarScript).

**¿Te ha sido útil y quieres colaborar con el proyecto?** Puedes hacerlo de distintas formas:
- Escribe un comentario, constructivo siempre, en esta publicación.
- [Crea un issue para proponer una nueva función o indicar un error](https://github.com/DavidLMS/ZoltarScript/issues).
- [Mejora el script y solicita un pull request](https://github.com/DavidLMS/ZoltarScript/pulls).
- [Invítame a un café](https://ko-fi.com/davidlms).
