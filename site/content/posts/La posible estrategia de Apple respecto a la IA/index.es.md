---
title: "La posible estrategia de Apple respecto a la IA"
subtitle: ""
description: "Los puntos sólo se unen hacia atrás"
date: 2023-08-26T09:32:00+02:00
lastmod: 2023-08-26T09:32:00+02:00
draft: false

author: "davidlms.es"

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
tags: ['opinión', 'inteligencia artificial']
categories: ['Cosas más técnicas']
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

Sin duda en los últimos años estamos viviendo **un tsunami de novedades en lo que se conoce como Inteligencia Artificial Generativa**, que no son más que modelos entrenados para generar textos, imágenes, vídeos, voces, músicas y otros tipos de contenido.

Son varios [los medios](https://www.bloomberg.com/news/newsletters/2023-04-18/is-apple-falling-behind-in-the-ai-race-against-microsoft-google-amazon) que han señalado a Apple como **la gran compañía tecnológica ausente** en esta carrera hacia nadie sabe dónde (la AGI, [según algunos](https://openai.com/blog/planning-for-agi-and-beyond)). Esta acusación se acusó (lo siento, no he podido evitarlo) especialmente tras la última [WWDC 2023](https://developer.apple.com/wwdc23/), en la que el gran protagonista fue el Apple Vision Pro y el "nuevo" concepto de computación espacial. Muchas voces indicaron que Apple había perdido la "visión" (qué ironía) al no subirse al tren de la IA y mantener el rumbo hacia la XR, cuando Meta "había demostrado que era una vía muerta". Este tema de la XR daría para otro artículo, así que por ahora no voy a explorar ese camino y me voy a centrar en la senda de la IA.

Los abogados defensores argumentaron que Apple no está mirando esa ola desde la orilla, **que lleva aplicando IA en sus dispositivos y aplicaciones** desde hace mucho tiempo. De hecho, tiene un portal de [Machine Learning](https://machinelearning.apple.com) donde comparte diferentes investigaciones en ese campo. Pero esto no convence al banquillo acusador, que no ve en Apple ningún "Copilot" a la vista. El problema es que el concepto de IA se ha convertido en **un saco demasiado grande**. Ahora mismo puede ser todo IA o no serlo nada. Parece que cada persona tiene una idea diferente de qué significa este concepto en la cabeza. Así que vamos a procurar indicar muy concretamente a qué nos referimos cuando hablamos de IA o no nos vamos a entender en la vida. En el resto de este artículo, IA será igual a "modelos de Machine Learning o Deep Learning entrenados para generar contenido, concretamente me voy a centrar casi exclusivamente en grandes modelos de lenguaje (LLMs) como [GPT-4](https://openai.com/gpt-4) o tecnologías derivadas como Copilot".

Sin ningún ánimo de posicionarme **en la defensa** (Apple si quieres pagarme por un artículo hablamos) **o en el ataque** (Microsoft/Meta/Google si queréis pagarme por un artículo hablamos) de esta empresa, me ha parecido que sería un ejercicio de análisis interesante elucubrar sobre el camino que podría seguir Apple para integrar esta tecnología en su ecosistema. Todo lo que encontréis en este artículo que no esté enlazado a una fuente de información, **es una opinión subjetiva**.

Antes de comenzar, pienso que es importante hacer **un repaso de las posiciones actuales de algunas de las empresas competidoras** en este aspecto:

- [OpenAI](https://openai.com) alias "**L'Enfant Terrible**", los protagonistas de la película. Primero con [DALL·E 2](https://openai.com/dall-e-2) y después con [ChatGPT](https://chat.openai.com) (GPT-3.5 en su salida). Querían ser muy abiertos, pero luego [no lo han sido tanto](https://www.lunasec.io/docs/blog/openai-not-so-open/). Al menos parecen mostrar preocupación por hacer las cosas bien y están destinando muchos recursos a entender cómo funcionan los LLMs y cómo alinearlos con “los valores humanos” (los suyos supongo). Se les perdona por regalos como [Whisper](https://openai.com/research/whisper).
- [Meta](https://ai.meta.com) alias "**Aquí estuvo Mark**", o la veleta empujada por el viento. Pivotaron toda la empresa hacia la Realidad Virtual y después con otro giro brusco empezaron a hacer mucho énfasis en la Inteligencia Artificial. Quizás le vuelvan a cambiar el nombre. AGI-le os pega, pensadlo. No entiendo muy bien la estrategia empresarial al respecto, pero el caso es que están regalando modelos abiertos muy buenos, como [SAM](https://segment-anything.com) o [Llama 2](https://ai.meta.com/llama/). Cada vez estoy más convencido de que el principal interés de Mark Zuckemberg es pasar a la historia por algo más que una red social que manipula a la gente. Y está dispuesto a seguir todos los caminos posibles para conseguirlo.
- [Microsoft](https://www.microsoft.com/es-mx/ai) alias "**El Mecenas**", tiene mucho que ganar y poco que perder. La estrategia de Satya Nadella ha sido y sigue siendo la nube (Azure) y meterse en todas las empresas con la suite de Office. La Inteligencia Artificial no es más que un nuevo Caballo de Troya para dar un empujón y seguir logrando sus objetivos. Invierte en la tecnología de OpenAI a cambio de dos grandes ventajas: tener la prioridad en utilizarla en sus productos y que se ejecute en su infraestructura. Librándose a su vez de dos desventajas que enfrentan las compañías basadas en tecnologías de Inteligencia Artificial Generativa: Que alguna competencia se les adelante o que surjan problemas de prestigio por polémicas relacionadas con las respuestas de estos modelos y/o las decisiones que se toman como consecuencia. Además juega a varias bandas, [presentando el modelo de lenguaje insignia de Meta en un evento propio](https://blogs.microsoft.com/es/blog/2023/07/18/microsoft-and-meta-expand-their-ai-partnership-with-llama-2-on-azure-and-windows/). Que, por supuesto, puede ejecutarse fácilmente en Azure. Gane quien gane esta guerra, Microsoft tiene todas las cartas para no quedarse fuera del equipo ganador.
- [Google](https://ai.google) alias "**Quiero y no puedo**", o pudo ser pero no de momento. No hace tanto que Google abarcaba todos los titulares que tenían que ver con la investigación de IA Generativa. Aún sin dejar probar ninguno de sus modelos, los resultados que mostraban nos dejaban con la boca abierta. Pero la competencia se adelantó. Mientras OpenAI se centra en el desarrollo de los modelos de IA y Microsoft en la infraestructura y la incorporación de esos modelos en sus productos, Google tiene que encargarse de todo. Preocupándose al mismo tiempo de no canibalizar o destruir sus principales líneas de financiación. Chico reto. Por eso es fácil de explicar la unión de fuerzas entre [DeepMind](https://www.deepmind.com) y [Google Brain](https://research.google/teams/brain/). Que la fuerza os acompañe.
- [Nvidia](https://www.nvidia.com/es-es/ai-data-science/) alias "**De Cryptobro a IAbro**", o [los dueños del trigo en el mundo de los panaderos](https://www.xataka.com/robotica-e-ia/hay-ganador-absoluto-industria-ia-se-llama-nvidia-esta-ganando-dinero-que-nunca). La mayor parte de la infraestructura que entrena o ejecuta modelos de Inteligencia Artificial lo hace sobre tarjetas que fabrica Nvidia. Eso la coloca en una posición privilegiada que se suma a las que ya tiene sobre el gaming o la minería de criptomonedas (últimamente venida a menos). Por lo tanto, tiene todas las papeletas para ser un claro ganador en los próximos años. Eso sí, ya son varias las empresas que han comenzado a crear sus propios diseños, así que no puede dormirse en los laureles... No vaya a ser que se convierta en la nueva Intel.

Hay otras empresas más pequeñas que creo que merece la pena mencionar:

- [StabilityAI](https://stability.ai) alias “**El Linux de la IAG**”, el verdadero relevo Open Source de OpenAI. Están teniendo algunos problemillas que espero que solucionen, porque la contribución de sus modelos son clave para permitir que cualquier persona pueda utilizar este tipo de tecnología tan potente sin limitaciones.
- [Anthropic](https://www.anthropic.com) alias "**El rival de ChatGPT**", siempre es bueno que haya competencia. Sus modelos basados en Claude tienen algunos aspectos que mejoran lo que ofrece actualmente OpenAI, aunque funcionan peor en otros. Claro candidato para acabar siendo adquirido por alguna de las grandes.
- [Hugging Face](https://huggingface.co) alias "**El Motor Open Source**", el sueño hecho realidad de aquellas personas a las que les gusta trastear y hacer pruebas con todas las novedades. Este portal web proporciona todo lo necesario: datasets, modelos e interfaces fáciles de crear y utilizar para ejecutarlos. No hay modelo abierto que quieras probar que no esté disponible en un clic en Hugging Face, muchas veces incluso el mismo día de su salida. ¿Se nota mucho que me encanta esta organización?
- [Humane](https://hu.ma.ne) alias "**El Magic Leap de la IA**", están cerca de sacar un dispositivo personal que supuestamente aprovecha verdaderamente el potencial de la IA, siendo el primero de lo que llaman computación contextual. Lo siento, pero a mí me recuerda demasiado al bombo que se le dio a Magic Leap cuando la moda era la XR, que prometían tener algo entre manos que "traería la magia a la realidad". Y después de mucho tiempo de espera sacaron algo similar a lo que había en el mercado en ese momento. Ojalá me equivoque y Humane saque un dispositivo verdaderamente disruptivo que mejore la vida de las personas y su relación con la tecnología.
- [xAI](https://x.ai) alias "**Elon Musk**", poco más que decir, el enésimo proyecto de Elon Musk para salvar al mundo después de pedir una pausa en el desarrollo de la IA. Lo nombro simplemente por hacerle un poco la pelota, ahora que me acaba de quitar el bloqueo que tenía puesto a mi dominio en Twitter (ahora X). Desde luego, teniendo todos los datos de la red social, tiene el potencial para crear el modelo de lenguaje más tóxico de todos.

Ahora sí creo que estamos en el punto idóneo para ponernos los zapatos de Apple desde el momento en el que OpenAI soltó la bomba a la que todavía **no hemos terminado de reaccionar**.

ChatGPT apareció en nuestras vidas el 30 de noviembre de 2022. Y, excepto a Microsoft, que obviamente contaba con información privilegiada, cogió al resto de grandes empresas tecnológicas a pie cambiado. También a Apple. Y con esto no quiero decir que no tuviese ningún tipo de investigación al respecto ni nada de eso. Simplemente que fue un evento inesperado. **Un evento que fue la semilla** para que luego el público general esperase algún tipo de movimiento por su parte en la WWDC 2023. De hecho, es más que probable que discutieran sobre ello en [el evento interno que realizaron sobre IA](https://appleinsider.com/articles/23/02/07/apple-to-hold-first-in-person-ai-summit-in-years). Pero claro... Apple no es Google.

Ya sabes lo que pasó después. La respuesta fue visionOS. Pese a algunas [diferencias de opinión dentro de la empresa](https://www.cnbc.com/2023/05/18/report-apple-execs-skeptical-on-headset-calling-it-science-project.html), se presentó el nuevo dispositivo Apple Vision Pro. De momento, no sabemos si la intención inicial era enseñarlo en este evento o simplemente decidieron adelantarlo porque necesitaban presentar algo que llamara verdaderamente la atención. Es probable que la narrativa fuese: "No presentamos nada que compita con GPT-4 y las tecnologías derivadas, pero lo compensamos con algo que lleváis esperando mucho tiempo". O quizás, simplemente, la inversión inicial en el producto requería mostrarlo ya para que los desarrolladores pudiesen comenzar a crear aplicaciones y así poder rentabilizarlo a futuro.

Sin embargo, si se presta la suficiente atención, Apple nos dejó en ese evento **algunas pistas** para confirmarnos que están trabajando en ello. Mira esta captura de la conferencia principal:

![Un modelo de lenguaje Transformer](/modelo-transformer.png)

Espera... ¿Un modelo de lenguaje Transformer? Anda... Como GPT (cuyas siglas son Generative Pre-trained Transformer). En ese momento estaban hablando de las mejoras en funciones de autocorrección y autocompletado. Podrían haber dicho simplemente que las han mejorado (de hecho, es el tipo de cosa que probablemente en cualquier otra conferencia no le hubiesen dedicado ni cinco segundos), pero **indican explícitamente** que es un modelo Transformer. No puede ser una casualidad. Se trata de un modelo simple GPT de Apple. Que sí, que obviamente dista mucho de GPT-4. Pero ojo, que se ejecuta en el dispositivo y cada vez que se pulsa una letra del teclado. No suficiente con eso, volvieron a pronunciar la palabra clave a continuación:

![Reconocimiento de voz basado en Transformer](/basado-transformer.png)

Otra vez Transformer... Ahora en el dictado (¿Alguien ha "susurrado" algo?). Es evidente que esta es la forma que ha elegido Apple para **mandarnos un mensaje claro** en la conferencia: Esta tecnología no nos es desconocida y llevamos tiempo trabajando en ella.

Pero ese mensaje no llegó. O al menos eso creo por las reacciones a la WWDC. De no ser así, no hubiese hecho falta hace unos días [filtrar que estaban trabajando en ello de forma explícita](https://www.xataka.com/robotica-e-ia/apple-gpt-empresa-cupertino-trabaja-ia-para-competir-openai-google-gurman). Pues claro, era evidente que no están ciegos ni sordos. Sobre todo después de [prohibir a sus empleados el uso de ChatGPT](https://www.genbeta.com/actualidad/apple-prohibe-uso-chatgpt-otras-inteligencias-artificiales-a-sus-trabajadores-documento-interno). Como empresa, tienes que proporcionar una alternativa porque de otra forma arriesgas mucho si dejas a tus empleados sin ese plus de productividad. Dejando eso a un lado, la reflexión que me ha llevado a escribir este artículo proviene precisamente a raíz de esa filtración. Porque en la misma se indica que Apple aún no tiene claro cómo hacer llegar esa tecnología a los consumidores y, como está expresado, parece que se debe a una falta de ideas.

A ver... ¿Falta de ideas? Aquí hay unas cuantas:

- Una Siri que por fin sepa qué queremos que haga.
- Un copiloto de código en Xcode.
- Informes textuales que interpreten de forma personalizada las medidas de la app Salud.
- Crear Atajos solamente describiendo el comportamiento que deseamos que tenga, sin tener que aprender a usar la app.
- Resúmenes de reuniones y notas.
- Búsqueda de respuestas en nuestros archivos.

Si a mí se me pueden ocurrir unos cuantos usos útiles pensando al vuelo en menos de un minuto, no me quiero imaginar **la cantidad de ideas que pueden tener anotadas** en Cupertino.

Los obstáculos tienen que ser otros. Mi opinión es que Apple enfrenta **dos problemas importantes** para desplegar un modelo tan potente como GPT-4 en su ecosistema:

- **Computación en la nube**. Al no poseer infraestructura de granjas de servidores propias (que puedan ofrecer servicios a los consumidores), Apple depende de otros distribuidores, encareciendo mucho su utilización, perdiendo libertad de acción, reacción y, por supuesto, privacidad.
- **No determinismo**. Las respuestas y generaciones de estos modelos son probabilísticas. La misma entrada en dos momentos diferentes no produce la misma salida y, por lo tanto, es muy complicado acotar las respuestas que pueden dar.  Esto choca frontalmente con la necesidad de control que tiene Apple sobre cómo actúan y reaccionan sus dispositivos. Algo fundamental para mantener viva su filosofía. ¿Os imagináis un dispositivo de Apple diciendo alguna barbaridad o realizando una acción no prevista inicialmente por la empresa? Pues esto es un problema difícil de resolver en los grandes modelos de lenguaje, [vulnerables a técnicas de Prompt Injection](http://www.elladodelmal.com/2023/08/como-lograr-que-llama-2-bard-ai-chatgpt.html) y llegando a cumplir objetivos intermedios que no habían previsto sus creadores.

La clave para solventar el primer problema tiene nombre y apellido: [**Neural Engine**](https://observatorio-ia.com/apple-neural-engine-procesador-ia-moviles-apple). De forma muy resumida, es un chip que permite ejecutar modelos de Inteligencia Artificial (Machine Learning) eficientemente en el dispositivo que lo integra. Apple comenzó a ponerlos en los iPhone en 2017 y actualmente se encuentran en toda su gama de dispositivos que tienen (o se les puede conectar) una pantalla. Tras su salida, lo han ido mejorando año tras año. Pese a no ser comparable a la potencia de ejecución que se puede lograr en un CPD (Centro de Procesamiento de Datos), cuenta con tres ventajas:

- **Los datos no salen del dispositivo**. La privacidad siempre ha sido una prioridad en Apple. Si el modelo lo ejecuta el propio dispositivo, no es necesario enviar ningún dato a través de Internet como sí debe hacerse forzosamente en el caso de modelos ejecutados en la nube. Siempre he pensado que a Apple le ha venido muy bien no tener negocios que dependan de la recolección de datos, hasta el punto de no saber si la privacidad fue un valor buscado o simplemente una consecuencia bienvenida. No es que sea todo cuestión de azar, porque ha realizado muchos avances independientes en privacidad, pero qué bien encaja esta ventaja a raíz de un gran inconveniente como es no tener centros de datos propios. Cuando se integre la IA con los sistemas operativos,  esta ventaja será aún mayor. Mientras que Windows y los sistemas basados en Linux como Android tendrán complicado controlar la ejecución en local de los modelos (por las diferentes configuraciones de hardware en las que se ejecutan), Apple podrá saber exactamente a qué velocidad puede ejecutarse cada modelo en cada uno de sus dispositivos. Por eso probablemente la estrategia de Microsoft pase, al menos a medio plazo, únicamente a través de la nube. Que además le viene muy bien para aumentar los ingresos de Azure.
- **Se reduce la huella ecológica**.  Una de las críticas más escuchadas acerca de los modelos de Inteligencia Artificial es que su procesamiento requiere una potencia muy superior a otras operaciones más simples, con el aumento de consumo correspondiente. Simplificando mucho, la presencia de una nueva ola de modelos potentes ejecutándose en los servidores supone un mayor gasto energético, como ya ha pasado con el auge de las criptomonedas. Si esos modelos se ejecutan de forma local en un dispositivo deben tener un consumo más moderado y eficiente, porque nadie quiere que la batería solamente dure una hora. Por lo tanto, garantiza que se trabaje en esa línea. Además, los nuevos ordenadores de Apple tienen un consumo muy inferior a la mayoría de su competencia, gracias a su arquitectura basada en ARM.
- **Ejecución offline**. Evidentemente si se ejecutan los modelos en el propio dispositivo no se necesitará conexión Internet, con las ventajas que eso conlleva cuando no tenemos cobertura o una conexión de datos. Pero no solamente eso, al no depender de un servicio en la nube, tampoco es posible que el servicio se encuentre caído o inaccesible en algún momento, como ya ha pasado en algunas ocasiones con ChatGPT por ejemplo.

El segundo problema es el que veo más complejo de resolver en el punto en el que estamos. Apple necesita que su modelo de lenguaje **esté alineado con "los valores" de la empresa**. Esto es mucho más fácil de decir que de conseguir, [OpenAI ya dedica el 20% de su computación](https://openai.com/blog/introducing-superalignment) a resolver ese problema. No creo que veamos una aplicación tipo ChatGPT de Apple. Primero, porque no le veo ningún uso con sentido dentro de su ecosistema. Pero, en el caso de que lo encuentren, no estará disponible hasta que la cuestión del alineamiento esté resuelta. Eso no significa que no haya una solución intermedia mucho más interesante: **usar el modelo para "comprender" qué desea hacer el usuario**. Esto ya lo podemos ver en ChatGPT a través de sus plugins. Parece magia (pero no lo es): activas los plugins, pides algo y el modelo sabe qué y cómo debe interactuar con otros sistemas para obtener la respuesta que necesitas. Esto permitiría, por ejemplo, hacer una petición a Siri sobre algún accesorio de Homekit sin necesidad de dar la orden exacta para que funcione. Como la salida no es un texto, sino una acción, eliminamos el problema de que la respuesta no esté alineada con sus valores. También permitirá crear un nuevo tipo de experiencia de usuario en las aplicaciones, porque **no será necesario aprender a usarlas**: bastará con indicarles el resultado que queremos para que el modelo ejecute las acciones necesarias para ello. En esta línea, ya tenemos librerías funcionando, como la recién liberada [TypeChat](https://microsoft.github.io/TypeChat/) por parte de Microsoft. Las posibilidades son infinitas. Nos acercamos a un punto en el que el límite está más en nuestra imaginación que en la tecnología.

Teniendo en cuenta los problemas que he expuesto, **¿qué es lo que yo haría si tuviese que marcar la estrategia de Apple respecto a la IA?**

- **Seguir invirtiendo en el diseño del Neural Engine**. Cada euro bien gastado estará. La piedra angular sobre la que debe construirse la estrategia. Porque gracias a la integración hardware y software que ninguna otra empresa tiene, puede aportar un valor añadido que a la competencia le supondría años igualar. Tal y como está pasando con la arquitectura Apple Silicon.
- **Pruebas, lluvias de ideas que lleven a más pruebas y contratar talento**. Surfear la ola de la IA no significa solamente sacar productos que la utilicen, también se trata de estar atentos. Leer acerca de las novedades e ir probando las diferentes soluciones que aparezcan. Poner equipos a pensar, idear y probar diferentes formas de aprovechar la tecnología e integrarla en el ecosistema. Estoy seguro de que esto ya lo están haciendo, al igual que fueron probando en un Mac los diferentes procesadores A hasta que su funcionamiento fue lo suficientemente decente para convertirse en el M1. Pero todo esto debe ir de la mano de contratar talento y contar con los/as mejores. Ahí lo dejo.
- **Esperar a que el Open Source me proporcione soluciones**. El nuevo modelo Llama 2 es completamente abierto. Pero tiene dos limitaciones: su dataset no puede utilizarse para entrenar otro modelo y no puede usarse de forma comercial si se tienen más de 700 millones de usuarios activos. Entrenar un modelo como Llama 2 cuesta 20 millones. No muchas empresas pueden permitirse ese presupuesto si no conlleva algún tipo de reinversión directa. Tampoco hay muchas que tengan más de 700 millones de usuarios activos. Pero el iPhone tiene unos 1000 millones. Unos números muy similares… ¿Casualidad? ¿O que Meta no ha querido darle ninguna ventaja que sabe que le ha estado dando liberando otros modelos como Segment Anything (SAM)?
- **Repensar toda la experiencia de usuario de mis sistemas operativos y aplicaciones (UX)**. ¿Sabías que macOS puede controlarse por completo únicamente usando la voz? No es nada cómodo, pero funciona y estas nuevas tecnologías pueden ser la puntilla para que se destierre el teclado y ratón a usos profesionales muy concretos. En Apple tienen experiencia en crear interacciones que enganchan: lo hicieron con la rueda del iPod, con la pantalla táctil del primer iPhone y apuesto a que lo harán con la vista y los gestos de visionOS. Pero en algún momento, alguien redefinirá todo lo que sabemos de UX usando Inteligencia Artificial. ¿Serán interfaces que se ajusten automáticamente a los conocimientos y destrezas de cada usuario? ¿Desaparecerán los menús y los botones y solamente habrá una entrada de texto (que tenga la posibilidad de escribirse usando la voz)? ¿Quizás solamente necesitemos un intérprete de nuestras ondas cerebrales para hacer peticiones a los dispositivos? ¿Será una mezcla de todo y tendremos varias opciones a nuestro alcance para elegir? Nadie lo sabe aún, pero de lo que estoy seguro es que alguna persona o entidad pasará a la historia por dar la solución adecuada de la nueva experiencia de usuario aplicando estas tecnologías.

Por todo lo comentado previamente, no creo que Apple muestre nada totalmente revolucionario de IA a corto plazo. Llegarán funcionalidades de forma muy paulatina, probablemente por detrás de la competencia, pero con otro enfoque. Hasta que, un día, de repente, todo haya cambiado. Porque hasta ahora Apple ha tenido un estilo de vida tipo Gandalf: **no llega tarde ni temprano, sino exactamente cuando se lo propone**. Y no tenemos ninguna pista de que eso vaya a cambiar pronto.

Esta es mi opinión acerca de los problemas y posibles soluciones que puede tener Apple encima de la mesa de cara a su estrategia respecto a la Inteligencia Artificial Generativa, concretamente, sobre los grandes modelos de lenguaje y sus aplicaciones. Pero obviamente no se podrá hacer ninguna predicción exacta y sin errores hasta que que las cosas sucedan. Parafraseando a Steve Jobs: "Los puntos solo se conectan hacia atrás". De cualquier forma, nos esperan al menos **unos cuantos años interesantes, transformadores y hasta cierto punto aterradores en el sector tecnológico**.

**Gracias por leer** y llegar hasta aquí.

PD: Ninguna IA ha sido maltratada para la redacción de este artículo... Pero sí para generar la imagen que lo ilustra.