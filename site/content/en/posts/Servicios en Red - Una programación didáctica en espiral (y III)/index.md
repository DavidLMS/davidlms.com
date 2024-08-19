---
title: "Network Services: A Spiral Teaching Curriculum (Part III)"
subtitle: "A detailed session-by-session proposal for a teaching unit"
description: "A detailed session-by-session proposal for a teaching unit"
date: 2020-09-06T18:05:00+02:00
lastmod: 2020-09-06T18:05:00+02:00
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
categories: ['Teaching proposals']
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
    - /article/servicios-en-red-una-programación-didáctica-en-espiral-y-iii/
---
**Important**: Translated automatically from Spanish by [🌐💬 Aphra 1.0.0](https://github.com/DavidLMS/aphra)

Having defined the [objective of this curriculum design](https://davidlms.com/en/girando-alrededor-del-aprendizaje-una-programación-didáctica-en-espiral/), [classified the assessment criteria[^1]](https://davidlms.com/en/servicios-en-red-una-programación-didáctica-en-espiral/), and [established a general weekly plan](https://davidlms.com/en/servicios-en-red-una-programación-didáctica-en-espiral-ii/), we'll conclude this series by **providing a detailed session-by-session breakdown of one of the units**. Specifically, **Unit 1: "Create your own hosting server"**, corresponding to weeks 3-8 of the general plan, that is, a total of 42 sessions.

You have the **complete proposal** in the following table:

| Session | Content |
|:------:|:------:|
|   1   |   - Discussion prompt: Can a computer be controlled remotely?     |
|      | - Explanation: Remote access in text mode and SSH |
|       | - Hands-on activity: Accessing a server using SSH  |
|   2   |   - Discussion prompt: How do we exchange files with a server?
| | - Explanation: File transfer with FTP |
| | - Hands-on activity: Downloading and uploading files on a server using vsftpd, using SSH for installation   |
|   3   |   - Discussion prompt: What do I need to put a web page online? |
| | - Explanation: Web servers |
| | - Hands-on activity: Allow your classmates access to your own web page, using SSH to install the nginx web server and uploading files to the server with vsftpd   |
|   4   |   - Discussion prompt: Are there alternatives to SSH? |
| | - Explanation: Telnet |
| | - Hands-on activity: Try making a Telnet connection and an SSH connection, capturing packets with Wireshark. What's the difference?   |
|   5  |   - Completion of pending activities |
| | - Challenge activity: Put a web page online with https://es.000webhost.com/   |
|   6   |   - Assessment of learning outcomes: 3b, 6b, 5b and 5f   |
|   7   |   - Assessment review   |
|   8   |   - Discussion prompt: Can you see the desktop of a remotely controlled computer? |
| | - Explanation: Remote access in graphical mode |
| | - Hands-on activity: Access a classmate's computer using Remote Desktop and TeamViewer. What are the differences?   |
|   9   |   - Discussion prompt: How do we manage an FTP server with multiple users? |
| | - Explanation: Users, groups, and anonymous access on an FTP server |
| | - Hands-on activity: Allow access on your server to the entire class using anonymous access and to two classmates using jailed users   |
|   10   |   - Discussion prompt: Can we secure communication between a client and a web page? |
| | - Explanation: HTTP and HTTPS protocols |
| | - Hands-on activity: Secure your web page with an HTTPS certificate. Compare HTTP and HTTPS traffic in Wireshark   |
|   11   |   - Discussion prompt: Is FTP a secure protocol? |
| | - Explanation: FTPS and SFTP as alternatives |
| | - Hands-on activity: Use a secure protocol for file transfer   |
|   12   |   - Completion of pending activities |
| | - Challenge activity: Can you find and use an app on your phone to remotely control a computer?   |
|   13   |   - Assessment of learning outcomes: 3c, 3d, 5i, 6c, 6d and 6f |
| | - Reassessment of learning outcomes: 3b, 6b, 5b and 5f   |
|   14   |   - Assessment review   |
|   15   |   - Discussion prompt: Can I administer a server without a graphical interface through a graphical interface? |
| | - Explanation: Remote access via the web |
| | - Hands-on activity: Installation and testing of webmin   |
|   16   |   - Discussion prompt: Can I set limits for FTP server users? |
| | - Explanation: Limits and quotas |
| | - Hands-on activity: Configuring limits and quotas in vsftpd   |
|   17   |   - Discussion prompt: How do I control an FTP server from the command line? |
| | - Explanation: FTP commands |
| | - Hands-on activity: Access your FTP server using the command line, download and upload a file, and verify it   |
|   18   |   - Discussion prompt: What differentiates active and passive access modes in an FTP server? |
| | - Explanation: Operation of active and passive access in an FTP server |
| | - Hands-on activity: Access your FTP server using active and passive mode, capturing the connection with Wireshark. Compare them   |
|   19   |   - Completion of pending activities |
| | - Challenge activity: Install Monsta FTP to use a web as a client for your FTP server   |
|   20   |   - Assessment of learning outcomes: 3e, 3f, 3g and 6g |
| | - Reassessment of learning outcomes: 3b, 3c, 3d   |
|   21   |   - Assessment review   |
|   22   |   - Discussion prompt: Can I have different web pages on the same server? |
| | - Explanation: Virtual sites |
| | - Hands-on activity: Configuration of virtual sites in nginx   |
|   23   |   - Discussion prompt: Are actions on a web page executed on the client or on the server? |
| | - Explanation: Client-side and server-side code. Languages |
| | - Hands-on activity: Execute client-side and server-side code in nginx   |
|   24   |   - Discussion prompt: Can the functionality of a web server be extended with modules? |
| | - Explanation: Utility and installation of modules |
| | - Hands-on activity: Installation of nginx with associated modules   |
|   25   |   - Discussion prompt: Can I block access to my web page from a specific IP? |
| | - Explanation: Security on a web server |
| | - Hands-on activity: Secure your nginx server   |
|   26   |   - Completion of pending activities |
| | - Challenge activity: Serve your web page using IIS on Windows Server   |
|   27   |   - Assessment of learning outcomes: 5c, 5d, 5e, 5g, 5h |
| | - Reassessment of learning outcomes: 5b, 5f, 5i   |
|   28   |   - Assessment review   |
|   29   |   - Discussion prompt: How would you explain to a family member the different ways we have to access and administer a system remotely? |
| | - Explanation: We create definitions of the different types of remote access and administration together |
| | - Personal work: We write our own definitions and usage scenarios for each type   |
|   30   |   - Discussion prompt: What's the utility of an FTP server? In what modes can it operate? |
| | - Explanation: Business scenarios are proposed and solutions are discussed in groups |
| | - Personal work: Search for examples on the Internet   |
|   31   |   - Discussion prompt: How does a web server work? What protocols does it use? |
| | - Explanation: Communication procedure between client and web server and description of protocol operation |
| | - Personal work: We create our own diagrams explaining web server communications   |
|   32   |   - Discussion prompt: What are the advantages and disadvantages of each type of remote access? |
| | - Explanation: Business scenarios are proposed and solutions are discussed in groups |
| | - Personal work: We create a table with the advantages and disadvantages of each type of remote access   |
|   33   |   - We self-evaluate our theoretical knowledge of the services |
| | - Review   |
|   34   |   - Assessment of learning outcomes: 3a, 5a, 6a and 6g   |
|   35   |   - Assessment review   |
|   36   |   - Project: We create our own Hosting   |
|   37   |   - Project: We create our own Hosting   |
|   38   |   - Project: We create our own Hosting   |
|   39   |   - Project: We create our own Hosting   |
|   40   |   - Project defense  |
|   41   |   - Review/Reassessment of learning outcomes 2, 5 and 6   |
|   42   |   - Assessment review   |

**I have structured each week in the same way**: four sessions with new content, an extra session for the slower ones to finish and for the more advanced ones to expand, an assessment session and another for reviewing it (ideally, these last two sessions would be consecutive in time).

Each session where new content is taught begins with a discussion prompt. A question is posed that **highlights a problem[^2]**, based on the students' prior knowledge. During that hour, the tools **to solve that problem** the next time it arises will be provided. Afterward, a hands-on activity will be carried out so that they can somehow "touch" the proposed solution.

To prevent pending work from accumulating for students who need more time, a full hour will be dedicated to finishing it, clearing doubts, and **ensuring they are prepared for an assessment**. More advanced students can perform an additional challenge activity to improve their learning transfer[^3].

We arrive at the assessment session, where **what they have learned will be put to the test**. It is very important that the teacher is attentive to the **different difficulties** that students encounter.

And lastly, and most importantly, the week ends with the review session. It is probably the key session, as it allows us to **apply quality formative assessment[^4]**. Students must be aware that it won't be the last time they have to test that knowledge, so they pay enough attention. In this hour, the teacher will explain and **clarify the difficulties** detected in the previous session.

The last two weeks of the unit are a bit different from the rest. In the penultimate week, **the most purely theoretical concepts** are worked on. On many occasions, we start with the theoretical explanation before moving on to practice. I think that if we only teach the basic theory at the beginning, students will be much better prepared to understand complex concepts after performing several practical tests, as they will be able to **create connections with previous knowledge more easily**. The last week is devoted to a project that **integrates all the content seen in the unit** (and potentially in previous units). It is important that it is as applied as possible, trying to have a **real utility**. Thus, students will verify that what they have learned will serve them in their professional future and **will feel more motivated** to continue learning.

With this approach, we ensure that each learning outcome[^5] is addressed over an extended period, far more thoroughly than if covered in a single, isolated unit. It would be good to take advantage of any circumstance in subsequent units **to use them again**, thus achieving **spaced review[^6]**. The only objective of those we proposed that is left a bit lacking is the one related to learning transfer. It would be ideal for them to put the contents into practice **in more varied situations and in different operating systems**, but it is difficult to achieve this with the time so tight to deliver the complete curriculum[^7]. The times dedicated to **challenge activities** can be used for this purpose.

I hope you find it, at the very least, interesting. Perhaps the current circumstances are not ideal to put something like this into practice for the first time. We are starting a course full of uncertainties, in which we will likely have to modify our planning practically every day. If I manage to carry out a good strategy that can be replicated, you will be the first to know. **I hope you also share it in that case**.

Much encouragement and **good luck**.

[^1]: "Criterios de evaluación" are specific assessment criteria used in the Spanish education system to measure student achievement of learning outcomes.

[^2]: "Poner en evidencia" in this context means to highlight or reveal a problem or issue for discussion.

[^3]: "Transferencia del aprendizaje" refers to the concept of learning transfer, where students apply knowledge or skills learned in one context to another.

[^4]: "Evaluación formativa" is equivalent to formative assessment in English-speaking educational contexts, referring to ongoing assessment practices used to monitor student learning and provide feedback.

[^5]: "Resultados de aprendizaje" are equivalent to learning outcomes in English-speaking educational contexts, describing what students should know or be able to do after completing a unit of study.

[^6]: "Repaso espaciado" refers to the concept of spaced repetition or distributed practice in learning, where review of material is spread out over time to enhance retention.

[^7]: "Currículum" in this context refers to the overall course of study or academic program, similar to "curriculum" in English.