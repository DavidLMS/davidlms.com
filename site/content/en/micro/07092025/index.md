---
title: "BananaMD"
date: 2025-09-08T12:25:00+02:00
platform: "X"
external_url: "https://x.com/davidlmsEN/status/1964817258347384889"
tags: ["x", "micro"]
---

This weekend I participated in [Google DeepMind’s Nano Banana Hackathon](https://www.kaggle.com/competitions/banana/).

The result is BananaMD, a web application for illustrating Markdown files (slides, documents…) with generated images. In recent years I’ve created all my teaching materials in this format and I like them to be accompanied by images, even if most are purely illustrative.

I also usually prefer to change them from one course to another. But thinking up the prompt, generating them, linking… It takes quite a bit of time.

BananaMD automates much of this process, generating two options to choose from for each image, with the ability to edit them with a simple instruction and maintaining a reference style.

It can update and make new proposals for existing images, but also create them from scratch, either from a description you’ve left or by creating one that’s coherent with the text where it’s located.

Finally, it allows you to download the new Markdown with properly linked images and good descriptive text in the “alt” field.

I was only able to dedicate a very specific time window to it, and the presentation video result is very much improvable, but [here it is](https://www.youtube.com/watch?v=7Lcjq8qfSRU).

For the more technical folks, some details: Google’s generative AI has been present throughout the entire project. The design, created with Stitch.

The code was pure vibe coding. I started creating it with AI Studio’s builder, to finish using Gemini CLI. The first images in the video, evidently, are a product of Veo 3.

If anyone wants to try it or know a bit more, [here’s the project repository](https://github.com/DavidLMS/bananamd).