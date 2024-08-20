---
title: "Apple's Possible AI Strategy"
subtitle: ""
description: "The dots only connect looking backwards"
date: 2023-08-26T09:32:00+02:00
lastmod: 2023-08-26T09:32:00+02:00
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
tags: ['opinion', 'artificial intelligence']
categories: ['More technical things']
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
---

**Important**: Translated automatically from Spanish by [🌐💬 Aphra 1.0.0](https://github.com/DavidLMS/aphra)

Undoubtedly, in recent years we've been experiencing **a tsunami of innovations in what's known as Generative Artificial Intelligence**, which are nothing more than trained models to generate texts, images, videos, voices, music, and other types of content.

Several [media outlets](https://www.bloomberg.com/news/newsletters/2023-04-18/is-apple-falling-behind-in-the-ai-race-against-microsoft-google-amazon) have pointed to Apple as **the major tech company absent** in this race towards who knows where (AGI, [according to some](https://openai.com/blog/planning-for-agi-and-beyond)). This accusation was particularly pronounced after the last [WWDC 2023](https://developer.apple.com/wwdc23/), where the big star was the Apple Vision Pro and the "new" concept of spatial computing. Many voices indicated that Apple had lost its "vision" (how ironic) by not jumping on the AI train and maintaining course towards XR, when Meta "had shown it was a dead end". This XR topic would warrant another article, so for now I'm not going to explore that path and I'm going to focus on the AI trail.

The defense attorneys argued that Apple isn't watching this wave from the shore, **that it has been applying AI in its devices and applications** for a long time. In fact, it has a [Machine Learning](https://machinelearning.apple.com) portal where it shares different research in this field. But this doesn't convince the prosecution bench, who don't see any "Copilot" in sight from Apple. The problem is that the concept of AI has become **too big a bag**. Right now everything can be AI or nothing can be. It seems that each person has a different idea of what this concept means in their head. So let's try to indicate very specifically what we mean when we talk about AI or we'll never understand each other in life. In the rest of this article, AI will be equal to "Machine Learning or Deep Learning models trained to generate content, specifically I'm going to focus almost exclusively on large language models (LLMs) like [GPT-4](https://openai.com/gpt-4) or derived technologies like Copilot".

Without any intention of positioning myself **in defense** (Apple if you want to pay me for an article let's talk) **or in attack** (Microsoft/Meta/Google if you want to pay me for an article let's talk) of this company, it seemed to me that it would be an interesting analysis exercise to speculate about the path Apple could follow to integrate this technology into its ecosystem. Everything you find in this article that isn't linked to a source of information **is a subjective opinion**.

Before beginning, I think it's important to do **a review of the current positions of some of the competing companies** in this aspect:

- [OpenAI](https://openai.com) alias "**L'Enfant Terrible**"[^1] (the troublemaker), the protagonists of the movie. First with [DALL·E 2](https://openai.com/dall-e-2) and then with [ChatGPT](https://chat.openai.com) (GPT-3.5 at its release). They wanted to be very open, but then [they haven't been so much](https://www.lunasec.io/docs/blog/openai-not-so-open/). At least they seem to show concern for doing things right and are allocating many resources to understand how LLMs work and how to align them with "human values" (theirs, I suppose). They're forgiven for gifts like [Whisper](https://openai.com/research/whisper).
- [Meta](https://ai.meta.com) alias "**Mark's Latest Pit Stop**", or the weathervane pushed by the wind. They pivoted the entire company towards Virtual Reality and then with another sharp turn started to put a lot of emphasis on Artificial Intelligence. Maybe they'll change the name again. AGI-le suits you, think about it. I don't quite understand the business strategy in this regard, but the fact is that they're giving away very good open models, like [SAM](https://segment-anything.com) or [Llama 2](https://ai.meta.com/llama/). I'm increasingly convinced that Mark Zuckerberg's main interest is to go down in history for something more than a social network that manipulates people. And he's willing to follow all possible paths to achieve it.
- [Microsoft](https://www.microsoft.com/es-mx/ai) alias "**The Patron**", has much to gain and little to lose. Satya Nadella's strategy has been and continues to be the cloud (Azure) and getting into all companies with the Office suite. Artificial Intelligence is nothing more than a new Trojan Horse[^2] to give a push and continue achieving their goals. They invest in OpenAI's technology in exchange for two great advantages: having priority in using it in their products and having it run on their infrastructure. Freeing themselves in turn from two disadvantages faced by companies based on Generative Artificial Intelligence technologies: That some competition gets ahead of them or that prestige problems arise due to controversies related to the responses of these models and/or the decisions that are made as a consequence. They also play on several fronts, [presenting Meta's flagship language model at their own event](https://blogs.microsoft.com/es/blog/2023/07/18/microsoft-and-meta-expand-their-ai-partnership-with-llama-2-on-azure-and-windows/). Which, of course, can be easily executed on Azure. Whoever wins this war, Microsoft has all the cards to not be left out of the winning team.
- [Google](https://ai.google) alias "**All Talk, No Action**", or could have been but not yet. Not long ago Google covered all the headlines that had to do with Generative AI research. Even without letting anyone try any of their models, the results they showed left us open-mouthed. But the competition got ahead. While OpenAI focuses on the development of AI models and Microsoft on infrastructure and incorporating those models into their products, Google has to take care of everything. Worrying at the same time about not cannibalizing or destroying their main lines of financing. Quite a challenge. That's why the joining of forces between [DeepMind](https://www.deepmind.com) and [Google Brain](https://research.google/teams/brain/) is easy to explain. May the force be with you.
- [Nvidia](https://www.nvidia.com/es-es/ai-data-science/) alias "**De Cryptobro a IAbro**"[^3] (From Crypto Bro to AI Bro), or [the Wheat Lords in a World of Bakers](https://www.xataka.com/robotica-e-ia/hay-ganador-absoluto-industria-ia-se-llama-nvidia-esta-ganando-dinero-que-nunca). Most of the infrastructure that trains or executes Artificial Intelligence models does so on cards manufactured by Nvidia. This puts it in a privileged position that adds to those it already has on gaming or cryptocurrency mining (lately diminished). Therefore, it has all the tickets to be a clear winner in the coming years. Of course, several companies have already begun to create their own designs, so they can't rest on their laurels... Lest they become the new Intel.

There are other smaller companies that I think are worth mentioning:

- [StabilityAI](https://stability.ai) alias "**The Linux of GenAI**"[^4], the true Open Source replacement for OpenAI. They're having some little problems that I hope they solve, because the contribution of their models is key to allowing anyone to use this type of powerful technology without limitations.
- [Anthropic](https://www.anthropic.com) alias "**ChatGPT's Rival**", it's always good to have competition. Their models based on Claude have some aspects that improve what OpenAI currently offers, although they work worse in others. Clear candidate to end up being acquired by one of the big ones.
- [Hugging Face](https://huggingface.co) alias "**The Open Source Engine**", the dream come true for those who like to tinker and test all the novelties. This web portal provides everything necessary: datasets, models and easy-to-create and use interfaces to execute them. There's no open model you want to try that isn't available in one click on Hugging Face, often even on the same day of its release. Is it very noticeable that I love this organization?
- [Humane](https://hu.ma.ne) alias "**The Magic Leap of AI**", they're close to releasing a personal device that supposedly truly harnesses the potential of AI, being the first of what they call contextual computing. I'm sorry, but it reminds me too much of the hype that was given to Magic Leap when XR was the fashion, which promised to have something in hand that "would bring magic to reality". And after a long wait they released something similar to what was on the market at that time. I hope I'm wrong and Humane releases a truly disruptive device that improves people's lives and their relationship with technology.
- [xAI](https://x.ai) alias "**Elon Musk**", little more to say, Elon Musk's umpteenth project to save the world after calling for a pause in AI development. I mention it simply to brown-nose a bit, now that he's just removed the block he had put on my domain on Twitter (now X). Of course, having all the data from the social network, he has the potential to create the most toxic language model of all.

Now I think we're at the ideal point to put ourselves in Apple's shoes from the moment OpenAI dropped the bomb that **we still haven't finished reacting to**.

ChatGPT appeared in our lives on November 30, 2022. And, except for Microsoft, which obviously had privileged information, it caught the rest of the big tech companies wrong-footed. Apple too. And by this I don't mean that they didn't have any kind of research in this regard or anything like that. It was simply an unexpected event. **An event that was the seed** for the general public to then expect some kind of movement on their part at WWDC 2023. In fact, it's more than likely that they discussed it at [the internal event they held on AI](https://appleinsider.com/articles/23/02/07/apple-to-hold-first-in-person-ai-summit-in-years). But of course... Apple isn't Google.

You know what happened next. The answer was visionOS[^5]. Despite some [differences of opinion within the company](https://www.cnbc.com/2023/05/18/report-apple-execs-skeptical-on-headset-calling-it-science-project.html), the new Apple Vision Pro device was presented. For now, we don't know if the initial intention was to show it at this event or if they simply decided to bring it forward because they needed to present something that truly caught attention. The narrative was likely: "We're not presenting anything that competes with GPT-4 and derived technologies, but we make up for it with something you've been waiting for for a long time". Or maybe, simply, the initial investment in the product required showing it now so that developers could start creating applications and thus be able to monetize it in the future.

However, if you pay enough attention, Apple left us **some clues** at that event to confirm that they're working on it. Look at this capture from the main conference:

![A Transformer language model](/modelo-transformer.png)

Wait... A Transformer language model? Well... Like GPT (whose initials stand for Generative Pre-trained Transformer). At that moment they were talking about improvements in autocorrection and autocomplete functions. They could have simply said that they've improved them (in fact, it's the kind of thing that probably in any other conference they wouldn't have dedicated even five seconds to), but **they explicitly indicate** that it's a Transformer model. It can't be a coincidence. This is a simple GPT model from Apple. Which yes, obviously it's far from GPT-4. But watch out, it runs on the device and every time a keyboard key is pressed. Not enough with that, they pronounced the key word again right after:

![Voice recognition based on Transformer](/basado-transformer.png)

Transformer again... Now in dictation (Has anyone "whispered" something?). It's evident that this is the way Apple has chosen to **send us a clear message** in the conference: This technology is not unknown to us and we've been working on it for a while.

But that message didn't get through. Or at least that's what I think from the reactions to WWDC. If it weren't so, it wouldn't have been necessary a few days ago [to leak that they were working on it explicitly](https://www.xataka.com/robotica-e-ia/apple-gpt-empresa-cupertino-trabaja-ia-para-competir-openai-google-gurman). Of course, it was obvious that they're not blind or deaf. Especially after [prohibiting their employees from using ChatGPT](https://www.genbeta.com/actualidad/apple-prohibe-uso-chatgpt-otras-inteligencias-artificiales-a-sus-trabajadores-documento-interno). As a company, you have to provide an alternative because otherwise you risk a lot if you leave your employees without that productivity boost. Leaving that aside, the reflection that has led me to write this article comes precisely in the wake of that leak. Because in it, it's indicated that Apple still isn't clear on how to bring that technology to consumers and, as it's expressed, it seems to be due to a lack of ideas.

Let's see... Lack of ideas? Here are a few:

- A Siri that finally knows what we want it to do.
- A code copilot in Xcode.
- Textual reports that interpret the Health app measurements in a personalized way.
- Create Shortcuts just by describing the behavior we want them to have, without having to learn how to use the app.
- Meeting and notes summaries.
- Search for answers in our files.

If I can come up with a few useful uses thinking on the fly in less than a minute, I don't want to imagine **the number of ideas they might have noted down** in Cupertino.

The obstacles have to be others. My opinion is that Apple faces **two important problems** to deploy a model as powerful as GPT-4 in its ecosystem:

- **Cloud computing**. Not having its own server farm infrastructure (that can offer services to consumers), Apple depends on other distributors, making its use much more expensive, losing freedom of action, reaction and, of course, privacy.
- **Non-determinism**. The responses and generations of these models are probabilistic. The same input at two different times does not produce the same output and, therefore, it's very difficult to limit the responses they can give. This clashes head-on with Apple's need for control over how its devices act and react. Something fundamental to keep its philosophy alive. Can you imagine an Apple device saying some barbarity or performing an action not initially foreseen by the company? Well, this is a difficult problem to solve in large language models, [vulnerable to Prompt Injection techniques](http://www.elladodelmal.com/2023/08/como-lograr-que-llama-2-bard-ai-chatgpt.html) and reaching intermediate objectives that their creators hadn't foreseen.

The key to solving the first problem has a name and surname: [**Neural Engine**](https://observatorio-ia.com/apple-neural-engine-procesador-ia-moviles-apple)[^6]. Very briefly, it's a chip that allows Artificial Intelligence (Machine Learning) models to be executed efficiently on the device that integrates it. Apple started putting them in iPhones in 2017 and they're currently in their entire range of devices that have (or can be connected to) a screen. After its release, they've been improving it year after year. Despite not being comparable to the execution power that can be achieved in a data center, it has three advantages:

- **Data doesn't leave the device**. Privacy has always been a priority at Apple. If the model is executed by the device itself, it's not necessary to send any data over the Internet as it must be forcibly done in the case of cloud-executed models. I've always thought that it has been very convenient for Apple not to have businesses that depend on data collection, to the point of not knowing if privacy was a sought-after value or simply a welcome consequence. It's not that it's all a matter of chance, because it has made many independent advances in privacy, but how well this advantage fits as a result of a great disadvantage such as not having its own data centers. When AI is integrated with operating systems, this advantage will be even greater. While Windows and Linux-based systems like Android will have a hard time controlling the local execution of models (due to the different hardware configurations they run on), Apple will be able to know exactly how fast each model can run on each of its devices. That's why Microsoft's strategy will probably pass, at least in the medium term, only through the cloud. Which also suits it very well to increase Azure's revenues.
- **The ecological footprint is reduced**. One of the most heard criticisms about Artificial Intelligence models is that their processing requires much higher power than other simpler operations, with the corresponding increase in consumption. Simplifying a lot, the presence of a new wave of powerful models running on servers means higher energy expenditure, as has already happened with the rise of cryptocurrencies. If those models are executed locally on a device they must have a more moderate and efficient consumption, because nobody wants the battery to only last an hour. Therefore, it guarantees that work is done in that line. In addition, Apple's new computers have a much lower consumption than most of their competition, thanks to their Apple Silicon[^7] architecture.
- **Offline execution**. Obviously if the models are executed on the device itself, an Internet connection won't be needed, with the advantages that entails when we don't have coverage or a data connection. But not only that, by not depending on a cloud service, it's also not possible for the service to be down or inaccessible at some point, as has already happened on some occasions with ChatGPT for example.

The second problem is the one I see as more complex to solve at the point we're at. Apple needs its language model **to be aligned with "the values" of the company**. This is much easier said than done, [OpenAI already dedicates 20% of its computation](https://openai.com/blog/introducing-superalignment) to solving that problem. I don't think we'll see a ChatGPT-type application from Apple. First, because I don't see any sensible use within its ecosystem. But, in case they find it, it won't be available until the alignment issue is resolved. That doesn't mean there isn't a much more interesting intermediate solution: **using the model to "understand" what the user wants to do**. We can already see this in ChatGPT through its plugins. It seems like magic (but it's not): you activate the plugins, ask for something and the model knows what and how it should interact with other systems to get the answer you need. This would allow, for example, making a request to Siri about some HomeKit[^8] accessory without needing to give the exact order for it to work. As the output is not a text, but an action, we eliminate the problem of the response not being aligned with their values. It will also allow creating a new type of user experience in applications, because **it won't be necessary to learn how to use them**: it will be enough to indicate the result we want for the model to execute the necessary actions for it. Along these lines, we already have libraries working, such as the recently released [TypeChat](https://microsoft.github.io/TypeChat/) by Microsoft. The possibilities are endless. We're approaching a point where the limit is more in our imagination than in technology.

Taking into account the problems I've exposed, **what would I do if I had to set Apple's strategy regarding AI?**

- **Continue investing in Neural Engine design**. Every euro well spent will be worth it. The cornerstone on which the strategy must be built. Because thanks to the hardware and software integration that no other company has, it can provide added value that would take years for the competition to match. As is happening with the Apple Silicon architecture.
- **Tests, brainstorming that lead to more tests and hiring talent**. Surfing the AI wave doesn't just mean releasing products that use it, it's also about being attentive. Reading about the novelties and trying out the different solutions that appear. Put teams to think, devise and test different ways to leverage the technology and integrate it into the ecosystem. I'm sure they're already doing this, just as they were testing different A processors on a Mac until their performance was decent enough to become the M1. But all this must go hand in hand with hiring talent and having the best. I'll leave it there.
- **Wait for Open Source to provide me with solutions**. The new Llama 2 model is completely open. But it has two limitations: its dataset can't be used to train another model and it can't be used commercially if you have more than 700 million active users. Training a model like Llama 2 costs 20 million. Not many companies can afford that budget if it doesn't involve some kind of direct reinvestment. There aren't many that have more than 700 million active users either. But the iPhone has about 1000 million. Very similar numbers... Coincidence? Or that Meta hasn't wanted to give any advantage that it knows it has been giving by releasing other models like Segment Anything (SAM)?
- **Rethink the entire user experience of my operating systems and applications (UX)**. Did you know that macOS can be fully controlled using only voice? It's not comfortable at all, but it works and these new technologies can be the final touch to banish keyboard and mouse to very specific professional uses. At Apple they have experience in creating engaging interactions: they did it with the iPod wheel, with the first iPhone's touch screen and I bet they'll do it with the view and gestures of visionOS. But at some point, someone will redefine everything we know about UX using Artificial Intelligence. Will they be interfaces that automatically adjust to the knowledge and skills of each user? Will menus and buttons disappear and there will only be a text input (that has the possibility of being written using voice)? Maybe we'll only need an interpreter of our brain waves to make requests to devices? Will it be a mix of everything and we'll have several options at our disposal to choose from? Nobody knows yet, but what I'm sure of is that some person or entity will go down in history for giving the right solution to the new user experience applying these technologies.

For all the above reasons, I don't think Apple will show anything totally revolutionary in AI in the short term. Functionalities will arrive very gradually, probably behind the competition, but with a different approach. Until, one day, suddenly, everything will have changed. Because so far Apple has had a Gandalf-like lifestyle[^9]: **it doesn't arrive late or early, but exactly when it intends to**. And we have no clue that this is going to change soon.

This is my opinion about the problems and possible solutions that Apple may have on the table regarding its strategy regarding Generative Artificial Intelligence, specifically, about large language models and their applications. But obviously no exact and error-free prediction can be made until things happen. As Steve Jobs said, "You can't connect the dots looking forward; you can only connect them looking backwards". In any case, we are expecting at least **a few interesting, transformative and to some extent terrifying years in the technology sector**.

**Thank you for reading** and getting this far.

PS: No AI was harmed in the writing of this article... But it was for generating the image that illustrates it.

[^1]: "L'Enfant Terrible" is a French expression referring to a troublemaker or disruptive figure in a field, often used to describe innovative but controversial entities.

[^2]: "Trojan Horse" is used metaphorically here to describe a strategy that appears beneficial but is designed to achieve a different, often advantageous, outcome for the initiator.

[^3]: "De Cryptobro a IAbro" is a Spanish wordplay combining "Cryptobro" (cryptocurrency enthusiast) and "IAbro" (AI enthusiast), highlighting Nvidia's shift from cryptocurrency to AI dominance.

[^4]: "GenAI" stands for Generative Artificial Intelligence. The comparison to Linux emphasizes StabilityAI's open-source nature in the AI field.

[^5]: visionOS is Apple's operating system for their augmented reality headset, Apple Vision Pro.

[^6]: Neural Engine is Apple's AI chip designed for efficient on-device machine learning processing.

[^7]: Apple Silicon refers to Apple's custom-designed processors used in their Mac computers, replacing Intel processors and offering advantages in performance and energy efficiency.

[^8]: HomeKit is Apple's smart home ecosystem, allowing users to control various smart home devices through Apple products.

[^9]: This refers to a quote by Gandalf, a character from "The Lord of the Rings," known for arriving precisely when needed, neither early nor late.