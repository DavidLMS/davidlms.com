---
title: "En busca de un formato para las guías prácticas: CodeLab"
date: 2021-07-11T18:36:00+02:00
description: "Crea guías técnicas atractivas, de fácil navegación y adaptables al futuro"
images:
- featuredimage.png

twitter:
  card: "summary"
  site: "@handle"
  title: "En busca de un formato para las guías prácticas: CodeLab"
  description: "Crea guías técnicas atractivas, de fácil navegación y adaptables al futuro"
  image: "https://davidlms.com/article/private-relay-la-soluci%C3%B3n-definitiva-para-el-anonimato-en-internet/featuredimage.png"

tags: ['codelab', 'guía', 'práctica', 'página web', 'interactividad', 'responsive']
categories: ['Recursos']
author: "David Romero"
noSummary: true

resizeImages: false
---

Siempre ocurre lo mismo.

Cuando me dispongo a crear algún tipo de material didáctico, como una guía práctica, ronda la misma pregunta en mi cabeza: **¿En qué formato la realizo?**

Puede parecer una pregunta trivial, quizás deba centrarme únicamente en el contenido, pero la realidad es que no lo es.

Por un lado, me interesa que el formato **perdure lo máximo posible**. Crear el material conlleva un tiempo y esfuerzo que ya no recuperarás, por lo que sería una pena hacerlo con una herramienta propietaria, que dependa de un servicio en la nube, y sobre la que no tienes ningún control. Aunque sean herramientas que se promocionan por todas partes y que estén de moda en el ámbito educativo. Quizás el resultado sea muy atractivo pero... ¿Depender de los intereses de una empresa para seguir accediendo a mi material? No, gracias. Por cierto, este argumento también incluye que sea fácil de cambiar y mantener en el futuro... Las guías prácticas en el ámbito de la informática tardan muy poquito en quedarse obsoletas.

Por otro lado, el formato, bajo mi punto de vista, debe ser **atractivo, adaptable a todo tipo de pantallas y de fácil navegación** a través del mismo. Al fin y al cabo, si conseguimos que el alumnado quiera pasar tiempo en el contenido, probablemente se acercarán más a nuestro objetivo de aprendizaje.

Hasta ahora, me he decantado por crear las guías con **Markdown y generar una página HTML** del mismo. Puedes comprobar el resultado en [esta guía que adapté sobre WireGuard](https://davidlms.github.io/Practicas/SERRED/wireguard). Así, he estado cumpliendo con los principios que más favorecen al creador del contenido: formato perdurable y fácil de mantener. Ahora... Atractivo, lo que se dice atractivo, no es. Fácil de navegar a través del mismo... Bueno, tiene una tabla de contenidos, pero no me parecía suficiente.

Así que me puse a investigar al respecto. De lo que he encontrado, me ha gustado mucho cómo crean guías prácticas en [Apple](https://developer.apple.com/tutorials/swiftui) y en [Google](https://developer.android.com/jetpack/compose/tutorial?hl=es-419&continue=https%3A%2F%2Fdeveloper.android.com%2Fcourses%2Fpathways%2Fcompose%3Fhl%3Des-419%23article-https%3A%2F%2Fdeveloper.android.com%2Fjetpack%2Fcompose%2Ftutorial). Por cierto, sospechosamente parecidas. Pero difícil de replicar. Hasta que di con los [CodeLabs de Google](https://codelabs.developers.google.com/). Y eso **sí me convenció**. Fácil de navegar y seguir, con secciones para no tener demasiado contenido a la vez en la página y adaptable a cualquier tipo de pantalla. Incluso permite al alumnado notificar de errores en la guía. Ahora solo falta que pueda replicarlo fácilmente, con un formato que perdure y fácil de mantener.

**Y existe**. Resulta que hay una comunidad de voluntarios que han creado una herramienta capaz de generar un sitio estático con una guía en formato CodeLab partiendo de un archivo Markdown. Y ahora la guía sobre WireGuard [luce así](https://davidlms.github.io/Practicas/SERRED/wireguard-ubuntu-server-20). Creo que estaréis de acuerdo con que la mejora es muy notable.

Como siempre, cuando os cuento algo no lo hago sin un objetivo. En este caso hay dos.

El primero, es que si conocéis herramientas similares que cumplan estos requisitos básicos y sean útiles para crear guías prácticas o material didáctico similar, sabéis que [me interesa que me lo contéis](mailto:hola@davidlms.com).

El segundo objetivo es enseñaros a vosotros también a crear estos CodeLabs si os ha gustado el formato. Para ello, he creado un [CodeLab sobre la creación de un CodeLab](https://davidlms.github.io/Practicas/crear-codelab). Únicamente es una adaptación del [original creado por Marc DiPasquale](https://www.marcd.dev/codelab-4-codelab), al que desde aquí le doy las gracias por permitirme adaptarlo al castellano.

Estoy deseando ver qué es lo próximo que vais a crear.