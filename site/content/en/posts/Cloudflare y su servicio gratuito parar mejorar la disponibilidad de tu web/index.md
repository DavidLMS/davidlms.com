---
title: "Cloudflare and its free service to improve your website's availability"
subtitle: "How has the blog's performance improved?"
description: "How has the blog's performance improved?"
date: 2020-10-16T18:00:00+02:00
lastmod: 2020-10-16T18:00:00+02:00
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
tags: ['cloudflare', 'CDN']
categories: ['Resources']
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
    - /article/cloudflare-y-su-servicio-gratuito-parar-mejorar-la-disponibilidad-de-tu-web/
---
**Important**: Translated automatically from Spanish by [🌐💬 Aphra 1.0.0](https://github.com/DavidLMS/aphra)

Since I started the blog, I've been transparent about its technical aspects, and in fact, you have the [How it's made](https://davidlms.com/en/como-se-hace/)[^1] section **fully updated**.

This week I registered the domain with [Cloudflare's](https://www.cloudflare.com/es-es/)[^2] **free service** to improve the website's **availability**. Want to know what it entails, how I did it, and what changes I've observed? Keep reading.

Cloudflare is an American company that offers various internet services. Among them, two are free: the [CDN](https://www.cloudflare.com/es-es/cdn/)[^3] and [DDoS attack prevention](https://www.cloudflare.com/es-es/ddos/)[^4]. A **CDN** is a content delivery network. Simply put, it's several strategically geographically distributed servers that store your website, thus improving speed (when there's an access, it's directed to the nearest server) and availability (it's less likely for the site to go offline if it's replicated on several servers). A **DDoS attack**, also simplified, occurs when multiple devices (many) make multiple requests to a specific server or network, aiming to saturate it and make it unavailable.

Before activating the service, I'm going to perform **some preliminary performance tests**, to be able to check if it improves afterwards. It's important to note that, depending on the network status and other factors, the tests can vary continuously, so they'll only be an estimate.

I'll perform the first test with Google's [PageSpeed Insights](https://developers.google.com/speed/pagespeed/insights/?hl=es)[^5] **service**. The result is a score of **88/100 in web performance on a computer** and **a score of 64/100 on a mobile**. You can access the details of these analyses in the following links:

* [PageSpeed analysis on a computer before activating Cloudflare](https://davidlms.github.io/ArchivosBlog/PageSpeed_antes_cloudfare_ordenador.html)
* [PageSpeed analysis on a mobile before activating Cloudflare](https://davidlms.github.io/ArchivosBlog/PageSpeed_antes_cloudfare_movil.html)

I'll perform the second test using **the** [Pingdom Website Speed Test](https://tools.pingdom.com/)[^6] **service**, which allows us to calculate the blog's **loading time** from different cities around the world. You have a summary of the results in the following table:

| Region | Performance Score | Load Time | Detail |
|:------:|:------:|:------:|:------:|
|   Asia - Japan - Tokyo   |   86  | 4.53s | [link](https://tools.pingdom.com/#5d478cb750400000) |
|   Europe - Germany - Frankfurt   |   86  | 328ms |  [link](https://tools.pingdom.com/#5d478d3443400000) |
|   Europe - United Kingdom - London  |   86  | 547ms |  [link](https://tools.pingdom.com/#5d478d4cca800000) |
|   North America - USA - Washington D.C   |   86  | 458ms |  [link](https://tools.pingdom.com/#5d478d6612800000) |
|   North America - USA - San Francisco   |   86  | 548ms |  [link](https://tools.pingdom.com/#5d478dfc36c00000) |
|   Oceania - Australia - Sydney   |   86  | 3.95s |  [link](https://tools.pingdom.com/#5d478e1b38400000) |
|   South America - Brazil - São Paulo   |   86  | 1.24s |  [link](https://tools.pingdom.com/#5d478e42d0800000) |

**The average performance score in Pingdom is 86 and the average loading time is 1.66 seconds**.

Next, I'll perform the free procedure to activate Cloudflare services. Want to know how I did it step by step? Check the following link:
[Step-by-step activation of a domain in Cloudflare](https://davidlms.github.io/Presentaciones-HTML/cloudflare/cloudflare.html)

Now we'll perform **the same previous analysis** again, to know how the blog's performance and loading speed have varied.

The result in PageSpeed is **a score of 98/100 in web performance on a computer** and **a score of 87/100 on a mobile**. You can access the details of these analyses in the following links:

* [PageSpeed analysis on a computer after activating Cloudflare](https://davidlms.github.io/ArchivosBlog/PageSpeed_despues_cloudfare_ordenador.html)
* [PageSpeed analysis on a mobile after activating Cloudflare](https://davidlms.github.io/ArchivosBlog/PageSpeed_despues_cloudfare_movil.html)

In the following table, you have the summary of the analyses performed in Pingdom:

| Region | Performance Score | Load Time | Detail |
|:------:|:------:|:------:|:------:|
|   Asia - Japan - Tokyo   |   83  | 1.75s | [link](https://tools.pingdom.com/#5d4983bda7800000) |
|   Europe - Germany - Frankfurt   |   81  | 1.51s |  [link](https://tools.pingdom.com/#5d4984116c400000) |
|   Europe - United Kingdom - London  |   83  | 2.18 |  [link](https://tools.pingdom.com/#5d49844952c00000) |
|   North America - USA - Washington D.C   |   83  | 736ms |  [link](https://tools.pingdom.com/#5d49846c21400000) |
|   North America - USA - San Francisco   |   83  | 227ms |  [link](https://tools.pingdom.com/#5d49848a69400000) |
|   Oceania - Australia - Sydney   |   83  | 1.09s |  [link](https://tools.pingdom.com/#5d4984a7fbc00000) |
|   South America - Brazil - São Paulo   |   83  | 3.00s |  [link](https://tools.pingdom.com/#5d4984c4b8800000) |

**The average performance score in Pingdom is 82.71 and the average loading time is 1.5 seconds**.

We see that **the PageSpeed scores have improved considerably**, and that's very positive for the blog, as it's one of the factors to consider for positioning it in Google's search engine. In Pingdom, **although the average loading time is lower**, it has caught my attention that now **the loading time for cities in Europe and South America is slower** than before activating the service. It's unfortunate, since most of the visits come from these regions. **But there's an important detail**. In Cloudflare, the following image appears:

![Diagram in Cloudflare about loading time](/cargacloudflare.png)

The total loading time with Cloudflare is slower, however, **partial content is displayed more quickly**. Isn't it the blank screen that frustrates us? Don't we prefer to check earlier that the page is loading? **What are the chances that someone will abandon a website they're trying to visit once "something" has loaded?**

We continue searching[^7].

[^1]: "How it's made" is likely a regular feature or section on the author's blog, providing insights into the technical aspects of the blog.

[^2]: Cloudflare is a company that provides content delivery network (CDN) services, DDoS mitigation, Internet security, and distributed domain name server services.

[^3]: CDN stands for Content Delivery Network, a system of distributed servers that deliver web content to users based on their geographic location.

[^4]: DDoS stands for Distributed Denial of Service, a type of cyberattack that attempts to make a website or network resource unavailable by overwhelming it with traffic from multiple sources.

[^5]: PageSpeed Insights is a tool by Google that analyzes web pages and provides suggestions to make them faster.

[^6]: Pingdom Website Speed Test is a tool that tests the load time of a website from different locations around the world.

[^7]: This phrase, "We continue searching," implies that the author is still investigating and exploring ways to improve the website's performance.