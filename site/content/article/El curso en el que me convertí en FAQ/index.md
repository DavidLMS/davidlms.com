---
title: "El curso en el que me convertí en FAQ"
date: 2020-12-31T14:16:00+02:00
description: "¿Cansados de escribir una y otra vez las mismas respuestas?"
images:
- featuredimage.jpg

twitter:
  card: "summary"
  site: "@handle"
  title: "El curso en el que me convertí en FAQ"
  description: "¿Cansados de escribir una y otra vez las mismas respuestas?"
  image: "https://davidlms.com/article/el-curso-en-el-que-me-convert%C3%AD-en-faq/featuredimage.jpg"

tags: ['FAQ', 'herramientas', 'comparativa', 'semipresencialidad', 'productividad', 'busqueda']
categories: ['Recursos']
author: "David Romero"
noSummary: true

resizeImages: false
---
No hace falta calcularlo. Este es el curso en el que más correos electrónicos he contestado. Y solamente ha pasado un trimestre. Uno de los efectos secundarios de la semipresencialidad supongo. Solo diré que el número de correos electrónicos con dudas recibido ha sido inversamente proporcional a la periodicidad con la que he publicado en el blog.

Y, conforme más respuestas daba, **más se repetían ciertos patrones**. Al final, escribía varias veces prácticamente lo mismo, lo cual no es nada deseable. De repente, me sentí como si fuera un FAQ. ¿Y por qué no hacer uno? No solo porque esté disponible para consulta y ahorre algún correo (mis ganas), sino por enlazar ciertas respuestas y así evitar redactar el mismo contenido de nuevo.

En ese contexto comenzó mi investigación. **Seguro que hay algo ya montado que pueda usar fácilmente**, pensé. Algo que cumpla más o menos con lo que busco, pensé. Y probablemente lo haya… Pero no he logrado encontrarlo, al menos no lo que tenía en la cabeza. Y eso no era más que un conjunto de cualidades deseables:

* **Open source**. De código abierto, así podría hacer pequeñas adaptaciones si fuese necesario.
* **Generación estática de la web**. Ya no solo porque la velocidad de carga sea la mínima, sino porque me permite que el hosting sea gratuito.
* **Respuestas enlazables**. Si el uso principal será responder a un correo, necesito poder obtener fácilmente un enlace a la respuesta concreta.
* **Respuestas desplegables**. Que se ofrezcan en forma de acordeón ([ejemplo](https://jqueryui.com/accordion/)), para no necesitar cargar una nueva página para cada una de ellas.
* **Fácil de actualizar**. Sería ideal que desde cualquier dispositivo pudiera añadir una nueva respuesta o hacer una edición a la página.
* **Con buscador integrado**. Sé que dificulta el hecho de que la página sea estática, pero hay opciones como Algolia.
* **Posibilidad de hacer nuevas preguntas**. Estaría bien que el alumnado pudiese sugerir nuevas dudas e incluso proponer respuestas.
* **Exportable**. Para que el trabajo hecho pueda migrarse fácilmente a otra plataforma si fuese necesario.
* **Estética**. Por pedir, que sea agradable navegar y permanecer en la página, así como que se adapte a distintos tamaños de pantalla.

Después de esto, **toca buscar**. Opciones hay muchas, y he probado cosas que no os pondré por aquí, por no alargarlo demasiado. Es importante diferenciar un simple FAQ de un software que nos permita crear una base de conocimiento, que no es lo que pretendía, por eso descarté opciones como [GitBook](https://www.gitbook.com/). También descarté probar plugins para Wordpress, que los hay y bastante interesantes, pero requiere demasiado mantenimiento para mi gusto, además de un hosting de pago. A no ser que lo haga de forma local y publique las modificaciones de forma estática, pero ya estaría limitando mucho la facilidad de actualización que buscaba. Una alternativa ligera a Wordpress que quiero mencionar es Ghost [con este tema](https://themeforest.net/item/digidocs-documentation-and-knowledge-base-ghost-theme/25719922), que aunque está más centrado en una base de conocimiento, me resultó una opción a considerar.

De entrada pensé en **un generador de sitios estáticos**, como Hugo, Jekyll o Gatsby con un tema preparado para ello. Encontré [Hugo FAQ Theme](https://themes.gohugo.io/hugo-faq-theme/) con muchas cosas que me gustaban, pero quedaba demasiado básico. También [unos cuantos de Jekyll](https://jekyllthemes.io/jekyll-documentation-themes), pensados sobre todo para bases de conocimiento. Y, entonces, casi por casualidad, me encontré con [esto](https://gatsby-theme-faqs.netlify.app/faq).

Pues **básicamente lo que buscaba**, sin más. Usa Prismic para alojar las preguntas, por lo que puedes actualizar desde cualquier dispositivo, Gatsby para generar la web y con un webhook configurar que se desplieguen automáticamente los cambios con Netlify. Es cierto que no permite sugerir nuevas preguntas y la exportación no es muy sencilla, pero oye, en estética y uso casi calcado a lo que tenía en mente. Sigo [las instrucciones](https://github.com/littleplusbig/gatsby-theme-faqs-prismic) para montarlo y… Error en la compilación. El proyecto lleva poco más de un año sin actualizarse, así que **me temo que algo se ha roto**. Si alguien controla de GraphQL y quiere arreglarlo, bienvenido será.

Ya más desmotivado opté por probar el sistema clásico de [phpMyFAQ](https://www.phpmyfaq.de/). Necesitas un hosting, pero quizás me proporcionara todo lo que buscaba. Es un proyecto que sigue vivo, y lleva mucho entre nosotros, pero sinceramente necesita una vuelta de tuerca. La estética y funcionalidad que tiene se ha quedado unos añitos estancadas en el pasado. Al menos para mi gusto. No obstante, si quieres personalizar al milímetro las opciones y **tienes tiempo para ello**, te animo a probarlo.

Y a mitad de camino me topé con [HAASH](https://haash.io/). Ni tan mal. Es verdad que no reúne muchos de los requisitos que buscaba, pero si necesitas **algo inmediato y extremadamente sencillo**, es tu solución. Te permite crear gratuitamente el número de FAQs que quieras, editarlos en la web directamente, establecer permisos, que el alumnado pueda proponer preguntas, con buscador integrado… Echo en falta una navegación que no requiera la carga de nuevas páginas (aunque he de admitir que es muy rápido) y, sobre todo, la opción de exportar el contenido. Por lo demás, quizás a ti te sirva.

Esta es mi forma de decir que, si conoces algún sistema que cumpla todo lo que quiero, no dudes en contactar conmigo. Y, por qué no, si estás buscando un proyecto web en el que **embarcarte para aprender**, lo suficientemente sencillo como para que una sola persona pueda llevarlo a cabo, aquí parece que hay un nicho. Una herramienta que genere, a partir de ficheros Markdown un sitio web tipo FAQ estático con categorías, buscador con Algolia, comentarios con Discuss... Ahí lo dejo.

No he querido que terminara este año sin dejar nada escrito por aquí. 

No he querido dejar pasar la oportunidad de desearte **un magnífico año nuevo, lleno de inquietudes, ilusiones, proyectos y buenas noticias**. No sabemos lo que nos traerá. Pero lo importante no es saberlo, sino **estar dispuestos** a adaptarnos a lo que venga.

**Hasta el año que viene**.