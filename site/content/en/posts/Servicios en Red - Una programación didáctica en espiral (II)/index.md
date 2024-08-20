---
title: "Network Services: A Spiral Teaching Curriculum (II)"
subtitle: "Placing Learning Outcomes in Time"
description: "Placing Learning Outcomes in Time"
date: 2020-08-22T10:15:00+02:00
lastmod: 2020-08-22T10:15:00+02:00
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
tags: ['teaching curriculum','network services']
categories: ['Teaching Proposals']
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
    - /article/network-services-a-spiral-teaching-curriculum-ii/
---
**Important**: Translated automatically from Spanish by [🌐💬 Aphra 1.0.0](https://github.com/DavidLMS/aphra)

After defining the [objective of this curriculum[^1]](https://davidlms.com/en/girando-alrededor-del-aprendizaje-una-programación-didáctica-en-espiral/) and [classifying the evaluation criteria[^2]](https://davidlms.com/en/servicios-en-red-una-programación-didáctica-en-espiral/), it is time to outline in general terms **what we are going to dedicate each week to**.

Ideally, we would have **worked on all learning outcomes in parallel**, deepening each of them throughout the course. However, as this is a vocational training program[^3], I thought it might be too overwhelming, so I have opted to group the learning outcomes. This way, **a set of them** will be learned in parallel. This does not mean that once a group has been worked on, they will not be revisited during the course. **The assessments and projects are designed to review the content** covered previously throughout the school year.

To promote formative assessment, **evaluations will be conducted every week**. Each assessment will allocate a percentage to reviewing some previous learning outcomes and another percentage to evaluating new criteria.

I believe it is good for students **not to work with just one software for a particular service, nor with just one operating system**, but the module[^4] does not have enough hours to dedicate sufficient time to cover the most used ones. That is why I recommend **coordinating with teachers of other modules** such as web applications or network operating systems. For example, Apache on Windows can be used in web applications and Nginx on Ubuntu Server can be used in network services. The network operating systems module can also be taught focusing on Windows and the network services module focusing on Linux.

In this case, **I have chosen to center the module on Ubuntu Server[^5]**, using the following applications:
* OpenSSH and Webmin for the remote access service.
* Vsftpd for the file transfer service.
* Nginx for the web server.
* Bind9 for the domain name service.
* Isc-dhcp-server for the dynamic network configuration service.
* Postfix and Squirrelmail for the mail service.
* FreeRadius for wireless network security.
* Squid as a proxy and WireGuard as a VPN for connecting private and public networks.

This does not mean that **I will not occasionally use other tools and other operating systems**, as well as control panel solutions from hosting companies.

Below, you have a **work proposal for each of the weeks** of the module:

| Week | Content |
|:------:|:------:|:------:|:-------:|
|   1   |   Review of networks and Linux operation   |
|   2   |   Review of networks and Linux commands*   |
|   3   |   Introduction to SSH, FTP and web server   |
|   4   |   Basic configuration of SSH, vsftpd and nginx   |
|   5  |   Remote access and advanced vsftpd   |
|   6   |   Advanced nginx   |
|   7   |   Consolidating theory (Remote access, file transfer service and web server)   |
|   8   |   Integration project (SSH, FTP and web server in a hosting)   |
|   9   |   Introduction to DNS and DHCP   |
|   10   |   Basic configuration of bind9 and introduction to mail service   |
|   11   |   Advanced configuration of bind9 and isc-dhcp-server   |
|   12   |   Advanced configuration of postfix and squirrelmail   |
|   13   |   Consolidating theory (DNS, DHCP and mail service)   |
|   14   |   Introduction to Proxy and VPN with basic configuration of Squid and WireGuard   |
|   15   |   Advanced configuration of Squid and WireGuard   |
|   16   |   Introduction and installation of a Radius server   |
|   17   |   Theory on wireless network security   |
|   18   |   Review project - Configuration of services in a local network (I)   |
|   19   |   Final evaluation tests   |
|   20   |   Review project - Configuration of services in a local network (II)   |
|   21   |   Recovery / Review projects - Creating a network with ZeroTier   |

*I usually dedicate only one week to review, but given that the students at this level had emergency instruction during the third trimester of the past course, I thought it appropriate to dedicate twice as much time to avoid gaps that might hinder the assimilation of new content.

The order and grouping of learning outcomes is based on **subjective criteria**. If anyone is particularly interested in this, I could provide an explanation.

I would like those teachers who have taught the module before to **share their opinions on this temporal distribution, as well as alternative ways of approaching it**.

Once we reach a consensus here, it will be time to decide **what content to work on and/or what criteria to evaluate in each session**.

**Update**: You can now find the conclusion of this series [here](https://davidlms.com/en/servicios-en-red-una-programación-didáctica-en-espiral-y-iii/).

[^1]: A comprehensive educational planning process in the Spanish education system, similar to curriculum development but with a focus on specific teaching strategies and methodologies.
[^2]: Specific standards used to assess student performance and achievement in the Spanish education system.
[^3]: Refers to a specific level of vocational education in the Spanish education system, typically pursued after completing compulsory secondary education.
[^4]: In the context of Spanish vocational education, this refers to a specific subject or course unit within a vocational program.
[^5]: A variant of the Ubuntu operating system optimized for server use.