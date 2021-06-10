---
title: "Private Relay: ¿La solución definitiva para el anonimato en internet?"
date: 2021-06-09T18:36:00+02:00
description: "Lo que se sabe, lo que intuyo y lo que opino del nuevo servicio de Apple"
images:
- featuredimage.png

twitter:
  card: "summary"
  site: "@handle"
  title: "Private Relay: ¿La solución definitiva para el anonimato en internet?"
  description: "Lo que se sabe, lo que intuyo y lo que opino del nuevo servicio de Apple"
  image: "https://davidlms.com/article/private-relay-la-soluci%C3%B3n-definitiva-para-el-anonimato-en-internet/featuredimage.png"

tags: ['private relay', 'apple', 'wwdc', 'anonimato', 'privacidad', 'vpn']
categories: ['Cosas más técnicas']
author: "David Romero"
noSummary: true

resizeImages: false
---

El pasado 7 de junio, en la WWDC (WorldWide Developer Conference) anual, Apple presentó las novedades en sus sistemas operativos. Una de ellas fue **Private Relay**.

Añadamos antes **un poco de contexto** (puedes saltártelo si tienes nociones básicas de redes). Cuando navegamos por internet, lo hacemos identificados con una dirección llamada IP. Esta IP es necesaria para que, cuando hagamos una solicitud a una página web, la respuesta pueda volver a nuestro dispositivo. Además, para conocer la IP de la página web que queremos visitar tenemos que preguntársela a otro servidor (esto es una petición DNS). Al final del proceso, tanto nuestra IP como la página web que vamos a visitar es conocida por:

- Nuestro proveedor de servicios de internet (ISP).
- El servidor DNS que procesa la petición.
- El servidor de la página web que visitamos.
- Cualquier otro intermediario en la red.

Además, la dirección IP puede usarse en ocasiones para conocer tu ubicación. Al menos, si usamos HTTPS el contenido de esa conexión sí que estará cifrado. Pero solo con esos dos datos, nuestro ISP puede bloquearnos y registrar el acceso a determinadas páginas, el DNS también puede tener nuestro historial de navegación y el servidor del sitio web puede compartir la información de nuestras consultas con terceros, creando perfiles comerciales mucho más personalizados de lo que le gustaría a nuestra privacidad. Algunas soluciones disponibles a este problema:

-	**DNS sobre HTTPS**. Muchos navegadores modernos y routers permiten cifrar las consultas al servidor DNS. Esto permite que nuestro ISP no vea esa consulta (aunque sí la que hacemos posteriormente al sitio web), aunque el servidor DNS sí que podría registrarla. Los servidores DNS que ofrecen este servicio dan su palabrita de que no almacenan ninguna información que pueda perjudicar a la privacidad.
-	**Usar un Proxy**. Consiste en utilizar un servidor intermediario para navegar por internet. Cualquier consulta que hagamos pasará por el proxy. Esto únicamente oculta nuestra IP al servidor del sitio web, pero no a nuestro ISP y por supuesto tampoco al dueño del proxy.
-	**Usar una VPN**. Las redes privadas virtuales o VPN se diseñaron para permitir a trabajadores remotos usar los recursos locales de una empresa como si físicamente se encontrasen en ella. Crean un túnel cifrado a través de internet entre el dispositivo de una persona y el servidor VPN. Esto oculta el tráfico a nuestro ISP, pero no al dueño del servidor VPN.
-	**Usar TOR**. Con un navegador especial podemos cifrar nuestras comunicaciones con varias capas, a costa de una conexión más lenta. No obstante, es posible identificar con un análisis más o menos profundo quién está detrás de esas comunicaciones.

