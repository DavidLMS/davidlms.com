# davidlms.com

## ¿De qué trata este repositorio?

En este repositorio se aloja un blog personal estático, que se realiza usando el framework [Hugo](https://gohugo.io/) y se despliega en [Netlify](https://www.netlify.com/). Puedes comprobar si el build es correcto en el siguiente banner:

[![Netlify Status](https://api.netlify.com/api/v1/badges/c66a178c-3963-41b8-9afb-5daaf0344047/deploy-status)](https://app.netlify.com/sites/ecstatic-aryabhata-bdb1da/deploys)

También puedes consultar más detalladamente [cómo se realiza](https://davidlms.com/page/como-se-hace/).

## ¿Cómo accedo al blog?

Puedes hacerlo en [davidlms.com](https://davidlms.com)

## ¿Qué tipo de contenido puedo encontrar?

Es un blog personal. Y, como tal, recogerá lo que me apetezca escribir en momentos determinados: reflexiones, tutoriales, experiencias o incluso colaboraciones de otras personas si se tercia. Por lo tanto, debo advertir que todo lo que aquí se plasme únicamente recogerá una opinión en un momento determinado, susceptible de cambiar al siguiente minuto de su publicación. También es posible que los textos contengan un gran porcentaje de ironía. Me gusta jugar con la ambigüedad, lamento profundamente si a alguien este aspecto le saca de quicio, no puede manejar la disonancia cognitiva y lo confunde con incoherencia.

## `llms.txt` Generation

Este proyecto implementa archivos `llms.txt` para ayudar a los Modelos de Lenguaje Grandes (LLMs) a comprender el contenido del blog, siguiendo el estándar propuesto en [llmstxt.org](https://llmstxt.org/). Estos archivos proporcionan metadatos y enlaces estructurados que facilitan la indexación y el entendimiento del sitio por parte de los LLMs.

### Main `llms.txt` File

*   **Location:** `site/static/llms.txt` (Este archivo estará disponible en `/llms.txt` en el sitio desplegado).
*   **Content:**
    *   Título del blog.
    *   Un resumen general del blog (extraído de la página "Sobre el blog").
    *   Enlaces a páginas generales importantes (ej. "Sobre el blog", "Cómo se hace").
    *   Enlaces a los archivos `llms.txt` específicos de cada artículo del blog, categorizados por idioma (Español e Inglés).

### Post-Specific `llms.txt` Files

*   **Location:** `site/content/<lang>/posts/<post-slug>/llms.txt` (donde `<lang>` es el código de idioma, ej. `es` o `en`, y `<post-slug>` es el identificador del artículo).
*   **Content:**
    *   El título del artículo específico.
    *   Un enlace directo al contenido Markdown del artículo (`index.md`).

### Generation Script

Todos los archivos `llms.txt` (tanto el principal como los específicos de cada post) son generados automáticamente por el script de Python ubicado en: `aphra/generate_main_llms_txt.py`.

### Automation

La generación y el commit de estos archivos `llms.txt` al repositorio están automatizados mediante una GitHub Action.
*   **Workflow file:** `.github/workflows/generate_llms_txt.yml`
*   **Trigger:** La acción se ejecuta automáticamente en cada `push` a la rama `main`. También puede ser disparada manualmente (`workflow_dispatch`).
*   **Functionality:** La acción se encarga de ejecutar el script de generación, y si detecta cambios en los archivos `llms.txt`, realiza un commit y push automático de estas actualizaciones.

### Manual Execution

Si es necesario generar los archivos `llms.txt` manualmente, se puede ejecutar el script desde la raíz del repositorio:
```bash
python aphra/generate_main_llms_txt.py
```
Asegúrate de tener las dependencias necesarias instaladas. La principal dependencia del script es `toml`:
```bash
pip install toml
```
(Otras dependencias como `openai` pueden ser necesarias si se utiliza la totalidad del paquete `aphra`, pero para `generate_main_llms_txt.py` específicamente, `toml` es la clave).
