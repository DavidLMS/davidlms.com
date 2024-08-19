---
title: "A Guide for Testing WireGuard with Your Students"
subtitle: "Learn to create and configure your own VPN server"
description: "Learn to create and configure your own VPN server"
date: 2021-02-11T18:03:00+02:00
lastmod: 2021-02-11T18:03:00+02:00
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
tags: ['wireguard', 'practice']
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
    - /article/a-guide-for-testing-wireguard-with-your-students/
---
**Important**: Translated automatically from Spanish by [🌐💬 Aphra 1.0.0](https://github.com/DavidLMS/aphra)

**I'm back**, after quite some time. In fact, this is the first post of 2021. And I'm back because I have something that might interest you. If I didn't have something worthwhile to share, I wouldn't have returned.

A few months ago, maybe a year (my perception of time is getting worse by the moment), I heard about **WireGuard**[^1] for the first time. And I've wanted to try it since then. If you don't know what it is yet, I'll tell you. If you already know, **skip the next paragraph**.

WireGuard is both **an application and a communication protocol** used to create **virtual private networks** or, as they're commonly known by their acronym, VPNs. A concept that has received a lot of attention in recent months, due to the rapid expansion of teleworking. In simple terms, a VPN creates an encrypted tunnel so that a client on the Internet can access a private local network **as if they were physically connected to it**. This way, you can connect to other devices on that local network and access the Internet using the public IP of that local network. For example, you can leave a hard drive with information connected to the network at your company and access it from home in a secure way. You can also set up a VPN server at your home and connect to it with your mobile or laptop from any public wifi network you access. This way, your internet traffic is encrypted and routed through your home network, protecting it from potential threats on public networks.

Then I came across [this course](https://serversideup.net/courses/gain-flexibility-and-increase-privacy-with-wireguard-vpn/) created by [Jay Rogers](https://jaydrogers.com/) on the [ServerSide UP](https://serversideup.net/) website, and it was so thoroughly explained that I had to ask him to let me do something similar in Spanish for my students.

If you also want to use it with yours, **you have it accessible** at [this link](https://davidlms.github.io/Practicas/SERRED/wireguard.html).

It can be especially useful for working on learning outcome 8 of the **Network Services**[^2] module of 2ºCFGM SMR[^3], specifically the criteria:

i) Access to a specific network has been verified from systems connected to a different network.

j) The configuration to access a service located on a machine in a local private network from a public network has been implemented and verified.

Also if you teach the **Security and High Availability**[^4] module of 2ºCFGS ASIR[^5], as it can help you teach learning outcome 3, specifically the criterion:

d) Virtual private networks have been configured using secure protocols at different levels.

Whenever I can, and feel like it, you'll have me here **sharing resources with you**.

**See you in our next video conference**.

**Update 07/11/2021**: I've changed the guide link, [this is the original published](https://davidlms.github.io/Practicas/SERRED/wireguard_old.html), modified thanks to the [publication about the CodeLab format](https://davidlms.com/article/en-busca-de-un-formato-para-las-gu%C3%ADas-pr%C3%A1cticas-codelab/).

[^1] WireGuard is a modern VPN protocol known for its simplicity and efficiency compared to older protocols.
[^2] "Servicios en Red" is a specific networking module in Spanish vocational IT courses, focusing on network services and administration.
[^3] 2ºCFGM SMR refers to the second year of a mid-level vocational training program in Microcomputer Systems and Networks in the Spanish education system.
[^4] "Seguridad y Alta Disponibilidad" is a module that focuses on security and high availability in IT systems, part of advanced vocational training in Spain.
[^5] 2ºCFGS ASIR refers to the second year of a higher-level vocational training program in Network Computer Systems Administration in the Spanish education system.