**Volvamos a Private Relay**. Hay que tener en cuenta que este servicio se centra en ocultar el conjunto de nuestra dirección IP y sitio web que visitamos, para que absolutamente nadie (ni ISP, ni servidor del sitio web, ni Apple, ni intermediarios) conozcan nuestro historial de navegación. No obstante, no protege las consultas DNS, por lo que habría que combinarlo con DoH (consultas DNS cifradas sobre HTTPS) o similar. En el caso de los dispositivos de Apple, en la WWDC de 2020 se emitió [una sesión hablando sobre ese tema](https://developer.apple.com/videos/play/wwdc2020/10047/).

Por ahora no he encontrado demasiada sobre el funcionamiento técnico de Private Relay. En este post voy a contaros lo que se sabe al respecto hasta el momento y cuál es mi interpretación. **Exponemos primero los hechos y después pasamos a las opiniones**.

La información técnica proporcionada por Apple podemos encontrarla en la sesión [Apple’s privacy pillars in focus](https://developer.apple.com/videos/play/wwdc2021/10085/) disponible públicamente. Voy a realizar una **traducción libre** de la misma usando imágenes del vídeo.

Los pilares del servicio Private Relay son:

-	Todas las conexiones están cifradas.
-	Tu dirección IP ya no te identifica.
-	La localización exacta de tu dirección IP está protegida.
-	Ninguna compañía (ni siquiera Apple) puede ver lo que haces.

![Características de Private Relay. Fuente: Apple](/privaterelay01.png)

El discurso proporcionado por el técnico de Apple es el siguiente:

![Esquema general de Private Relay. Fuente: Apple](/privaterelay02.png)

“Vamos a explorar brevemente cómo funciona Private Relay cuando voy a comprar cosas para mi nueva casa. Primero, cuando hacemos una conexión a una web de venta de mobiliario, se eligen aleatoriamente dos servidores Proxy diferentes en la red de Private Relay, por lo que un solo operador no tiene el control ni tampoco puede ver el escenario completo. El proxy que acepta mi conexión desde internet se llama Ingress Proxy (proxy de entrada). Este proxy oculta mi IP de otros servidores y cifra mi tráfico de internet para que mi proveedor de servicios no sepa qué estoy haciendo. La retransmisión de la petición hacia internet la realiza el Egress Proxy (proxy de salida), para evitar que el Ingress Proxy conozca el sitio al que estoy realizando la petición.

![Funciones de los proxies de entrada y salida en Private Relay. Fuente: Apple](/privaterelay03.png)

Private Relay gestiona el acceso a la red de forma que no requiere ningún tipo de identificación o información personal, usando firmas RSA ciegas. Una operación criptográfica de cegado realizada por mi dispositivo me permite acceder a la red sin dar ningún tipo de información sobre mi cuenta o sobre quién está realizando la conexión.

![Verificación de tokens de acceso en Private Relay. Fuente: Apple](/privaterelay04.png)

Usando la clave pública del servidor de tokens de acceso, un proxy Private Relay puede verificar rápidamente el permiso de acceso a la red. Antes de hacer una conexión, el Servidor de Tokens de Acceso de Private Relay proporciona un conjunto de tokens diferentes a mi dispositivo. Esto me da acceso a cualquier proxy que elija cuando lo necesite.

![Tokens de acceso cegados para no permitir el rastreo del origen en Private Relay. Fuente: Apple](/privaterelay05.png)

Para forzar la separación de información entre los proxies que elijo, la conexión se encapsula usando varias capas de cifrado. Los proxies van eliminando esas capas conforme la conexión pasa a través de ellos. Solamente mi dispositivo puede descifrar cada capa, lo cual es necesario para conocer que estoy accediendo a la web de mobiliario.

![Capas de cifrado en Private Relay. Fuente: Apple](/privaterelay06.png)

Cuando se realiza la conexión, el Egress Proxy elige una IP aleatoriamente. Esto ayuda a evitar que se relacione mi búqueda de un sofá con mi búsqueda del cortacésped, o con mi pedido reciente de una mesa. A lo largo del tiempo las conexiones Private Relay se crean automáticamente y se reutilizan para proporcionar protección contra el rastreo de IP y un buen rendimiento. La forma en la que Private Relay oculta mi IP tiene un beneficio más sobre la privacidad. Puesto que la dirección IP de mi casa puede geolocalizarse, el Ingress Proxy puede compartir esa localización conmigo. Esto me permite informar al Egress Proxy qué grupo de direcciones IP elegir. Esto es un gran ejemplo de buen servicio manteniendo la privacidad. Los sitios web pueden proporcionar contenido local en Safari mientras mi localización precisa permanece oculta.

Recuerda, el Ingress Proxy es el único que puede ver mi dirección IP y la convierte en otra dirección que pertenece a la misma área geográfica. Así, el sitio de venta de cortacésped puede saber desde qué área aproximadamente se realiza la conexión. En este ejemplo, el Ingress Proxy devuelve el área "Bay Area, California", la cual es reenviada al Egress Proxy para ayudarlo a elegir un grupo de direcciones IP asignadas a ese área general. Con una dirección IP regional, los sitios con los que establezco conexión pueden seguir mostrándome tiendas cercanas a mí.

Vamos a ver cómo funciona. Cuando me conecto, ambos sitios ven conexiones entrantes desde una dirección IP que se geolocaliza en mi área general. Pero hay varias posibles localizaciones de las direcciones IP de Private Relay que son compartidas por todos en la región.

![Información a la que accede el servidor del sitio web en Private Relay. Fuente: Apple](/privaterelay07.png)

Cuando la opción "Use Country and Time Zone" se selecciona en las opciones de iCloud Internet Privacy, no se le da ninguna pista al Egress Proxy.

Así que se elige una dirección IP del grupo que representa toda la región que pertenece al Ingress Proxy. Como resultado, los sitios web verán conexiones realizadas desde un área regional extensa. El mismo conjunto de direcciones IP se utiliza para todos en la región.

![Selección de la IP en función del área en Private Relay. Fuente: Apple](/privaterelay08.png)

Con la configuración de localización generalizada, el sitio web del cortacésped ahora ve una localización aleatoria, la cual para mí pueden ser lugares como Los Ángeles en lugar de Cupertino.”

**Hasta aquí los hechos** (información proporcionada por la propia Apple), **a partir de ahora todo es interpretación y opinión**.

Private Relay es un servicio incluido en iCloud+, por lo tanto, no es un servicio público. Así que es necesario **dar permiso al usuario** para acceder al mismo. El problema es que hay que darle permiso **sin identificar al usuario**, por seguir manteniendo su privacidad. Para solucionarlo, Apple utiliza **un servidor de tokens de acceso**. En función de la información proporcionada, voy a intentar explicar cómo se crean de forma simplificada:

1.	Tu dispositivo genera un token de sesión de tu cuenta iCloud en la que mantienes la sesión iniciada usando una función y un número aleatorio.
2.	Tu dispositivo le solicita al servidor de tokens de acceso de Private Relay su clave pública.
3.	Tu dispositivo usa la función, el número aleatorio y la clave pública que ha obtenido para crear un token de sesión “ciego”. Nadie puede comprobar que ese token está asociado a tu cuenta.
4.	Tu dispositivo le envía al servidor de tokens de acceso de Private Relay el token de sesión ciego y tu autenticación de iCloud.
5.	El servidor de tokens de acceso de Private Relay, una vez verificada tu autenticación de iCloud, firma el token de sesión ciego y se lo envía a tu dispositivo.

Este procedimiento se realiza varias veces, lo que proporciona a tu dispositivo **un conjunto de tokens de sesión ciegos**. Cuando quieres utilizar el servicio de Private Relay, ocurre lo siguiente:

1.	Tu dispositivo se comunica con el proxy correspondiente de Private Relay usando uno de los tokens de sesión ciegos obtenidos previamente.
2.	El proxy con el que se ha conectado tu dispositivo solicita al servidor de tokens de acceso de Private Relay su clave pública.
3.	Con la clave pública obtenida, verifica que el token de sesión ciego contiene una firma válida y permite a tu dispositivo el acceso al servicio.

Por lo tanto, el servicio **se puede utilizar sin identificarte como usuario**. Por hacer un símil, es como si comprásemos unas cuantas fichas de lavado de coche. La empresa que nos ha vendido esas fichas no puede saber cuándo las usaremos ni dónde. Ni siquiera cuántas hemos usado porque no sabe cuántas tenemos aún en nuestro poder. Sin embargo, podemos usar el servicio para lavar el coche cuando queramos. Este procedimiento no es nuevo, por ejemplo, Google One también utiliza uno similar para permitir el acceso a su VPN. Puedes leer **más información sobre cifrado ciego RSA** en [este artículo de Cathie Yun](https://cathieyun.medium.com/adventures-with-rsa-blind-signing-397035585121).

**Ahora es cuando comienza verdaderamente a funcionar el servicio de Private Relay**. Voy a limitarme a hacer **una propuesta simplificada de cómo podría implementarse** usándose un esquema simple de clave pública y privada. La premisa de partida es simple, cada actor en la comunicación genera un par de claves matemáticamente relacionadas de forma que lo que se cifre con una de las claves se descifraría únicamente con la otra. Pero no hay manera de que, teniendo una de las claves, pueda obtenerse la otra. En este caso intervienen cuatro agentes:

-	**Dispositivo del usuario**. Genera su clave privada (SU) y su clave pública (PU) relacionada. Únicas por cada conexión.
-	**Proxy de entrada (Ingress)**. Tiene una clave privada (SI) y su clave pública (PI) relacionada.
-	**Proxy de salida (Egress)**. Tiene una clave privada (SE) y su clave pública (PE) relacionada.
-	**Servidor del sitio web**. Tiene una clave privada (SS) y su clave pública (PS) relacionada.

Cuando realizamos una petición a un servidor web en Safari (una vez resuelto el DNS) pasaría lo siguiente:

1.	Nuestro dispositivo, usando uno de los tokens de sesión, solicita al servicio Private Relay dos servidores proxy aleatorios (uno de entrada y otro de salida) y sus respectivas claves públicas (PI y PE).
2.	Nuestro navegador cifra el contenido de la petición junto con su clave pública (PU) usando la clave pública del servidor web (PS). Básicamente esto es lo que realiza el cifrado HTTPS.
3.	Vuelve a cifrar lo anterior, enmascarando la IP de destino de la petición (la del servidor del sitio web) y añadiendo otro token de sesión y su clave pública (PU), con la clave pública del proxy de salida (PE).
4.	De nuevo vuelve a cifrar lo anterior, añadiendo otro token de sesión y la IP del proxy de salida elegido, con la clave pública del proxy de entrada (PI).

![Esquema del paquete de petición con todas las capas cifradas en el cliente](/propuestaprivaterelay01.png)

5.	Ahora envía el paquete con todas sus capas de cifrado a la dirección IP del proxy de entrada.
6.	El proxy de entrada descifra la primera capa con su clave secreta (SI) y verifica con la clave pública del servidor de tokens de acceso que el token es válido. A continuación, geolocaliza la IP del usuario y le asigna una zona extensa aproximada.

![Esquema del paquete de petición con la capa del proxy de entrada descifrada](/propuestaprivaterelay02.png)

7.	Envía el paquete con el resto de capas y la zona aproximada al proxy de salida cuya IP ha descifrado usando uno de sus puertos (y registrando que las comunicaciones de ese puerto pertenecen a la IP del usuario).
8.	El proxy de salida registra el puerto origen de la petición y lo mapea con otro de sus puertos, por el que reenviará la petición. Descifra una capa más con su clave privada (SE) y obtiene la IP destino (la del servidor del sitio web) y un token de acceso. Verifica el token de acceso y elige una IP aleatoria de la zona que le ha indicado el proxy de entrada. Le envía lo que queda del paquete, usando esa IP elegida como origen, al servidor del sitio web.

![Esquema del paquete de petición con la capa del proxy de salida descifrada](/propuestaprivaterelay03.png)

9.	El servidor del sitio web descifra el contenido de la petición usando su clave privada (SS), obteniendo la clave pública del usuario (PU). Esto es propio del cifrado HTTPS.

![Esquema del paquete de petición con todas las capas descifradas en el servidor web](/propuestaprivaterelay04.png)

10.	El servidor del sitio web procesa la petición y cifra la respuesta usando la clave pública del usuario (PU), enviándola de vuelta al proxy de salida. Este paso también pertenece al protocolo HTTPS.

![Esquema del paquete de respuesta con la primera capa cifrada en el servidor web](/propuestaprivaterelay05.png)

11.	El proxy de salida recibe la respuesta por un puerto que tiene registrado con otro (por el que le llegó la petición del proxy de entrada). Cifra la respuesta junto con la IP de origen (la del servidor del sitio web) usando de nuevo la clave pública del usuario (PU) y la envía por el puerto registrado.

![Esquema del paquete de respuesta con la segunda capa cifrada en el proxy de salida para ocultar la IP del servidor web](/propuestaprivaterelay06.png)

12.	El proxy de entrada recibe el paquete por un puerto que tiene registrado con una IP de origen (la del usuario), y a la que le reenvía el paquete.

![Esquema del paquete de respuesta con la segunda capa cifrada en el proxy de salida pasando por el proxy de entrada](/propuestaprivaterelay07.png)

13.	El navegador del usuario recibe el paquete. Descifra la primera capa con su clave privada (SU) y verifica el origen de la respuesta (IP del servidor del sitio web). 

![Esquema del paquete de respuesta con la segunda capa descifrada en el cliente](/propuestaprivaterelay08.png)

14. Descifra ahora la segunda capa con su clave privada de nuevo (SU), obteniendo la respuesta del servidor.

![Esquema del paquete de respuesta con todas las capas descifradas en el cliente](/propuestaprivaterelay09.png)

En esta comunicación:

-	El navegador del usuario obtiene la respuesta deseada del sitio web.
-	El proxy de entrada únicamente conoce la IP del usuario, pero no el destino de la petición.
-	El proxy de salida conoce el destino de la petición, pero no la IP del usuario, ya que la IP a la que tiene acceso es a la del proxy de entrada.
-	El servidor del sitio web responde a una petición generada por una IP aleatoria escogida por el proxy de salida. La próxima vez que el mismo usuario le realice una petición, lo hará desde otra IP de la misma zona, por lo que no podrá asociarlo a un perfil comercial.
-	El proveedor de servicios de internet (ISP) solamente sabe que el usuario ha establecido comunicación con un proxy de entrada de Private Relay, pero no qué sitio ha visitado.
-	Si además el usuario marca la opción “Use Country and Time Zone”, la IP que puede ver el servidor del sitio web ni siquiera se corresponderá a la zona aproximada en la que se encuentra realmente.

Es bastante posible que de alguna manera hayan simplificado los procesos para mantener la privacidad y a la vez tener un buen rendimiento en la navegación. Como aún se desconocen varios de estos detalles técnicos, vuelvo a avisar que **esto es solamente una propuesta sobre cómo podría funcionar aproximadamente Private Relay** con los datos que se han revelado hasta ahora.

Personalmente, creo que es una de las novedades **más interesantes de esta WWDC**. Hay que tener en cuenta que hay aproximadamente 1,5 billones de dispositivos activos de Apple en el mundo. Muchos de ellos contarán con esta configuración por defecto cuando accedan a internet. Y ese es uno de los problemas que tendrán los rastreadores, anunciantes y proveedores de servicio que deseen mantener el control sobre los sitios web visitados por nosotros. Es **la privacidad por defecto**, sin necesidad de ser usuarios avanzados, lo que marca la diferencia. Sin embargo, **no todos los países podrán acogerse a este servicio**. Comenzando por China, [Apple ha declarado que el servicio no estará activo de momento en un total de diez países](https://www.reuters.com/world/china/apples-new-private-relay-feature-will-not-be-available-china-2021-06-07/). ¿Por qué? Porque la legislación de esos países no permite desconocer la navegación web de sus ciudadanos. ¿Y por qué Apple, si lleva la privacidad por bandera, no pone resistencia? Porque una cosa es la ética y la privacidad, y otra muy distinta es el dinero. **Y cada cual tiene sus prioridades**.

Si te ha gustado el artículo, te aconsejo que te pases por [este podcast de DekkaR](https://www.spreaker.com/user/dekkar/icloud?autoplay=1). Y si te gustan estos temas, no dejes de seguirlo en [Twitter](https://twitter.com/DekkaR) y [Telegram](https://t.me/DekNet).

Si conoces algún otro sistema diferente a los nombrados que use un método similar, no dudes en dejar algún comentario. Y tampoco lo dudes si simplemente quieres dejar alguno.

Me voy a por mi token ciego.