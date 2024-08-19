---
title: "Network Services: A Spiral Teaching Curriculum"
subtitle: "Everything has a beginning... and an end?"
description: "Everything has a beginning... and an end?"
date: 2020-08-04T19:03:00+02:00
lastmod: 2020-08-04T19:03:00+02:00
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
tags: ['curriculum design','network services']
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
    - /article/servicios-en-red-una-programación-didáctica-en-espiral/
---

**Important**: Translated automatically from Spanish by [🌐💬 Aphra 1.0.0](https://github.com/DavidLMS/aphra)

Following the trail of the gauntlet thrown in [this publication](https://davidlms.com/article/girando-alrededor-del-aprendizaje-una-programaci%C3%B3n-did%C3%A1ctica-en-espiral/), the time has come **to design a new curriculum**[^1] for the Network Services module[^2].

I'm going to start from the evaluation criteria of the different learning outcomes[^3], first dividing them into **conceptual** (things that students should know) and **procedural** (things that students should know how to do). Although I **prefer to make the distinction between theoretical (T) and practical (P)** directly. It may all sound very old-fashioned to you, but the conceptual and procedural terms are also outdated, and I think this way we understand each other much better. If you take a quick look at the criteria, you'll realize that categorization into one group or another is very simple. The theoretical ones **use verbs** like recognize, identify, illustrate, describe..., etc. The practical ones, on the other hand, use verbs like install, check, verify, create, configure, implement..., etc. If you disagree with any of the classified criteria **we can always discuss it**.

The other categorization is more complex, **as it is entirely subjective**. I'm referring to the weight that each criterion will have in the evaluation: basic, intermediate or advanced. If you want to know why I do it this way, you have the full explanation in [this publication](https://davidlms.com/article/evaluar-por-resultados-de-aprendizaje-y-criterios-de-evaluaci%C3%B3n-sin-morir-en-el-intento/). I've classified the installation, basic configuration, and verification of each service as a basic criterion and, therefore, minimum. A slightly more complex configuration or a concept that requires having basic knowledge of how the service works, I've classified as **intermediate**. The **advanced** criteria are those with the highest complexity and are entirely supplementary to the core requirements. This classification is completely **open to debate**, moreover, it would help me a lot if it were discussed and if all the teachers who teach the module established a similar criterion, as it would contribute to making **the evaluation fairer** regardless of the educational center where the student studies.

You have **the complete table** with all the classified criteria of the module below:

| Evaluation Criterion | Type | Proposed Weight |
|:------:|:------:|:------:|:-------:|
|   1a. The functioning of automated mechanisms for configuring network parameters was recognized   |   T   |   B |
|   1b. The advantages they provide were identified   |   T   |   B |
|   1c. The procedures and guidelines involved in a network parameter configuration request were illustrated   |   T   |   I |
|   1d. A DHCP service for network parameters was installed   |   P   |   B |
|   1e. The service was configured to assign the basic configuration to local network systems   |   P   |   B |
|   1f. Dynamic and static assignments were made   |   P   |   B |
|   1g. Additional configuration options were integrated into the service   |   P   |   I |
|   1h. The correct assignment of parameters was verified   |   P   |   B |
|   2a. Scenarios where the need for a name resolution service arises were identified and described   |   T   |   B |
|   2b. The main name resolution mechanisms were classified   |   T   |   I |
|   2c. The structure, nomenclature, and functionality of hierarchical name systems were described   |   T   |   I |
|   2d. A hierarchical name resolution service was installed   |   P   |   B |
|   2e. The service was configured to cache responses from public DNS servers and serve them to local network devices   |   P   |   B |
|   2f. Name records corresponding to a new zone were added, with options related to mail servers and aliases   |   P   |   I |
|   2g. Group work was performed to conduct zone transfers between two or more servers   |   P   |   A |
|   2h. The correct functioning of the server was verified   |   P   |   B |
|   3a. The utility and mode of operation of the file transfer service were established   |   T   |   B |
|   3b. A file transfer service was installed   |   P   |   B |
|   3c. Users and groups were created for remote access to the server   |   P   |   I |
|   3d. Anonymous access was configured   |   P   |   I |
|   3e. Limits were set on different access modes   |   P   |   A |
|   3f. Access to the server was verified in both active and passive modes   |   P   |   B |
|   3g. Tests were conducted with command-line and graphical mode clients   |   P   |   B |
|   4a. The different protocols involved in sending and retrieving email were described   |   T   |   B |
|   4b. An email server was installed   |   P   |   B |
|   4c. User accounts were created and their access was verified   |   P   |   B |
|   4d. Aliases were defined for email accounts   |   P   |   I |
|   4e. Methods were applied to prevent misuse of the email server   |   P   |   A |
|   4f. Services were installed to allow remote collection of existing mail in user mailboxes   |   P   |   I |
|   4g. Students used email clients to send and receive mail   |   P   |   B |
|   5a. The fundamentals and protocols on which web server operation is based were described   |   T   |   B |
|   5b. A web server was installed   |   P   |   B |
|   5c. Virtual sites were created  |   P   |   I |
|   5d. Existing possibilities to differentiate the destination site of incoming server traffic were verified   |   P   |   A |
|   5e. Server security was configured   |   P   |  A  |
|   5f. User access to the server was verified   |   P   |   B |
|   5g. The execution of code on the server, on the client, and between the two was differentiated and tested   |   P   |   B |
|   5h. Modules were installed on the server   |   P   |   I |
|   5i. Mechanisms were established to ensure communications between the client and the server   |   P   |  A  |
|   6a. Methods of remote system access and administration were described   |   T   |   B |
|   6b. A command-line remote access service was installed   |   P   |   B |
|   6c. A graphical mode remote access service was installed   |   P   |   B |
|   6d. The operation of both methods was verified   |   P   |   B |
|   6e. The main advantages and disadvantages of each were identified   |   T   |   I |
|   6f. Remote access tests were performed between systems of different types   |   P   |   I |
|   6g. Remote administration tests were performed between systems of different types   |   P   |   I |
|   7a. A wireless access point was installed within a local network   |   P   |   B |
|   7b. The access point's protocols, operation modes, and main configuration parameters were identified   |   T   |   B |
|   7c. The most suitable configuration was selected for different test scenarios   |   P   |   I |
|   7d. An adequate security mechanism for wireless communications was established   |   P   |   I |
|   7e. Various types of wireless devices and adapters were used to check coverage   |   P   |   B |
|   7f. A wireless router with connection to a public network and local network wireless services was installed   |   P   |   A |
|   7g. The router was configured and tested from local network computers   |   P   |   I |
|   8a. The hardware of a system with access to a local private network and a public network was installed and configured   |   P   |   B |
|   8b. An application acting as a gateway between the local private network and the public network was installed   |   P   |   B |
|   8c. The main characteristics and capabilities of the selected application were recognized and differentiated   |   T   |   I |
|   8d. The local private network systems were configured to access the public network through the gateway   |   P   |   I |
|   8e. Access control procedures were established to secure traffic transmitted through the gateway   |   P   |   A |
|   8f. Mechanisms were implemented to accelerate communications between the local private network and the public network   |   P   |   A |
|   8g. Possible application scenarios for this type of mechanism were identified  |   T   |   I |
|   8h. A mechanism was established to allow forwarding network traffic between two or more interfaces of the same system   |   P   |   I |
|   8i. Access to a specific network from systems connected to a different network was verified   |   P   |   I |
|   8j. The configuration to access a service located on a machine in a local private network from a public network was implemented and verified   |   P   |   I |

This **is the starting point**, and on this basis we will build a new curriculum design. Further details will be provided in upcoming publications.

**Update**: You now have the second publication of this series available [here](https://davidlms.com/article/servicios-en-red-una-programaci%C3%B3n-did%C3%A1ctica-en-espiral-ii/) and the conclusion [here](https://davidlms.com/article/servicios-en-red-una-programaci%C3%B3n-did%C3%A1ctica-en-espiral-y-iii/).

[^1]: "Programación didáctica" refers to a comprehensive educational planning process in Spanish-speaking countries, which includes curriculum design, teaching methodologies, and assessment strategies.

[^2]: "Servicios en Red" refers to a specific module or course in the Spanish educational system focused on network services and administration.

[^3]: "Resultados de aprendizaje" is equivalent to "learning outcomes" in English-speaking educational systems and is a key component of curriculum design in Spain.