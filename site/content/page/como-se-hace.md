---
title: "Cómo se hace"
date: 2020-06-02T20:10:14+01:00
excludeFromTopNav: false
showDate: false
---

¿Tienes interés en saber cómo se hace a nivel técnico este blog, qué inversión conlleva y cuáles son sus estadísticas de visitantes? En un ejercicio de transparencia inauguro esta sección, basada en la publicación [**Cómo se hace**](https://davidlms.com/article/c%C3%B3mo-se-hace-un-blog-a-coste-0/) y que irá actualizándose con las novedades que surjan.

Lo **primero** que hice fue registrar **el dominio** davidlms.com. Concretamente utilicé la plataforma [namecheap](https://www.namecheap.com), lo que supuso un coste de 12,94$ (con certificado SSL incluido) que tendré la opción de renovar el próximo 11 de mayo de 2021.

Tuve claro que quería una web **estática** fácil de mantener. Buscaba algo simple, que tuviese tiempos de carga mínimos y me permitiera escribir los artículos en **Markdown**. Fue cuando descubrí el framework [HUGO](https://gohugo.io/).

Sin duda lo que me dio el empujón definitivo al vacío fue encontrar [Netlify](https://www.netlify.com/). Esta plataforma te permite publicar un sitio web estático en Internet con **muy pocos clics**. Concretamente, crea un repositorio en tu cuenta de [Github](https://github.com/) con el código fuente del framework que elijas y, cada vez que realizas una modificación (un commit en el repositorio), lo vuelve a compilar para **actualizar la página**. Te proporciona además de forma gratuita un CDN, un dominio y un certificado SSL.

Podéis echar un vistazo al [repositorio de este blog](https://github.com/DavidLMS/davidlms.com),  la **configuración básica** se indica en el archivo site/config.toml y los **artículos** se ponen en formato Markdown dentro de carpetas individuales en la ruta site/content/article. He usado el tema [Bilberry Hugo](https://themes.gohugo.io/bilberry-hugo-theme/), que además está basado en [Lingonberry](https://www.andersnoren.se/teman/lingonberry-wordpress-theme/) de [Wordpress](https://wordpress.org/). Lo elegí por su **minimalismo**, por estar centrado en un **formato blog** y, básicamente, por cumplir con lo que necesitaba.

En este tema hay un par de cosas que merece la pena configurar. Una de ellas son **los comentarios**. Para mí era fundamental que el lector que quisiese pudiera comentar un artículo fácilmente, teniendo en cuenta que es una página estática. Se dan dos opciones, y [DISQUS](https://disqus.com/) es la gratuita. Solamente hay que crear una cuenta y poner el nombre registrado en el parámetro disqusShortname del config.toml. La otra cosa es la configuración de **las búsquedas**. Para eso se hace uso de una cuenta gratuita en [Algolia](https://www.algolia.com), que se configura siguiendo paso a paso las [instrucciones](https://themes.gohugo.io/bilberry-hugo-theme/#Algolia-Search).

También he querido llevar **un registro de los visitantes** del blog, más por curiosidad que por otra cosa. Se puede hacer gratuitamente con [Google Analytics](https://analytics.google.com/analytics/web/), pero Google ya sabe bastante de nosotros y no me daba la gana que obtuviese datos de mis visitantes por el hecho de entrar en mi web. Entonces encontré [Plausible](https://plausible.io), una alternativa más ligera y con un enfoque centrado en **mantener la privacidad de los visitantes**. Si se paga anualmente, sale a 4$ por mes.

Si quieres acceder a las estadísticas de visitantes de este blog, [aquí las tienes](https://plausible.io/davidlms.com).

En octubre de 2020 activé el servicio gratuito de Cloudflare en el dominio para mejorar la disponibilidad de la web y mitigar los posibles ataques DDoS. Puedes ver cómo lo hice detalladamente [aquí](https://davidlms.com/article/cloudflare-y-su-servicio-gratuito-parar-mejorar-la-disponibilidad-de-tu-web/).

Por último, quiero mostrarte en la siguiente tabla la inversión realizada en el blog hasta el momento:

| Concepto | Fecha | Inversión |
|:------:|:------:|:------:|:-------:|
|   Dominio (un año)   |   Mayo 2020   |   12,94$ |
|   Analítica con Plausible (un año)   |   Junio 2020   |   48$ |
|   TOTAL  | | 60,94$ |