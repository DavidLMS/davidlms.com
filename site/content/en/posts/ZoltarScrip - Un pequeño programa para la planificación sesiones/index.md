---
title: "ZoltarScript: A small program for class session planning"
subtitle: "Would you like to know at a glance what class you have next and what you have planned to do in it?"
description: "Would you like to know at a glance what class you have next and what you have planned to do in it?"
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
tags: ['sessions','calendar']
categories: ['Small programs']
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
**Important**: Translated automatically from Spanish by [🌐💬 Aphra 1.0.0](https://github.com/DavidLMS/aphra)

Last week, I was [imagining an ideal application for planning and improving training sessions](https://davidlms.com/article/imagina-una-aplicaci%C3%B3n-ideal-para-planificar-y-mejorar-las-sesiones-de-clase/). As I couldn't find one, I decided to create a **small script**[^1] that I could use for this purpose.

Although it has many flaws and limitations due to the minimal time I could dedicate to it, for now it **decently fulfills** most of the things I was looking for to plan the course. It currently has two main functions:

- **It generates all the sessions of a subject for an entire academic course**. By indicating a course start date, an end date, holidays, and the days and hours of the week when there's a class session, **it shows all the sessions that will take place throughout the course**, creating a row for each one with the session number, date, day of the week, and specific time. In each session's row, there's a column to plan **what will be done in it**.
- **It transfers all the subject sessions to Google Calendar**[^2], including the development of that session **in the event description**. This way, having the calendar synchronized, **I can check what I have to do** in the next session **at any time**, looking at the clock, tablet, or computer. It can also be exported in .icalc format, in case you want to take it to your favorite application.

Everything is done in a Google Sheet[^3], as it's a very easy format to manipulate. For the next course, you can simply copy the column of the sessions into the new ones that are generated, taking into account the comments that have been made to improve them.

**Would you like to try it out to plan your classes?** You can do so by following the instructions you'll find in the [project repository](https://github.com/DavidLMS/ZoltarScript)[^4].

If you've found it useful and want to collaborate on the project, you can do so in different ways:
- Write a comment, always constructive, on this post.
- [Create an issue](https://github.com/DavidLMS/ZoltarScript/issues)[^5] to propose a new function or report an error.
- [Improve the script and submit a pull request](https://github.com/DavidLMS/ZoltarScript/pulls)[^6].
- [Buy me a coffee](https://ko-fi.com/davidlms)[^7] (support my work).

[^1] ZoltarScript: A custom-named script, possibly referencing the fortune-telling machine Zoltar, designed as an educational planning tool.
[^2] Google Calendar: A cloud-based calendar service provided by Google.
[^3] Google Sheet: A cloud-based spreadsheet service provided by Google, similar to Microsoft Excel.
[^4] Project repository: A central location where all the project files and version history are stored, typically on platforms like GitHub.
[^5] Issue: In the context of GitHub, an "issue" is a way to track tasks, enhancements, and bugs for projects.
[^6] Pull request: A method of submitting contributions to a GitHub project, allowing for review before changes are merged.
[^7] "Buy me a coffee": A common phrase used for small online donations to support content creators, not a literal invitation for coffee.