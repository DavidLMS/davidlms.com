---
title: "Cómo se hace un blog a coste 0"
subtitle: "Anímate a crear uno y compartir tu opinión"
description: "Anímate a crear uno y compartir tu opinión"
date: 2020-06-06T08:31:00+01:00
lastmod: 2020-06-06T08:31:00+01:00
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
tags: ['blog', 'hugo']
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
    - /article/cómo-se-hace-un-blog-a-coste-0/
---

Hace ya **casi un mes** que comencé esta aventura de dejar plasmado por escrito **pensamientos** con más o menos acierto. Así que hoy me he planteado que podría hacer una publicación tipo “**Cómo se hace**” (y no “Cómo se hizo”, porque se sigue haciendo) explicando con más detalle lo que conté en la [primera publicación](https://davidlms.com/article/hello-world/).

Lo **primero** que hice fue registrar **el dominio** davidlms.com. Este paso no es gratuito, pero es **totalmente opcional**. Concretamente utilicé la plataforma [namecheap](https://www.namecheap.com), lo que supuso un coste de 12,94$ (con certificado SSL incluido) que tendré la opción de renovar el próximo 11 de mayo de 2021.

Tenía claro que quería una web **estática** fácil de mantener. Buscaba algo simple, que tuviese tiempos de carga mínimos y me permitiera escribir los artículos en **Markdown**. Fue cuando descubrí el framework [HUGO](https://gohugo.io/)... Si quieres saber más no dejes de leer aquí.

Sin duda lo que me dio el empujón definitivo al vacío fue encontrar [Netlify](https://www.netlify.com/). Esta plataforma te permite publicar un sitio web estático en Internet con **muy pocos clics**. Concretamente, crea un repositorio en tu cuenta de [Github](https://github.com/) con el código fuente del framework que elijas y, cada vez que realizas una modificación (un commit en el repositorio), lo vuelve a compilar para **actualizar la página**. Te proporciona además de forma gratuita un CDN, un dominio y un certificado SSL.

Podéis echar un vistazo al [repositorio de este blog](https://github.com/DavidLMS/davidlms.com),  la **configuración básica** se indica en el archivo site/config.toml y los **artículos** se ponen en formato Markdown dentro de carpetas individuales en la ruta site/content/article. He usado el tema [Bilberry Hugo](https://themes.gohugo.io/bilberry-hugo-theme/), que además está basado en [Lingonberry](https://www.andersnoren.se/teman/lingonberry-wordpress-theme/) de [Wordpress](https://wordpress.org/). Lo elegí por su **minimalismo**, por estar centrado en un **formato blog** y, básicamente, por cumplir con lo que necesitaba.

En este tema hay un par de cosas que merece la pena configurar. Una de ellas son **los comentarios**. Para mí era fundamental que el lector que quisiese pudiera comentar un artículo fácilmente, teniendo en cuenta que es una página estática. Se dan dos opciones, y [DISQUS](https://disqus.com/) es la gratuita. Solamente hay que crear una cuenta y poner el nombre registrado en el parámetro disqusShortname del config.toml. La otra cosa es la configuración de **las búsquedas**. Para eso se hace uso de una cuenta gratuita en [Algolia](https://www.algolia.com), que se configura siguiendo paso a paso las [instrucciones](https://themes.gohugo.io/bilberry-hugo-theme/#Algolia-Search).

Por último, he querido llevar **un registro de los visitantes** del blog, más por curiosidad que por otra cosa. Se puede hacer gratuitamente con [Google Analytics](https://analytics.google.com/analytics/web/), pero Google ya sabe bastante de nosotros y no me daba la gana que obtuviese datos de mis visitantes por el hecho de entrar en mi web. Netlify te permite contratarlo como servicio en su propia plataforma, pero son 9$ al mes… Un poco caro para mi gusto. Entonces encontré [Plausible](https://plausible.io), una alternativa más ligera y con un enfoque centrado en **mantener la privacidad de los visitantes**. Si se paga anualmente, sale a 4$ por mes. De momento estoy en el mes gratuito de prueba. **Algo curioso**: te permite poner la estadística en un enlace público. Así que, por qué no, [aquí tenéis las mías](https://plausible.io/davidlms.com).

Todo esto te lo he contado con el único objetivo de animarte a **crear tu propio blog**, en estos tiempos en los que están en peligro de extinción. Y lo puedes hacer **a coste cero**.

También hay un objetivo secundario. Si sabes cómo lo he hecho, puedes sugerirme **cómo hacerlo mejor**. Te espero en los comentarios.