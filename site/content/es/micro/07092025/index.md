---
title: "BananaMD"
date: 2025-09-08T12:25:00+02:00
platform: "LinkedIn"
external_url: "https://www.linkedin.com/posts/david-romero-santos_github-davidlmsbananamd-generate-illustrations-activity-7370580448940466177-rF5M"
tags: ["linkedin", "micro"]
---

Este finde he participado en el [Nano Banana Hackathon de Google DeepMind](https://www.kaggle.com/competitions/banana/).

El resultado es BananaMD, una aplicación web para ilustrar con imágenes generadas un archivo Markdown (diapositivas, documentos…). En los últimos años he elaborado todo mi material didáctico en este formato y me gusta que vaya acompañado de imágenes, aunque la mayoría sean únicamente ilustrativas. También suelo preferir cambiarlas de un curso a otro. Pero pensar el prompt, generarlas, enlazarlas… Lleva bastante tiempo. BananaMD automatiza mucho este proceso, generándote dos opciones entre las que elegir para cada imagen, con la posibilidad de editarlas con una simple instrucción y manteniendo un estilo de referencia. Puede actualizar y hacer nuevas propuestas de imágenes existentes, pero también crearlas de cero, ya sea a partir de una descripción que hayas dejado o creando una que sea coherente con el texto de la ubicación en la que se encuentra. Finalmente, te permite descargar el nuevo Markdown con las imágenes correctamente enlazadas y con un buen texto descriptivo en el campo “alt”.

He podido dedicarle una ventana de tiempo muy concreta, y el resultado del vídeo de presentación es muy mejorable, pero [aquí está](https://www.youtube.com/watch?v=7Lcjq8qfSRU).

Para las personas más cafeteras, algunos detalles técnicos: La IA generativa de Google ha estado presente de forma transversal en todo el proyecto. El diseño, creado con Stitch. El código ha sido puro vibe coding. Empecé a crearlo con el constructor de AI Studio, para terminarlo usando Gemini CLI. Las primeras imágenes del vídeo, evidentemente, son producto de Veo 3.

Si alguien quiere probarlo o saber un poco más, este es el [repositorio del proyecto](https://github.com/DavidLMS/bananamd).