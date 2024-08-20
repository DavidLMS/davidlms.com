---
title: "How to Create a Blog at Zero Cost"
subtitle: "Take the plunge and create your own blog to share your thoughts"
description: "Take the plunge and create your own blog to share your thoughts"
date: 2020-06-06T08:31:00+01:00
lastmod: 2020-06-06T08:31:00+01:00
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
tags: ['blog', 'hugo']
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
    - /article/cómo-se-hace-un-blog-a-coste-0/
---
**Important**: Translated automatically from Spanish by [🌐💬 Aphra 1.0.0](https://github.com/DavidLMS/aphra)

It's been almost a month since I embarked on this adventure of committing my thoughts to writing, with mixed results. So today I thought I could write a "How-to" type post (and not "How it was done," because it's still ongoing) explaining in more detail what I shared in the [first post](https://davidlms.com/article/hello-world/).

The first thing I did was register the domain davidlms.com. This step isn't free, but it's completely optional. Specifically, I used the [namecheap](https://www.namecheap.com) platform, which cost $12.94 (including SSL certificate) that I'll have the option to renew on May 11, 2021.

I knew I wanted a static website that's easy to maintain. I was looking for something simple, with minimal loading times and that would allow me to write articles in Markdown. That's when I discovered the HUGO[^1] framework... If you want to know more, keep reading.

Without a doubt, what gave me the final push to take the leap[^2] was discovering Netlify[^3]. This platform allows you to publish a static website on the Internet with very few clicks. Specifically, it creates a repository in your [Github](https://github.com/) account with the source code of the framework you choose and, every time you make a modification (a commit in the repository), it recompiles to update the page. It also provides you with a CDN, a domain, and an SSL certificate for free.

You can check out this blog's repository, the basic configuration is indicated in the site/config.toml file and the articles are put in Markdown format inside individual folders in the site/content/article path. I've used the [Bilberry Hugo](https://themes.gohugo.io/bilberry-hugo-theme/) theme, which is also based on [Lingonberry](https://www.andersnoren.se/teman/lingonberry-wordpress-theme/) from [Wordpress](https://wordpress.org/). I chose it for its minimalism, for being centered on a blog format and, basically, for meeting what I needed.

In this theme, there are a couple of things worth configuring. One of them is comments. For me, it was essential that the reader who wanted could easily comment on an article, considering it's a static page. Two options are given, and [DISQUS](https://disqus.com/) is the free one. You just have to create an account and put the registered name in the disqusShortname parameter of config.toml. The other thing is the configuration of searches. For that, a free account on [Algolia](https://www.algolia.com) is used, which is configured by following the [instructions](https://themes.gohugo.io/bilberry-hugo-theme/#Algolia-Search) step by step.

Lastly, I wanted to keep a record of the blog visitors, more out of curiosity than anything else. You can do it for free with [Google Analytics](https://analytics.google.com/analytics/web/), but Google already knows enough about us and I didn't want them collecting data on my visitors just for browsing my website. Netlify allows you to hire it as a service on their own platform, but it's $9 per month... A bit expensive for my taste. Then I found Plausible[^4], a lighter alternative with a focus on maintaining visitor privacy. If paid annually, it comes out to $4 per month. For now, I'm on the free trial month. Something curious: it allows you to put the statistics on a public link. So, why not, [here are mine](https://plausible.io/davidlms.com).

I've told you all this with the sole purpose of encouraging you to create your own blog, in these times when they're in danger of extinction. And you can do it at zero cost[^5].

There's also a secondary objective. If you know how I've done it, you can suggest how to do it better. I'll be waiting for you in the comments[^6].

[^1]: HUGO is a popular open-source static site generator.

[^2]: This is a translation of the Spanish idiom "empujón definitivo al vacío," which metaphorically means the final motivation to make a significant decision or take a risk.

[^3]: Netlify is a cloud computing company that offers hosting and serverless backend services for static websites.

[^4]: Plausible is a lightweight, open-source alternative to Google Analytics.

[^5]: "At zero cost" is a translation of the Spanish phrase "a coste 0," meaning completely free or without any expense.

[^6]: This is a translation of the Spanish phrase "Te espero en los comentarios," which is commonly used to invite readers to engage in discussion in the comment section.