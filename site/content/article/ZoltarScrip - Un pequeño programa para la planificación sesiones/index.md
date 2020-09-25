---
title: "ZoltarScript: Un pequeño programa para la planificación sesiones"
date: 2020-09-25T19:00:00+02:00
description: "¿Te gustaría saber de un vistazo qué clase tienes a continuación y qué tienes planificado hacer en la misma?"
images:
- featuredimage.jpg

twitter:
  card: "summary"
  site: "@handle"
  title: "ZoltarScript: Un pequeño programa para la planificación sesiones"
  description: "¿Te gustaría saber de un vistazo qué clase tienes a continuación y qué tienes planificado hacer en la misma?"
  image: "https://davidlms.com/article/imagina-una-aplicaci%C3%B3n-ideal-para-planificar-y-mejorar-las-sesiones-de-clase/featuredimage.jpg"

tags: ['zoltar', 'sesiones', 'docencia', 'script', 'calendario', 'productividad']
categories: ['Pequeños programas']
author: "David Romero"
noSummary: true

resizeImages: false
---
La semana pasada estuve [imaginando una aplicación ideal para planificar y mejorar las sesiones de una formación](https://davidlms.com/article/imagina-una-aplicaci%C3%B3n-ideal-para-planificar-y-mejorar-las-sesiones-de-clase/). Como no la encontré, decidí crear un **pequeño script** que pudiera utilizar para ese propósito.

Aunque tiene **muchos defectos y limitaciones**, porque no le podido dedicar más que el tiempo justo, de momento **cumple decentemente** con la mayoría de cosas que buscaba para planificar el curso. Realiza únicamente dos funciones:

- **Genera todas las sesiones de una asignatura para todo un curso**. Indicando una fecha de inicio de curso, otra de fin de curso, los días festivos y los días y horas de la semana en los que hay una sesión de la clase, **muestra todas las sesiones que habrá a lo largo del curso**, creando una fila por cada una con el número de sesión, la fecha, el día de la semana y la hora concreta. En la fila de cada sesión hay una columna para planificar **qué se hará en la misma**.
- **Traslada todas las sesiones de la asignatura a un Calendario de Google**, incluyendo el desarrollo de esa sesión **en la descripción** del evento. De esta manera, teniendo el calendario sincronizado, **puedo consultar qué tengo que hacer** en la próxima sesión **en todo momento**, mirando en el reloj, la tablet o el ordenador. También se puede exportar en formato .icalc, por si quieres llevártelo a tu aplicación favorita.

Todo se realiza en una Hoja de Cálculo de Google, ya que es un formato muy fácil de manipular. Para el próximo curso simplemente puede copiarse la columna de las sesiones en las nuevas sesiones que se generen, teniendo en cuenta los comentarios que se hayan puesto para mejorarlas.

**¿Te gustaría probarlo para planificar tus clases?** Puedes hacerlo siguiendo las instrucciones que encontrarás en el [repositorio del proyecto](https://github.com/DavidLMS/ZoltarScript).

**¿Te ha sido útil y quieres colaborar con el proyecto?** Puedes hacerlo de distintas formas:
- Escribe un comentario, constructivo siempre, en esta publicación.
- [Crea un issue para proponer una nueva función o indicar un error](https://github.com/DavidLMS/ZoltarScript/issues).
- [Mejora el script y solicita un pull request](https://github.com/DavidLMS/ZoltarScript/pulls).
- [Invítame a un café](https://ko-fi.com/davidlms).
