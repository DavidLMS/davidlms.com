---
title: "La transparencia de los nuevos DAW y DAM"
subtitle: "Análisis sobre el nuevo borrador publicado por el Ministerio"
description: "Análisis sobre el nuevo borrador publicado por el Ministerio"
date: 2021-03-22T19:01:00+02:00
lastmod: 2021-03-22T19:01:00+02:00
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
tags: ['DAM', 'DAW', 'borrador']
categories: ['Reflexiones educativas']
resources:
- name: "featured-image"
  src: "featured-image.png"

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
    - /article/la-transparencia-de-los-nuevos-daw-y-dam/
---

**Hace unos días** se publicó un [borrador del Real Decreto](https://www.educacionyfp.gob.es/servicios-al-ciudadano/informacion-publica/audiencia-informacion-publica/abiertos/2021/prd-actualizacion-23titulos-10familias-fp.html) de actualización de determinados títulos de Formación Profesional. Entre ellos, se proponen modificaciones a los títulos de Técnico Superior en **Desarrollo de Aplicaciones Web (DAW)** y Técnico Superior en **Desarrollo de Aplicaciones Multiplataforma (DAM)**, dos de los tres grados superiores de la familia de **Informática y Comunicaciones**. Permiten realizar propuestas sobre esas modificaciones **hasta el 30 de marzo**. Hasta aquí bien.

¿Dónde está el problema? **Principalmente en el formato**. Un PDF de 815 páginas que, por cierto, tarda bastante en descargar del servidor del Ministerio (aún pesando solamente 8,3 MB). El documento **carece totalmente de índice**, por lo que hay que buscar formas alternativas de acceder a la información del título o módulo que quieres consultar. Una vez la encuentras, resulta que te indica el nuevo contenido de los artículos y módulos **sin hacer alusión directa a qué están modificando concretamente**.

Es decir. Que **si quieres saber qué modificaciones se proponen** sobre un módulo concreto, **primero tienes que esperar** a que cargue el PDF, luego **realizar una búsqueda** hasta que encuentres la página donde está la información y, por último, **comparar línea a línea** los resultados de aprendizaje, criterios de evaluación y contenidos con los que están actualmente vigentes. **Si fuera mal pensado**, diría que este tipo de cosas se hacen para **dificultar la comparativa** y que **menos personas** realicen propuestas de cambios. Como no lo soy, lo achaco a que se le han dado muy pocos pensamientos al formato de publicación.

La transparencia **no solo consiste en la publicación en abierto de la información**, sino **también en mostrarla para que pueda analizarse de la forma más sencilla posible**.

Pero **no puede criticarse algo sin propuesta**, así que me puse manos a la obra para elaborar la mía. No he impartido nunca ningún módulo en un ciclo superior, por lo que no tengo la suficiente experiencia como para saber si los cambios en los nuevos borradores son **buenos, malos o insuficientes**. Mi grano de arena será facilitar que la información sobre los cambios propuestos llegue a **las personas adecuadas**, que son los profesores que actualmente imparten esos módulos y conocen sus deficiencias y necesidades **mejor que nadie**.

Tuve más o menos claro desde el principio que una buena opción sería **marcar los cambios** tal y como se ven en el código cuando se realiza una propuesta de modificación sobre un repositorio de Github por ejemplo. Me puse a investigar y encontré [dubdiff](http://dubdiff.com), un software open source creado por [Adam Brown](https://adamarthurryan.com/) que resalta exactamente de esta forma los cambios sobre cualquier texto. También necesitaba una plantilla **que permitiese tener distintas secciones a las que se pudiese acceder fácilmente**, tanto desde un sistema de escritorio como uno móvil. Buscando un poco, localicé [una propuesta en CodePen](https://codepen.io/frogmcw/pen/deqRwa) creada por [Monica Wheeler](https://www.linkedin.com/in/monicacwheeler/). A ambos agradezco el trabajo previo para que esta idea saliese adelante.

**No os hago esperar más**, podéis acceder al [portal de modificaciones sobre DAW](https://davidlms.github.io/ArchivosBlog/BorradorDAW2021/index.html) y al [portal de modificaciones sobre DAM](https://davidlms.github.io/ArchivosBlog/BorradorDAM2021/index.html). Espero que os sea útil a los docentes de esos módulos y que podáis comprobar con más facilidad los cambios que se realizan, con el objetivo de que propongáis vuestras ideas. **Las necesitamos**.
