---
title: "Servicios en Red: Una programación didáctica en espiral (y III)"
date: 2020-09-06T18:05:00+02:00
description: "Propuesta desglosada por sesiones de una unidad didáctica"
images:
- featuredimage.jpg

twitter:
  card: "summary"
  site: "@handle"
  title: "Servicios en Red: Una programación didáctica en espiral (y III)"
  description: "Propuesta desglosada por sesiones de una unidad didáctica"
  image: "https://davidlms.com/article/servicios-en-red-una-programaci%C3%B3n-did%C3%A1ctica-en-espiral-y-iii/featuredimage.jpg"

tags: ['programacion didactica', 'modelo espiral', 'unidad didáctica', 'sesiones', 'temporalización', 'servicios en red']
categories: ['Propuestas didácticas']
author: "David Romero"
noSummary: true

resizeImages: false
---
Una vez definido el [objetivo de esta programación](https://davidlms.com/article/girando-alrededor-del-aprendizaje-una-programaci%C3%B3n-did%C3%A1ctica-en-espiral/), [clasificar los criterios de evaluación](https://davidlms.com/article/servicios-en-red-una-programaci%C3%B3n-did%C3%A1ctica-en-espiral/) y [establecer una planificación general semanal](https://davidlms.com/article/servicios-en-red-una-programaci%C3%B3n-did%C3%A1ctica-en-espiral-ii/), terminaremos esta serie **desglosando las distintas sesiones de una de las unidades**. Concretamente, la **unidad 1: “Crea tu propio servidor de hosting”**, correspondiente a las semanas 3-8 de la planificación general, es decir, un total de 42 sesiones.

Tenéis la **propuesta completa** en la siguiente tabla:

| Sesión | Contenido |
|:------:|:------:|
|   1   |   - Reflexión: ¿Se puede controlar un ordenador a distancia?     |
|      | - Explicación: Acceso remoto en modo texto y SSH |
|       | - Práctica: Acceso a un servidor usando SSH  |
|   2   |   - Reflexión: ¿Cómo intercambiamos archivos con un servidor?
| | - Explicación: Transferencia de ficheros con FTP |
| | - Práctica: Descarga y subida de ficheros en un servidor usando vsftpd usando SSH para la instalación   |
|   3   |   - Reflexión: ¿Qué necesito para poner en línea una página web?<br/><br/>- Explicación: Servidores web<br/><br/>- Práctica: Permite el acceso a tus compañeros a una página web propia, usando SSH para la instalación del servidor web nginx y subiendo los archivos al servidor con vsftpd   |
|   4   |   - Reflexión: ¿Hay alternativas a SSH?<br/><br/>- Explicación: Telnet<br/><br/>- Práctica: Prueba a realizar una conexión Telnet y otra SSH capturando paquetes con Wireshark. ¿Cuál es la diferencia?   |
|   5  |   - Finalización de prácticas pendientes<br/><br/>- Práctica de ampliación: Pon una página web online con https://es.000webhost.com/   |
|   6   |   - Evaluación de los criterios: 3b, 6b, 5b y 5f   |
|   7   |   - Revisión de la evaluación   |
|   8   |   - Reflexión: ¿Se puede ver el escritorio de un ordenador controlado a distancia?<br/><br/>- Explicación: Acceso remoto en modo gráfico<br/><br/>- Práctica: Accede al ordenador de un compañero usando Escritorio Remoto y TeamViewer. ¿Cuáles son las diferencias?   |
|   9   |   - Reflexión: ¿Cómo gestionamos un servidor FTP con varios usuarios?<br/><br/>- Explicación: Usuarios, grupos y acceso anónimo en un servidor FTP<br/><br/>- Práctica: Permite el acceso en tu servidor a toda la clase usando el acceso anónimo y a dos compañeros usando usuarios enjaulados   |
|   10   |   - Reflexión: ¿Podemos asegurar la comunicación entre un cliente y una página web?<br/><br/>- Explicación: Los protocolos HTTP y HTTPS<br/><br/>- Práctica: Asegura tu página web con un certificado HTTPS. Compara el tráfico HTTP y HTTPS en Wireshark   |
|   11   |   - Reflexión: ¿FTP es un protocolo seguro?<br/><br/>- Explicación: FTPS y SFTP como alternativas<br/><br/>- Práctica: Usa un protocolo seguro para la transferencia de archivos   |
|   12   |   - Finalización de prácticas pendientes<br/><br/>- Práctica de ampliación: ¿Puedes encontrar y usar una app en tu teléfono para controlar remotamente un ordenador?   |
|   13   |   - Evaluación de los criterios: 3c, 3d, 5i, 6c, 6d y 6f<br/><br/>- Recuperación de los criterios: 3b, 6b, 5b y 5f   |
|   14   |   - Revisión de la evaluación   |
|   15   |   - Reflexión: ¿Puedo administrar un servidor sin interfaz gráfica a través de una interfaz gráfica?<br/><br/>- Explicación: Acceso remoto a través de la web<br/><br/>- Práctica: Instalación y prueba de webmin   |
|   16   |   - Reflexión: ¿Puedo poner límites a los usuarios de un servidor FTP?<br/><br/>- Explicación: Límites y cuotas<br/><br/>- Práctica: Configuración de límites y cuotas en vsftpd   |
|   17   |   - Reflexión: ¿Cómo controlo un servidor FTP por línea de comandos?<br/><br/>- Explicación: Comandos FTP<br/><br/>- Práctica: Accede a tu servidor FTP usando la línea de comandos, descarga y sube algún archivo y compruébalo   |
|   18   |   - Reflexión: ¿Qué diferencia al modo de acceso activo y pasivo en un servidor FTP?<br/><br/>- Explicación: Funcionamiento del acceso activo y pasivo en un servidor FTP<br/><br/>- Práctica: Accede a tu servidor FTP usando el modo activo y pasivo capturando la conexión con Wireshark. Compáralas   |
|   19   |   - Finalización de prácticas pendientes<br/><br/>- Práctica de ampliación: Instala Monsta FTP para usar una web como cliente de tu servidor FTP   |
|   20   |   - Evaluación de los criterios: 3e, 3f, 3g y 6g<br/><br/>- Recuperación de los criterios: 3b, 3c, 3d   |
|   21   |   - Revisión de la evaluación   |
|   22   |   - Reflexión: ¿Puedo tener distintas páginas web en un mismo servidor?<br/><br/>- Explicación: Sitios virtuales<br/><br/>- Práctica: Configuración de sitios virtuales en nginx   |
|   23   |   - Reflexión: Las acciones en una página web, ¿Se ejecutan en el cliente o en el servidor?<br/><br/>- Explicación: Código cliente y código servidor. Lenguajes<br/><br/>- Práctica: Ejecuta código cliente y código servidor en nginx   |
|   24   |   - Reflexión: ¿Se puede extender la funcionalidad de un servidor web con módulos?<br/><br/>- Explicación: Utilidad e instalación de módulos<br/><br/>- Práctica: Instalación de nginx con módulos asociados   |
|   25   |   - Reflexión: ¿Puedo bloquear el acceso en mi página web a una determinada IP?<br/><br/>- Explicación: Seguridad en un servidor web<br/><br/>- Práctica: Asegura tu servidor nginx   |
|   26   |   - Finalización de prácticas pendientes<br/><br/>- Práctica de ampliación: Sirve tu página web usando IIS en Windows Server   |
|   27   |   - Evaluación de los criterios: 5c, 5d, 5e, 5g, 5h<br/><br/>- Recuperación de los criterios: 5b, 5f, 5i   |
|   28   |   - Revisión de la evaluación   |
|   29   |   - Reflexión: ¿Cómo explicarías a un familiar las distintas formas que tenemos de acceder y administrar un sistema remotamente?<br/><br/>- Explicación: Creamos definiciones de los distintos tipos de acceso y administración remoto entre todos<br/><br/>- Trabajo personal: Escribimos nuestras propias definiciones y escenarios de uso para cada tipo   |
|   30   |   - Reflexión: ¿Cuál es la utilidad de un servidor FTP? ¿En qué modos puede operar?<br/><br/>- Explicación: Se proponen escenarios empresariales y se discuten soluciones en grupo<br/><br/>- Trabajo personal: Búsqueda de ejemplos en Internet   |
|   31   |   - Reflexión: ¿Cómo funciona un servidor web? ¿Qué protocolos utiliza?<br/><br/>- Explicación: Procedimiento de comunicación entre cliente y servidor web y descripción del funcionamiento de los protocolos<br/><br/>- Trabajo personal: Creamos nuestros propios diagramas que expliquen las comunicaciones de un servidor web   |
|   32   |   - Reflexión: ¿Cuáles son las ventajas y desventajas de cada tipo de acceso remoto?<br/><br/>- Explicación: Se proponen escenarios empresariales y se discuten soluciones en grupo<br/><br/>- Trabajo personal: Creamos una tabla con las ventajas y desventajas de cada tipo de acceso remoto   |
|   33   |   - Autoevaluamos nuestro conocimiento teórico de los servicios<br/><br/>- Repaso   |
|   34   |   - Evaluación de los criterios: 3a, 5a, 6a y 6g   |
|   35   |   - Revisión de la evaluación   |
|   36   |   - Proyecto: Creamos nuestro propio Hosting   |
|   37   |   - Proyecto: Creamos nuestro propio Hosting   |
|   38   |   - Proyecto: Creamos nuestro propio Hosting   |
|   39   |   - Proyecto: Creamos nuestro propio Hosting   |
|   40   |   - Defensa de proyectos  |
|   41   |   - Repaso/Recuperación de los RA 2, 5 y 6   |
|   42   |   - Revisión de la evaluación   |

**He estructurado cada semana de la misma forma**: cuatro sesiones con nuevo contenido, una sesión extra para que terminen los más rezagados y puedan ampliar los más aventajados, una sesión de evaluación y otra de revisión de la misma (sería ideal que estas dos últimas sesiones fueran seguidas en el tiempo).

Cada sesión en la que se enseña nuevo contenido, empieza con una reflexión. Se lanza una pregunta que **pone en evidencia un problema**, en base a los conocimientos previos del alumnado. Durante esa hora se proporcionarán las herramientas **para resolver ese problema** la próxima vez que les surja. Después, se realizará una práctica para que ellos mismos puedan de alguna manera “tocar” la solución propuesta.

Para que el trabajo pendiente no se acumule al alumnado que necesite más tiempo, se dedicará una hora completa para terminarlo, despejar dudas y **asegurar que se encuentran preparados para una evaluación**. Los alumnos más aventajados pueden realizar una práctica más para mejorar su transferencia del aprendizaje.

Llegamos a la sesión de evaluación, donde **se pondrá a prueba lo que han aprendido**. Es muy importante que el docente esté atento a las **distintas dificultades** con las que se encuentren los estudiantes.

Y por último, y más importante, finaliza la semana con la sesión de revisión. Es probablemente la sesión clave, ya que nos permite **aplicar una evaluación formativa de calidad**. El alumnado debe ser consciente de que no será la última vez que tengan que poner a prueba esos conocimientos, para que presten la atención suficiente. En esta hora el docente explicará y **aclarará las dificultades** que haya detectado en la sesión anterior.

La dos últimas semanas de la unidad son un poco diferentes al resto. En la penúltima semana se trabajan **los conceptos más puramente teóricos**. En muchas ocasiones, se comienza con la explicación teórica antes de pasar a la práctica. Pienso que si solo impartimos la teoría básica al comienzo, el alumnado estará mucho mejor preparado para entender conceptos complejos después de realizar varias pruebas prácticas, ya que podrá **crear conexiones con conocimientos previos más fácilmente**. La última semana se destina a un proyecto que **integre todos los contenidos vistos en la unidad** (y potencialmente en unidades anteriores). Es importante que sea lo más aplicado posible, intentando que tenga una **utilidad real**. Así, el alumnado comprobará que lo que ha aprendido le servirá en su futuro profesional y **se sentirá más motivado** a seguir aprendiendo.

Con esta planificación, conseguimos que **cada resultado de aprendizaje se trabaje durante bastante tiempo**, mucho más que si lo vemos solamente en una unidad aislada. Sería bueno aprovechar cualquier circunstancia de unidades posteriores **para volver también a utilizarlos**, consiguiendo así **un repaso espaciado**. El único objetivo de los que propusimos que se queda un poco cojo es el que está relacionado con la transferencia del aprendizaje. Sería ideal que pusiesen en práctica los contenidos **en situaciones más variadas y en distintos sistemas operativos**, pero es difícil conseguirlo con el tiempo que hay tan ajustado para impartir el currículum completo. Se pueden aprovechar para este propósito los tiempos dedicados a las **prácticas de ampliación**.

Espero que os resulte, cuanto menos, interesante. Quizás las circunstancias actuales no sean las idóneas para poner en práctica algo así por primera vez. Comenzamos un curso lleno de incertidumbres, en el que es probable que tengamos que modificar nuestra planificación prácticamente cada día. Si logro llevar a cabo una buena estrategia que pueda replicarse, seréis los primeros en enteraros. **Espero que vosotros también la compartáis en ese caso**.

Mucho ánimo y **buena suerte**.


