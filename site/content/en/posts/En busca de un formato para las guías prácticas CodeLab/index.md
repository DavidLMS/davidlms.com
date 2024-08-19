---
title: "In search of a format for practical guides: CodeLab"
subtitle: "Create attractive, easy-to-navigate, and future-proof technical guides"
description: "Create attractive, easy-to-navigate, and future-proof technical guides"
date: 2021-07-11T19:41:00+02:00
lastmod: 2021-07-11T19:41:00+02:00
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
tags: ['codelab', 'practical']
categories: ['Resources']
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
    - /article/en-busca-de-un-formato-para-las-guías-prácticas-codelab/
---

**Important**: Translated automatically from Spanish by [🌐💬 Aphra 1.0.0](https://github.com/DavidLMS/aphra)

It always happens the same way.

When I set out to create some kind of educational material, like a practical guide, I can't shake this question from my mind: **In what format should I create it?**

It might seem like a trivial question, perhaps I should focus solely on the content, but the reality is that it's not.

On one hand, I'm interested in the format remaining relevant and usable for as long as possible. Creating the material takes time and effort that you won't get back, so it would be a shame to do it with a proprietary tool that depends on a cloud service and over which you have no control. Even if they're tools that are promoted everywhere and are trendy in the educational field. Maybe the result is very attractive but... Depending on a company's interests to keep accessing my material? No, thanks. By the way, this argument also includes making it easy to change and maintain in the future... Practical guides in the field of IT become obsolete very quickly.

On the other hand, the format, from my point of view, should be attractive, adaptable to all types of screens, and easy to navigate through. After all, if we manage to make students want to spend time on the content, they will probably get closer to our learning objective.

Until now, I've opted for creating guides with Markdown[^1] and generating an HTML page from it. You can check the result in [this guide I adapted about WireGuard](https://davidlms.github.io/Practicas/SERRED/wireguard)[^2]. This way, I've been fulfilling the principles that most favor the content creator: a lasting format that's easy to maintain. Now... As far as attractiveness goes, it falls short. Easy to navigate through... Well, it has a table of contents, but it didn't seem enough to me.

So I started investigating. From what I've found, I really liked how they create practical guides at [Apple](https://developer.apple.com/tutorials/swiftui) and [Google](https://developer.android.com/jetpack/compose/tutorial?hl=es-419&continue=https%3A%2F%2Fdeveloper.android.com%2Fcourses%2Fpathways%2Fcompose%3Fhl%3Des-419%23article-https%3A%2F%2Fdeveloper.android.com%2Fjetpack%2Fcompose%2Ftutorial)[^3]. By the way, uncannily similar. But difficult to replicate. Until I came across [Google's CodeLabs](https://codelabs.developers.google.com/)[^4]. And that **did convince me**. Easy to navigate and follow, with sections to avoid having too much content at once on the page and adaptable to any type of screen. It even allows students to report errors in the guide. Now I just need to be able to replicate it easily, with a format that lasts and is easy to maintain.

**And it exists**. It turns out there's a community of volunteers who have created a tool capable of generating a static site[^5] with a guide in CodeLab format starting from a Markdown file. And now the guide about WireGuard has been transformed to look like [this](https://davidlms.github.io/Practicas/SERRED/wireguard-ubuntu-server-20). I think you'll agree that the improvement is very noticeable.

As always, when I tell you something, I don't do it without a purpose. **In this case, there are two**.

The first is that **if you know of similar tools** that meet these basic requirements and are useful for creating practical guides or similar educational material, you know [I'm interested in you telling me about them](mailto:hola@davidlms.com).

The second objective is to **teach you** how to **create these CodeLabs** if you liked the format. For this, I've created a [CodeLab about creating a CodeLab](https://davidlms.github.io/Practicas/crear-codelab). It's only an adaptation of the [original created by Marc DiPasquale](https://www.marcd.dev/codelab-4-codelab), to whom I thank here for allowing me to adapt it to Spanish.

I can't wait to see what you're going to create next.

[^1]: Markdown is a lightweight markup language used for formatting text, popular among developers and technical writers.
[^2]: WireGuard is an open-source Virtual Private Network (VPN) protocol, providing secure network connections.
[^3]: Apple and Google developer tutorials are official learning resources provided by these tech companies for app developers, highlighting their significance in the tech industry.
[^4]: Google's CodeLabs refers to Google's interactive tutorial platform, distinct from the general concept of coding labs or workshops.
[^5]: A static site is a website with fixed content, as opposed to dynamically generated content, often used for simple and fast-loading web pages.