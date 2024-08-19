---
title: "Where is the knowledge in your educational center?"
subtitle: "An educational center that doesn't know its history is doomed to repeat it"
description: "An educational center that doesn't know its history is doomed to repeat it"
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
tags: ['wiki', 'organization']
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
    - /article/where-is-the-knowledge-in-your-educational-center/
---
**Important**: Translated automatically from Spanish by [🌐💬 Aphra 1.0.0](https://github.com/DavidLMS/aphra)

I want you to think, **if you need to obtain information** regarding the following points, **where or to whom would you turn**:
* Instructions for access and usage rules for the educational center's[^1] Wifi connection.
* How to perform a specific procedure on the educational management platform[^2] provided by the administration (enter grades, create a certain type of report, manage training...).
* Find out which teacher taught a particular subject or module in a specific course.
* What tasks you should perform as a tutor/ICT coordinator[^3]/head of studies[^4]/department head[^5]/any other position and how to perform them.
* Innovation projects and competitions that are being carried out in the educational center and a history of those that have already been done.
* Important dates to keep in mind.

I could keep adding to the list, but I think the idea is clear. If you would get the answer by **asking a reference person, consulting personal notes, or even digging through your email inbox... That's really not good**. That person may not be available, personal notes will stay with you and won't be able to help others, and in the email, we might find outdated information.

Someone (it's not clear who) once said that **an educational community that doesn't know its history is doomed to repeat it**. In the same way, an educational center that lacks an accessible record of its history and doesn't have information about dates, tasks, and procedures within reach of any teacher, **is doomed to repeat mistakes, waste staff time, and head down an unproductive path**.

All organizations need a good knowledge base, and the case of educational centers is no different. Now then, **What software can we use for this?**

The most basic option would be to use **some document manager** like Google Drive, although it will be hell to organize, manage, and quickly find the information you need at a given moment.

Without doubt, moving to something **more structured** like a Wiki would be better, although it requires a certain learning curve, and we want to provide all possible facilities.

We can find **specific software to create a knowledge base**. The personal ideal I've found within this category is [Nuclino](https://www.nuclino.com/), although the main drawback is that, while it has a limited free option, serious use requires a fairly high monthly payment for an educational center.

After searching and comparing other options, I've come to [Wiki.js](https://wiki.js.org/)[^6]. It has a very clean and intuitive design, using the free search engine from [Algolia](https://www.algolia.com/), the search for information is almost immediate, it allows limiting access to certain pages based on user groups (a bit complex to configure, but allows a high degree of customization) and resolves conflicts very well when two users edit the same page at the same time. **Of course, it's open source and we can install it on our own server**.

The next logical step would be to use that information as a data source to feed a bot, **which provides you with the information you need at any time based on questions in natural language**.

What about your educational center? Do you use any software for this purpose? Do you know a better option? **I'm interested**.

Catch you later.

[^1]: An educational center in the Spanish system refers to any institution that provides formal education, including primary schools, secondary schools, and universities.

[^2]: Educational management platforms in Spanish educational settings typically include tools for course creation, student data management, grading, and communication between teachers, students, and parents.

[^3]: ICT coordinators in Spanish schools are responsible for integrating and managing Information and Communication Technologies within the educational institution.

[^4]: The "head of studies" (jefe de estudios) is a senior administrative position in Spanish schools, similar to an academic dean, responsible for overseeing academic programs and student affairs.

[^5]: A department head (jefe de departamento) in Spanish educational institutions is responsible for overseeing a specific department or area of study, managing faculty and staff, and coordinating educational programs and policies.

[^6]: Wiki.js is an open-source wiki software platform designed for creating collaborative documentation and knowledge management systems.