---
title: "Una guía para probar WireGuard con tu alumnado"
date: 2021-02-11T18:03:00+02:00
description: "Aprende a crear y configurar tu propio servidor VPN"
images:
- featuredimage.jpg

twitter:
  card: "summary"
  site: "@handle"
  title: "Una guía para probar WireGuard con tu alumnado"
  description: "Aprende a crear y configurar tu propio servidor VPN"
  image: "https://davidlms.com/article/una-gu%C3%ADa-para-probar-wireguard-con-tu-alumnado/featuredimage.jpg"

tags: ['wireguard', 'vpn', 'servicios en red', 'practica', 'seguridad', 'redes']
categories: ['Recursos']
author: "David Romero"
noSummary: true

resizeImages: false
---
**Vuelvo**, después de bastante tiempo. De hecho, este es la primera publicación del 2021. Y vuelvo, porque tengo algo que quizás os interese. Si no fuera así **no volvería**.

Hace unos meses, quizás algún año (mi percepción del tiempo empeora por momentos) escuché hablar por primera vez de **WireGuard**. Y he querido probarlo desde entonces. Si aún no sabes lo que es, te lo cuento. Si ya lo sabes, **sáltate el párrafo siguiente**.

WireGuard es a la vez **una aplicación y un protocolo de comunicación** que se utiliza para crear **redes privadas virtuales** o, como se les conoce habitualmente por sus siglas en inglés, VPN. Un concepto al que se le ha prestado mucha atención los últimos meses, por la rápida expansión del teletrabajo. Simplificando, una VPN permite **crear un túnel cifrado** para que un cliente que se encuentre en Internet pueda acceder a una red privada local **como si físicamente estuviera conectado a la misma**. Así, puedes conectarte a otros equipos de esa red local y acceder a Internet usando la IP pública que tenga esa red local. Por poner un ejemplo, puedes dejar un disco duro con información conectado en red en la empresa y acceder al mismo desde tu casa de una forma segura. También puedes dejar configurado un servidor VPN en tu casa y conectarte al mismo con tu móvil o portátil desde cualquier red wifi pública a la que accedas. De esta manera el tráfico sin cifrar pasará por la red privada de tu casa y no por esa red pública.

Entonces me encontré con [este curso](https://serversideup.net/courses/gain-flexibility-and-increase-privacy-with-wireguard-vpn/) creado por [Jay Rogers](https://jaydrogers.com/) en la web [ServerSide UP](https://serversideup.net/) y estaba tan detalladamente explicado que tuve que pedirle que me dejara hacer algo similar en castellano para mi alumnado.

Si también queréis utilizarlo con el vuestro, **lo tenéis accesible** en [este enlace](https://davidlms.github.io/Practicas/SERRED/wireguard.html).

Puede serte especialmente útil para trabajar el resultado de aprendizaje 8 del módulo **Servicios en Red** de 2ºCFGM SMR, en concreto los criterios:

i) Se ha comprobado el acceso a una red determinada desde los sistemas conectados a otra red distinta.

j) Se ha implantado y verificado la configuración para acceder desde una red pública a un servicio localizado en una máquina de una red privada local.

También si impartes el módulo **Seguridad y Alta Disponibilidad** de 2ºCFGS ASIR, ya que puede servirte para impartir el resultado de aprendizaje 3, en concreto el criterio:

d) Se han configurado redes privadas virtuales mediante protocolos seguros a distintos niveles.

Siempre que pueda, y me apetezca, por aquí me tendréis **compartiendo recursos con vosotros**.

**Nos vemos por videoconferencia**.