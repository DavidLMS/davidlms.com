---
title: "Private Relay: The Ultimate Solution for Internet Anonymity?"
subtitle: "What is known, what I intuit, and what I think about Apple's new service"
description: "What is known, what I intuit, and what I think about Apple's new service"
date: 2021-06-09T18:36:00+02:00
lastmod: 2021-06-09T18:36:00+02:00
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
tags: ['Private Relay', 'privacy']
categories: ['More technical things']
resources:
- name: "featured-image"
  src: "featured-image.png"

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
    - /article/private-relay-la-solución-definitiva-para-el-anonimato-en-internet/
---

**Important**: Translated automatically from Spanish by [🌐💬 Aphra 1.0.0](https://github.com/DavidLMS/aphra)

On June 7th, at the annual WWDC[^1], Apple presented the new features in their operating systems. One of them was Private Relay.

But first, let's add some context (you can skip this if you have basic knowledge of networks). When we browse the internet, we do so identified by an address called IP. This IP is necessary so that when we make a request to a website, the response can return to our device. Additionally, to know the IP of the website we want to visit, we have to ask another server (this is a DNS request). At the end of the process, both our IP and the website we're going to visit are known by:

- Our Internet Service Provider (ISP).
- The DNS server that processes the request.
- The server of the website we visit.
- Any other intermediary on the network.

Moreover, the IP address can sometimes be used to determine your location. At least, if we use HTTPS, the content of that connection will be encrypted. But with just those two pieces of data, our ISP can block us and record access to certain pages, the DNS can also have our browsing history, and the website server can share information about our queries with third parties, creating commercial profiles much more personalized than our privacy would like. Some available solutions to this problem:

-	DNS over HTTPS (DoH)[^2]. Many modern browsers and routers allow encrypting queries to the DNS server. This prevents our ISP from seeing that query (although it does see the one we subsequently make to the website), although the DNS server could still record it. DNS servers that offer this service cross their hearts that they don't store any information that could harm privacy.
-	Using a Proxy. This involves using an intermediary server to browse the internet. Any query we make will pass through the proxy. This only hides our IP from the website server, but not from our ISP and of course not from the proxy owner.
-	Using a VPN. Virtual Private Networks or VPNs were designed to allow remote workers to use a company's local resources as if they were physically there. They create an encrypted tunnel through the internet between a person's device and the VPN server. This hides the traffic from our ISP, but not from the VPN server owner.
-	Using TOR[^3]. With a special browser, we can encrypt our communications with several layers, at the cost of a slower connection. However, it's possible to identify who's behind these communications with a more or less deep analysis.

Let's return to Private Relay. Keep in mind that this service focuses on hiding the combination of our IP address and the website we visit, so that absolutely no one (not ISP, not website server, not Apple, not intermediaries) knows our browsing history. However, it doesn't protect DNS queries, so it would need to be combined with DoH or similar. In the case of Apple devices, at WWDC 2020 [a session was broadcast talking about this topic](https://developer.apple.com/videos/play/wwdc2020/10047/).

So far I haven't found too much about the technical functioning of Private Relay. In this post, I'm going to tell you what's known about it so far and what my interpretation is. We'll first present the facts and then move on to opinions.

The technical information provided by Apple can be found in the session [Apple's privacy pillars in focus](https://developer.apple.com/videos/play/wwdc2021/10085/) available publicly. I'm going to do a free translation of it using images from the video.

The pillars of the Private Relay service are:

-	All connections are encrypted.
-	Your IP address no longer identifies you.
-	The exact location of your IP address is protected.
-	No company (not even Apple) can see what you're doing.

![Private Relay features. Source: Apple](/privaterelay01.png)

The discourse provided by the Apple technician is as follows:

![General scheme of Private Relay. Source: Apple](/privaterelay02.png)

"Let's briefly explore how Private Relay works when I go shopping for things for my new home. First, when we make a connection to a furniture sales website, two different Proxy servers are randomly chosen in the Private Relay network, so that no single operator has control or can see the complete scenario. The proxy that accepts my connection from the internet is called the Ingress Proxy[^4]. This proxy hides my IP from other servers and encrypts my internet traffic so that my service provider doesn't know what I'm doing. The retransmission of the request to the internet is done by the Egress Proxy[^5], to prevent the Ingress Proxy from knowing the site to which I'm making the request.

![Functions of the ingress and egress proxies in Private Relay. Source: Apple](/privaterelay03.png)

Private Relay manages network access in a way that doesn't require any type of identification or personal information, using blind RSA signatures[^6]. A blinding cryptographic operation performed by my device allows me to access the network without giving any type of information about my account or who is making the connection.

![Verification of access tokens in Private Relay. Source: Apple](/privaterelay04.png)

Using the public key of the access token server, a Private Relay proxy can quickly verify the permission to access the network. Before making a connection, the Private Relay Access Token Server provides a set of different tokens to my device. This gives me access to any proxy I choose when I need it.

![Blinded access tokens to prevent tracking of the origin in Private Relay. Source: Apple](/privaterelay05.png)

To force the separation of information between the proxies I choose, the connection is encapsulated using several layers of encryption. The proxies remove these layers as the connection passes through them. Only my device can decrypt each layer, which is necessary to know that I'm accessing the furniture website.

![Encryption layers in Private Relay. Source: Apple](/privaterelay06.png)

When the connection is made, the Egress Proxy randomly chooses an IP. This helps prevent my sofa search from being related to my lawnmower search, or to my recent table order. Over time, Private Relay connections are automatically created and reused to provide protection against IP tracking and good performance. The way Private Relay hides my IP has one more benefit for privacy. Since my home IP address can be geolocated, the Ingress Proxy can share that location with me. This allows me to inform the Egress Proxy which group of IP addresses to choose. This is a great example of good service while maintaining privacy. Websites can provide local content in Safari while my precise location remains hidden.

Remember, the Ingress Proxy is the only one that can see my IP address and converts it to another address that belongs to the same geographic area. Thus, the lawnmower sales site can know approximately from which area the connection is made. In this example, the Ingress Proxy returns the area "Bay Area, California"[^7], which is forwarded to the Egress Proxy to help it choose a group of IP addresses assigned to that general area. With a regional IP address, the sites I connect to can continue to show me stores near me.

Let's see how it works. When I connect, both sites see incoming connections from an IP address that geolocates to my general area. But there are several possible locations of Private Relay IP addresses that are shared by everyone in the region.

![Information accessed by the website server in Private Relay. Source: Apple](/privaterelay07.png)

When the "Use Country and Time Zone"[^8] option is selected in the iCloud Internet Privacy options, no hint is given to the Egress Proxy.

So an IP address is chosen from the group that represents the entire region belonging to the Ingress Proxy. As a result, websites will see connections made from an extensive regional area. The same set of IP addresses is used for everyone in the region.

![IP selection based on the area in Private Relay. Source: Apple](/privaterelay08.png)

With the generalized location setting, the lawnmower website now sees a random location, which for me could be places like Los Angeles instead of Cupertino."

Up to here are the facts (information provided by Apple itself), from now on everything is interpretation and opinion.

Private Relay is a service included in iCloud+[^9], therefore, it's not a public service. So it's necessary to give permission to the user to access it. The problem is that permission must be given without identifying the user, to continue maintaining their privacy. To solve this, Apple uses an access token server. Based on the information provided, I'm going to try to explain how they are created in a simplified way:

1.	Your device generates a session token for your iCloud account in which you maintain the session logged in using a function and a random number.
2.	Your device requests the public key from the Private Relay access token server.
3.	Your device uses the function, the random number, and the public key it has obtained to create a "blind" session token. No one can verify that this token is associated with your account.
4.	Your device sends the blind session token and your iCloud authentication to the Private Relay access token server.
5.	The Private Relay access token server, once your iCloud authentication is verified, signs the blind session token and sends it to your device.

This procedure is performed several times, which provides your device with a set of blind session tokens. When you want to use the Private Relay service, the following happens:

1.	Your device communicates with the corresponding Private Relay proxy using one of the previously obtained blind session tokens.
2.	The proxy your device has connected to requests the public key from the Private Relay access token server.
3.	With the obtained public key, it verifies that the blind session token contains a valid signature and allows your device access to the service.

Therefore, the service can be used without identifying you as a user. To make a comparison, it's as if we bought a few car wash tokens. The company that sold us those tokens can't know when we'll use them or where. Not even how many we've used because they don't know how many we still have in our possession. However, we can use the service to wash the car whenever we want. This procedure is not new, for example, Google One also uses a similar one to allow access to its VPN. You can read more information about blind RSA encryption in [this article by Cathie Yun](https://cathieyun.medium.com/adventures-with-rsa-blind-signing-397035585121).

This is when the Private Relay service truly begins to function. I'm going to limit myself to making a simplified proposal of how it could be implemented using a simple public and private key scheme. The starting premise is simple, each actor in the communication generates a pair of mathematically related keys so that what is encrypted with one of the keys would be decrypted only with the other. But there is no way that, having one of the keys, the other can be obtained. In this case, four agents intervene:

-	User's device. It generates its private key (SU) and its related public key (PU). Unique for each connection.
-	Ingress Proxy. It has a private key (SI) and its related public key (PI).
-	Egress Proxy. It has a private key (SE) and its related public key (PE).
-	Website server. It has a private key (SS) and its related public key (PS).

When we make a request to a web server in Safari[^10] (once the DNS is resolved) the following would happen:

1.	Our device, using one of the session tokens, requests from the Private Relay service two random proxy servers (one ingress and one egress) and their respective public keys (PI and PE).
2.	Our browser encrypts the content of the request along with its public key (PU) using the public key of the web server (PS). Basically, this is what HTTPS encryption does.
3.	It re-encrypts the above, masking the destination IP of the request (that of the website server) and adding another session token and its public key (PU), with the public key of the egress proxy (PE).
4.	Again it re-encrypts the above, adding another session token and the IP of the chosen egress proxy, with the public key of the ingress proxy (PI).

![Scheme of the request packet with all layers encrypted on the client](/propuestaprivaterelay01.png)

5.	Now it sends the packet with all its encryption layers to the IP address of the ingress proxy.
6.	The ingress proxy decrypts the first layer with its secret key (SI) and verifies with the public key of the access token server that the token is valid. Then, it geolocates the user's IP and assigns it an approximate extensive zone.

![Scheme of the request packet with the ingress proxy layer decrypted](/propuestaprivaterelay02.png)

7.	It sends the packet with the rest of the layers and the approximate zone to the egress proxy whose IP it has decrypted using one of its ports (and recording that the communications of that port belong to the user's IP).
8.	The egress proxy records the source port of the request and maps it to another of its ports, through which it will forward the request. It decrypts one more layer with its private key (SE) and obtains the destination IP (that of the website server) and an access token. It verifies the access token and chooses a random IP from the zone indicated by the ingress proxy. It sends what's left of the packet, using that chosen IP as the source, to the website server.

![Scheme of the request packet with the egress proxy layer decrypted](/propuestaprivaterelay03.png)

9.	The website server decrypts the content of the request using its private key (SS), obtaining the user's public key (PU). This is specific to HTTPS encryption.

![Scheme of the request packet with all layers decrypted on the web server](/propuestaprivaterelay04.png)

10.	The website server processes the request and encrypts the response using the user's public key (PU), sending it back to the egress proxy. This step also belongs to the HTTPS protocol.

![Scheme of the response packet with the first layer encrypted on the web server](/propuestaprivaterelay05.png)

11.	The egress proxy receives the response through a port that it has registered with another (through which it received the request from the ingress proxy). It encrypts the response along with the source IP (that of the website server) using the user's public key (PU) again and sends it through the registered port.

![Scheme of the response packet with the second layer encrypted on the egress proxy to hide the web server IP](/propuestaprivaterelay06.png)

12.	The ingress proxy receives the packet through a port that it has registered with a source IP (that of the user), and to which it forwards the packet.

![Scheme of the response packet with the second layer encrypted on the egress proxy passing through the ingress proxy](/propuestaprivaterelay07.png)

13.	The user's browser receives the packet. It decrypts the first layer with its private key (SU) and verifies the origin of the response (IP of the website server).

![Scheme of the response packet with the second layer decrypted on the client](/propuestaprivaterelay08.png)

14. It now decrypts the second layer with its private key again (SU), obtaining the server's response.

![Scheme of the response packet with all layers decrypted on the client](/propuestaprivaterelay09.png)

In this communication:

-	The user's browser obtains the desired response from the website.
-	The ingress proxy only knows the user's IP, but not the destination of the request.
-	The egress proxy knows the destination of the request, but not the user's IP, since the IP it has access to is that of the ingress proxy.
-	The website server responds to a request generated by a random IP chosen by the egress proxy. The next time the same user makes a request, it will do so from another IP in the same zone, so it cannot associate it with a commercial profile.
-	The internet service provider (ISP) only knows that the user has established communication with a Private Relay ingress proxy, but not what site they have visited.
-	If the user also checks the "Use Country and Time Zone" option, the IP that the website server can see won't even correspond to the approximate zone where they're actually located.

It's quite possible that they have somehow simplified the processes to maintain privacy while also having good browsing performance. As several of these technical details are still unknown, I warn again that this is only a proposal on how Private Relay could work approximately with the data that has been revealed so far.

Personally, I think it's one of the most interesting novelties of this WWDC. Keep in mind that there are approximately 1.5 billion active Apple devices in the world. Many of them will have this configuration by default when accessing the internet. And that's one of the problems that trackers, advertisers, and service providers who wish to maintain control over the websites we visit will have. It's privacy by default, without the need to be advanced users, which makes the difference. However, not all countries will be able to use this service. Starting with China, [Apple has declared that the service will not be active for now in a total of ten countries](https://www.reuters.com/world/china/apples-new-private-relay-feature-will-not-be-available-china-2021-06-07/). Why? Because the legislation of these countries does not allow not knowing the web browsing of their citizens. And why doesn't Apple, if it carries privacy as a banner, put up resistance? Because one thing is ethics and privacy, and another very different is money. And each one has their priorities.

If you liked the article, I advise you to check out [this DekkaR podcast](https://web.archive.org/web/20210610104004/https://www.spreaker.com/user/dekkar/icloud?autoplay=1). And if you like these topics, don't stop following him on [Twitter](https://twitter.com/DekkaR) and [Telegram](https://t.me/DekNet).

If you know any other system different from those mentioned that uses a similar method, don't hesitate to leave a comment. And don't hesitate either if you simply want to leave one.

I'm off to get my blind token.

[^1]: WWDC (WorldWide Developer Conference) is Apple's annual event where they announce new products and features for developers and users.

[^2]: DNS over HTTPS (DoH) is a protocol for performing DNS resolution via the HTTPS protocol, enhancing privacy and security in web browsing.

[^3]: TOR (The Onion Router) is a network that enables anonymous communication by directing internet traffic through a worldwide overlay network of servers.

[^4]: Ingress Proxy in Private Relay is the first server that receives the user's connection, hiding their IP from other servers.

[^5]: Egress Proxy in Private Relay is the second server that forwards the user's request to the internet, preventing the Ingress Proxy from knowing the destination.

[^6]: Blind RSA signatures are a cryptographic technique that allows signing a message without seeing its content, enhancing privacy.

[^7]: The Bay Area, California refers to the San Francisco Bay Area, a region known for its high concentration of tech companies and startups.

[^8]: "Use Country and Time Zone" is a privacy option in Private Relay that further generalizes the user's location information.

[^9]: iCloud+ is Apple's premium cloud storage and privacy service that includes features like Private Relay.

[^10]: Safari is Apple's web browser, available on iOS and macOS devices.