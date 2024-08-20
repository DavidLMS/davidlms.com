---
title: "The course where I became a walking FAQ"
subtitle: "Tired of writing the same answers over and over again?"
description: "Tired of writing the same answers over and over again?"
date: 2020-12-31T14:16:00+02:00
lastmod: 2020-12-31T14:16:00+02:00
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
tags: ['FAQ', 'tools']
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
    - /article/el-curso-en-el-que-me-convertí-en-faq/
---
**Important**: Translated automatically from Spanish by [🌐💬 Aphra 1.0.0](https://github.com/DavidLMS/aphra)

No need to calculate it. This is the course in which I've answered the most emails. And only one term has passed. One of the side effects of blended learning[^1], I suppose. I'll just say that the number of emails with questions received has been inversely proportional to how often I've posted on the blog.

And, as I gave more answers, **certain patterns kept repeating**. In the end, I was writing practically the same thing several times, which is not desirable at all. Suddenly, I felt like I had turned into a walking FAQ myself. So why not make one? Not just because it would be available for consultation and save some emails (my desire), but to link certain answers and thus avoid writing the same content again.

In this context, my investigation began. **Surely there's something already set up that I can use easily**, I thought. Something that more or less meets what I'm looking for, I thought. And there probably is... But I haven't managed to find it, at least not what I had in mind. And that was nothing more than a set of desirable qualities:

* **Open Source**[^2]. With open code, so I could make small adaptations if necessary.
* **Static site generation**. Not only because the loading speed would be minimal, but because it allows the hosting to be free.
* **Linkable answers**. If the main use will be to respond to an email, I need to be able to easily obtain a link to the specific answer.
* **Expandable answers**. Offered in the form of an accordion (menu)[^3] ([example](https://jqueryui.com/accordion/)), so as not to need to load a new page for each of them.
* **Easy to update**. It would be ideal if I could add a new answer or edit the page from any device.
* **With integrated search**. I know it complicates the fact that the page is static, but there are options like Algolia[^4].
* **Possibility of asking new questions**. It would be nice if students could suggest new doubts and even propose answers.
* **Exportable**. So that the work done can be easily migrated to another platform if necessary.
* **Aesthetic**. To top it off, that it's pleasant to navigate and stay on the page, as well as adapt to different screen sizes.

After this, **it's time to search**. There are many options, and I've tried things that I won't put here, so as not to make it too long. It's important to differentiate a simple FAQ from software that allows us to create a Knowledge Base[^5], which is not what I intended, so I discarded options like [GitBook](https://www.gitbook.com/). I also discarded trying plugins for Wordpress, which are quite interesting, but require too much maintenance for my taste, in addition to paid hosting. Unless I do it locally and publish the modifications statically, but I would already be limiting too much the ease of updating that I was looking for. A lightweight alternative to Wordpress that I want to mention is Ghost [with this theme](https://themeforest.net/item/digidocs-documentation-and-knowledge-base-ghost-theme/25719922), which although it's more focused on a Knowledge Base, I found it an option to consider.

At first, I thought of **a static site generator**, like Hugo, Jekyll or Gatsby with a theme prepared for it. I found [Hugo FAQ Theme](https://themes.gohugo.io/hugo-faq-theme/) with many things I liked, but it was too basic. Also [quite a few from Jekyll](https://jekyllthemes.io/jekyll-documentation-themes), designed especially for Knowledge Bases. And then, almost by chance, I came across [this](https://gatsby-theme-faqs.netlify.app/faq).

Well, **basically what I was looking for**, nothing more. It uses Prismic to host the questions, so you can update from any device, Gatsby to generate the web and with a configured *webhook*[^6] to automatically deploy changes with Netlify. It's true that it doesn't allow suggesting new questions and the export is not very simple, but hey, in aesthetics and use almost identical to what I had in mind. I follow [the instructions](https://github.com/littleplusbig/gatsby-theme-faqs-prismic) to set it up and... Compilation error. The project has been without updates for just over a year, so **I'm afraid something has broken**. If someone controls *GraphQL*[^7] and wants to fix it, they will be welcome.

Already more demotivated, I opted to try the classic system of [phpMyFAQ](https://www.phpmyfaq.de/). You need hosting, but maybe it would provide me with everything I was looking for. It's a project that's still alive, and has been with us for a long time, but honestly, it needs an overhaul. The aesthetics and functionality it has have been stuck a few years in the past. At least for my taste. However, if you want to customize the options to the millimeter and **have time for it**, I encourage you to try it.

And halfway through, I came across [HAASH](https://haash.io/). Not so bad. It's true that it doesn't meet many of the requirements I was looking for, but if you need **something immediate and extremely simple**, it's your solution. It allows you to create as many FAQs as you want for free, edit them directly on the web, set permissions, allow students to propose questions, with integrated search... I miss a navigation that doesn't require loading new pages (although I must admit it's very fast) and, above all, the option to export the content. Other than that, maybe it works for you.

This is my way of saying that, if you know of any system that fulfills everything I want, don't hesitate to contact me. And, why not, if you're looking for a web project to **embark on to learn**, simple enough for one person to carry out, here seems to be a niche. A tool that generates, from Markdown files, a static FAQ-type website with categories, Algolia search, Disqus comments... I'll leave it there.

I didn't want to let the year end without writing something here[^8].

I didn't want to miss the opportunity to wish you **a magnificent new year, full of concerns, hopes, projects, and good news**. We don't know what it will bring us. But the important thing is not to know it, but **to be willing** to adapt to whatever comes.

**Until then, see you next year**[^9].

[^1]: Blended learning refers to a hybrid educational model combining in-person and online instruction, which gained prominence during the COVID-19 pandemic.

[^2]: Open Source refers to software whose source code is freely available for viewing, modification, and distribution.

[^3]: An accordion menu in web design is an expandable/collapsible content area, not the musical instrument.

[^4]: Algolia is a hosted search engine provider, often used for implementing site search functionality.

[^5]: A Knowledge Base is a centralized repository of information, often used in customer service and information management contexts.

[^6]: A webhook is a method for real-time data transfer between web applications.

[^7]: GraphQL is a query language for APIs, developed by Facebook.

[^8]: This phrase reflects the cultural context of end-of-year reflections common in blogging.

[^9]: This phrase serves as both a New Year's greeting and a friendly farewell, often used in informal contexts.