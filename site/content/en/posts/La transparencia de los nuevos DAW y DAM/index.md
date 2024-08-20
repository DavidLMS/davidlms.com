---
title: "Transparency in the New DAW and DAM Curricula"
subtitle: "Analysis of the new draft published by the Ministry"
description: "Analysis of the new draft published by the Ministry"
date: 2021-03-22T19:01:00+02:00
lastmod: 2021-03-22T19:01:00+02:00
draft: false

author: "davidlms.en"

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
tags: ['DAM', 'DAW', 'draft']
categories: ['Educational reflections']
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
**Important**: Translated automatically from Spanish by [🌐💬 Aphra 1.0.0](https://github.com/DavidLMS/aphra)

**A few days ago**, a [draft Royal Decree](https://web.archive.org/web/20210323201936/https://www.educacionyfp.gob.es/servicios-al-ciudadano/informacion-publica/audiencia-informacion-publica/abiertos/2021/prd-actualizacion-23titulos-10familias-fp.html)[^1] was published updating certain Vocational Training qualifications[^2]. Among them, modifications are proposed to the qualifications of Higher Technician[^3] in **Web Application Development (DAW)**[^4] and Higher Technician in **Cross-platform Application Development (DAM)**[^5], two of the three higher degrees in the **Computer Science and Communications** family. Proposals for changes to these modifications can be submitted **until March 30**. Up to this point, the process seems appropriate.

What is the main issue? **Primarily in the format**. A PDF of 815 pages which, by the way, takes quite a while to download from the Ministry's[^6] server (even though it only weighs 8.3 MB). The document **completely lacks an index**, so you have to find alternative ways to access the information about the qualification or module you want to consult. Once you find it, it turns out that it indicates the new content of the articles and modules **without making direct reference to what they are specifically modifying**.

In other words, if **you want to know what modifications are proposed** for a specific module, **first you have to wait** for the PDF to load, then **perform a search** until you find the page where the information is and, finally, **compare line by line** the learning outcomes, evaluation criteria, and contents with those currently in force. **If I were to be cynical**, I'd say this kind of thing is done to **make comparison difficult** and have **fewer people** make change proposals. As I'm not, I attribute it to very little thought being given to the publication format.

Transparency **not only consists of publishing information openly** but **also in presenting it so that it can be analyzed in the simplest way possible**.

But **you can't criticize something without a proposal**, so I got to work to develop mine. I have never taught any module in a higher cycle, so I don't have enough experience to know if the changes in the new drafts are **good, bad or insufficient**. My small contribution will be to facilitate that the information about the proposed changes reaches **the right people**, who are the teachers who currently teach these modules and know their deficiencies and needs **better than anyone**.

I was more or less clear from the beginning that a good option would be to **mark the changes** as they are seen in the code when a modification proposal is made on a Github repository for example. I started investigating and found [dubdiff](http://dubdiff.com), an open source software created by [Adam Brown](https://adamarthurryan.com/) that highlights changes on any text exactly in this way. I also needed a template **that would allow different sections to be easily accessed**, both from a desktop and a mobile system. Searching a bit, I found [a proposal on CodePen](https://codepen.io/frogmcw/pen/deqRwa) created by [Monica Wheeler](https://www.linkedin.com/in/monicacwheeler/). I thank both of them for their previous work to make this idea come to fruition.

Without further delay, you can access the [DAW modifications portal](https://davidlms.github.io/ArchivosBlog/BorradorDAW2021/index.html) and the [DAM modifications portal](https://davidlms.github.io/ArchivosBlog/BorradorDAM2021/index.html). I hope it's useful for teachers of these modules and that you can more easily check the changes being made, with the aim of proposing your ideas. **We need your contributions**.

[^1]: Real Decreto: A type of royal decree used in the Spanish legal system for implementing regulations.
[^2]: Formación Profesional: Refers to Vocational Training in the Spanish education system, which is different from general academic education.
[^3]: Técnico Superior: Refers to a higher technician qualification in the Spanish education system, obtained after completing advanced vocational studies.
[^4]: DAW (Desarrollo de Aplicaciones Web): Web Application Development, a specific vocational training program in Spain.
[^5]: DAM (Desarrollo de Aplicaciones Multiplataforma): Cross-platform Application Development, another vocational training program in Spain.
[^6]: Ministerio: In this context, refers to the Ministry of Education in Spain.