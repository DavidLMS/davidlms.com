---
title: "Cómo se hace"
date: 2020-06-02T20:10:14+01:00
excludeFromTopNav: false
showDate: false
aliases:
    - /page/como-se-hace/
---

¿Tienes interés en saber cómo se hace a nivel técnico este blog, qué inversión conlleva y cuáles son sus estadísticas de visitantes? En un ejercicio de transparencia inauguro esta sección, basada en la publicación [**Cómo se hace**](https://davidlms.com/article/c%C3%B3mo-se-hace-un-blog-a-coste-0/) y que irá actualizándose con las novedades que surjan.

Lo **primero** que hice fue registrar **el dominio** davidlms.com. Concretamente utilicé la plataforma [namecheap](https://www.namecheap.com), lo que supuso un coste de 12,94$ (con certificado SSL incluido) que tendré la opción de renovar cada mes de mayo.

Tuve claro que quería una web **estática** fácil de mantener. Buscaba algo simple, que tuviese tiempos de carga mínimos y me permitiera escribir los artículos en **Markdown**. Fue cuando descubrí el framework [HUGO](https://gohugo.io/).

Sin duda lo que me dio el empujón definitivo al vacío fue encontrar [Netlify](https://www.netlify.com/). Esta plataforma te permite publicar un sitio web estático en Internet con **muy pocos clics**. Concretamente, crea un repositorio en tu cuenta de [Github](https://github.com/) con el código fuente del framework que elijas y, cada vez que realizas una modificación (un commit en el repositorio), lo vuelve a compilar para **actualizar la página**. Te proporciona además de forma gratuita un CDN, un dominio y un certificado SSL.

Podéis echar un vistazo al [repositorio de este blog](https://github.com/DavidLMS/davidlms.com),  la **configuración básica** se indica en el archivo site/config.toml y los **artículos** se ponen en formato Markdown dentro de carpetas individuales en la ruta site/content/article. He usado el tema [Bilberry Hugo](https://themes.gohugo.io/bilberry-hugo-theme/), que además está basado en [Lingonberry](https://www.andersnoren.se/teman/lingonberry-wordpress-theme/) de [Wordpress](https://wordpress.org/). Lo elegí por su **minimalismo**, por estar centrado en un **formato blog** y, básicamente, por cumplir con lo que necesitaba.

En este tema hay un par de cosas que merece la pena configurar. Una de ellas son **los comentarios**. Para mí era fundamental que el lector que quisiese pudiera comentar un artículo fácilmente, teniendo en cuenta que es una página estática. Se dan dos opciones, y [DISQUS](https://disqus.com/) es la gratuita. Solamente hay que crear una cuenta y poner el nombre registrado en el parámetro disqusShortname del config.toml. La otra cosa es la configuración de **las búsquedas**. Para eso se hace uso de una cuenta gratuita en [Algolia](https://www.algolia.com), que se configura siguiendo paso a paso las [instrucciones](https://themes.gohugo.io/bilberry-hugo-theme/#Algolia-Search).

También he querido llevar **un registro de los visitantes** del blog, más por curiosidad que por otra cosa. Se puede hacer gratuitamente con [Google Analytics](https://analytics.google.com/analytics/web/), pero Google ya sabe bastante de nosotros y no me daba la gana que obtuviese datos de mis visitantes por el hecho de entrar en mi web. Entonces encontré [Plausible](https://plausible.io), una alternativa más ligera y con un enfoque centrado en **mantener la privacidad de los visitantes**. Si se paga anualmente, sale a 4$ por mes.

Si quieres acceder a las estadísticas de visitantes de este blog, [aquí las tienes](https://plausible.io/davidlms.com).

En octubre de 2020 activé **el servicio gratuito de Cloudflare** en el dominio para mejorar la disponibilidad de la web y mitigar los posibles ataques DDoS. Puedes ver cómo lo hice detalladamente [aquí](https://davidlms.com/article/cloudflare-y-su-servicio-gratuito-parar-mejorar-la-disponibilidad-de-tu-web/).

En marzo de 2021 me encontré el blog fuera de servicio. En la página de error, Cloudflare indicaba que su DNS funcionaba correctamente y el problema estaba en el hosting. Sin embargo, en el panel de Netlify todo parecía correcto. Así que **desactivé Cloudflare**, quedándome con la red CDN original de Netlify. Al cabo de las horas el sitio volvió a estar en línea.

En junio de 2021 un lector del blog me comentó que DISQUS no cuidaba demasiado la privacidad, por decirlo de alguna forma, así que estuve buscando alternativas que sí se tomaran este asunto en serio. No encontré ninguna gratuita, pero [Hyvor Talk](https://talk.hyvor.com/) me ofrecía lo que buscaba a un precio más o menos asequible. Así que migré los comentarios existentes **de DISQUS a Hyvor Talk** y a funcionar.

En agosto de 2021 llegó el momento de **cambiar la apariencia del blog**. El primer tema lo elegí rápido, por simplicidad y por centrarme pronto en el contenido. Sin embargo, viendo que había podido mantener el proyecto más de un año sin abandonarlo, llegó el momento de tomar la elección un poco más en serio. Me decanté por [uBlogger](https://themes.gohugo.io/themes/ublogger/). Pienso que es lo suficientemente moderno, pero a la vez lo suficientemente conservador, como para que pueda mantenerlo así por mucho tiempo. Hay algunas novedades, como la posibilidad del modo oscuro, así como una útil flechita para volver siempre arriba o el menú flotante de forma continua. Aunque sigo manteniendo los mismos servicios de búsqueda, comentarios y analítica. Incluso se ha corregido el histórico error que no permitía acceder al RSS del blog y me ha permitido redirigir los antiguos enlaces a los nuevos, para que no se rompa ninguno. Creo que la presentación ha ganado enteros. Para los nostálgicos, [aquí tenéis cómo se veía el blog en julio de 2021](/old2020.html).

En agosto de 2024 quise probar a **ofrecer una versión en inglés del blog** de forma automática, utilizando modelos de lenguaje generativos. No me bastaban las traducciones automáticas disponibles de forma general, porque solían contener errores de contexto. Mi intención era que las traducciones mantuviesen mi estilo, pero se adaptaran al máximo a una audiencia lectora en inglés, haciendo aclaraciones con notas si fuera necesario para explicar entidades o conceptos que solo tengan aplicación en mi entorno. Así que, para cubrir esta necesidad, desarrollé [🌐💬 Aphra](https://github.com/DavidLMS/aphra), liberando el proyecto de forma que cualquiera pueda usarlo también. Para integrarlo de forma transparente, implementé una [Github Action](https://github.com/DavidLMS/davidlms.com/blob/master/.github/workflows/translate.yml) en el repositorio del blog. De esta forma, si se añadía un nuevo artículo o se modificaba uno existente, se hacía una traducción automática por parte de 🌐💬 Aphra. Por suerte, el tema que elegí en 2021 era compatible con un enfoque multilenguaje, así que tuve que hacer pocos cambios en la estructura de archivos del sitio.

Por último, quiero mostrarte en la siguiente tabla la inversión realizada en el blog (actualizada a fecha de julio de 2024, he omitido los gastos de traducción al inglés, que son unos 20-30 céntimos por artículo):

| Concepto | Fecha | Inversión |
|:------:|:------:|:------:|
|   Dominio (cinco años)   |   Mayo 2020-24   |   64,70$ |
|   Analítica con Plausible (cinco años)   |   Junio 2020-24   |   240$ |
|   Comentarios con Hyvor Talk (cuatro años)   |   Julio 2021-24   |   290,40$ |
|   TOTAL  | | 595,10$ |