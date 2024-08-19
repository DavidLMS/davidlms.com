---
title: "How it's done"
date: 2020-06-02T20:10:14+01:00
excludeFromTopNav: false
showDate: false
aliases:
    - /page/como-se-hace/
---

Are you interested in knowing how this blog is made on a technical level, what investment it entails, and what its visitor statistics are? As an exercise in transparency, I'm launching this section, based on the publication [**How it's done**](https://davidlms.com/article/c%C3%B3mo-se-hace-un-blog-a-coste-0/) and which will be updated with any new developments that arise.

To start, I registered the domain davidlms.com. Specifically, I used the [namecheap](https://www.namecheap.com) platform, which cost $12.94 (including SSL certificate) with the option to renew on May 11, 2021.

I knew I wanted a static website that was easy to maintain. I was looking for something simple, with minimal loading times, that would allow me to write articles in Markdown. That's when I discovered the Hugo framework.

Without a doubt, what finally convinced me to take the plunge was finding [Netlify](https://www.netlify.com/). This platform allows you to publish a static website on the Internet with just a few clicks. Specifically, it creates a repository in your [Github](https://github.com/) account with the source code of the framework you choose, and every time you make a modification (a commit to the repository), it recompiles to update the page. It also provides you with a CDN, a domain, and an SSL certificate for free.

You can view this blog's repository [here](https://github.com/DavidLMS/davidlms.com). The basic configuration is indicated in the site/config.toml file, and the articles are put in Markdown format inside individual folders in the site/content/article path. I've used the [Bilberry Hugo](https://themes.gohugo.io/bilberry-hugo-theme/) theme, which is also based on [Lingonberry](https://www.andersnoren.se/teman/lingonberry-wordpress-theme/) from [Wordpress](https://wordpress.org/). I chose it for its minimalism, its focus on a blog format, and basically for meeting what I needed.

In this theme, there are a couple of things worth configuring. One of them is comments. For me, it was essential that readers who wanted to could easily comment on an article, considering it's a static page. Two options are given, and [DISQUS](https://disqus.com/) is the free one. You just need to create an account and put the registered name in the disqusShortname parameter of config.toml. The other thing is the configuration of searches. For this, a free account on [Algolia](https://www.algolia.com) is used, which is configured by following the [instructions](https://themes.gohugo.io/bilberry-hugo-theme/#Algolia-Search) step by step.

I also wanted to track the blog's visitors, mainly out of curiosity. It can be done for free with [Google Analytics](https://analytics.google.com/analytics/web/), but Google already knows enough about us and I had no intention of letting them obtain data from my visitors just for entering my website. Then I found [Plausible](https://plausible.io), a lighter alternative with an approach focused on maintaining visitors' privacy. If paid annually, it comes to $4 per month.

If you want to access the visitor statistics of this blog, [here they are](https://plausible.io/davidlms.com).

In October 2020, I activated Cloudflare's free service on the domain to improve the website's availability and mitigate possible DDoS attacks. You can see in detail how I did it [here](https://davidlms.com/article/cloudflare-y-su-servicio-gratuito-parar-mejorar-la-disponibilidad-de-tu-web/).

In March 2021, I found the blog out of service. On the error page, Cloudflare indicated that its DNS was working correctly and the problem was with the hosting. However, everything seemed correct in the Netlify panel. So I deactivated Cloudflare, staying with Netlify's original CDN network. After a few hours, the site was back online.

In June 2021, a blog reader commented that, to put it mildly, DISQUS didn't take care of privacy too much, so I started looking for alternatives that did take this issue seriously. I didn't find any free ones, but [Hyvor Talk](https://talk.hyvor.com/) offered me what I was looking for at a more or less affordable price. So I migrated the existing comments from DISQUS to Hyvor Talk and got it working.

In August 2021, it was time to change the blog's appearance. I chose the first theme quickly, for simplicity and to focus soon on the content. However, seeing that I had been able to maintain the project for more than a year without abandoning it, it was time to take the choice a little more seriously. I opted for [uBlogger](https://themes.gohugo.io/themes/ublogger/). I think it's modern enough, but at the same time conservative enough, that I can maintain it like this for a long time. There are some new features, like the possibility of dark mode, as well as a useful little arrow to always go back to the top or the continuously floating menu. Although I'm still maintaining the same search, comment, and analytics services. It has even corrected the historical error that didn't allow access to the blog's RSS and has allowed me to redirect old links to new ones, so that none break. I believe the presentation has gained points. For the nostalgic, [here you can see how the blog looked in July 2021](/old2020.html).

Lastly, I want to show you in the following table the investment made in the blog (updated as of July 2024):

| Concept | Date | Investment |
|:------:|:------:|:------:|
|   Domain (five years)   |   May 2020-24   |   $64.70 |
|   Analytics with Plausible (five years)   |   June 2020-24   |   $240 |
|   Comments with Hyvor Talk (one year)   |   July 2021-24   |   $290.40 |
|   TOTAL  | | $595.10 |