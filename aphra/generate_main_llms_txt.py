import os
import toml

CONFIG_PATH = "site/config.toml"
OUTPUT_PATH = "site/static/llms.txt"

def parse_config():
    """Parses the site/config.toml file to extract blog titles, baseURL, and defaultContentLanguage."""
    try:
        with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
            config = toml.load(f)
        
        es_title = config.get("languages", {}).get("es", {}).get("title", "Blog Title ES")
        en_title = config.get("languages", {}).get("en", {}).get("title", "Blog Title EN")
        base_url = config.get("baseURL", "http://localhost:1313")
        default_content_language = config.get("defaultContentLanguage", "es")
        
        return {
            "es_title": es_title,
            "en_title": en_title,
            "base_url": base_url,
            "default_content_language": default_content_language,
        }
    except FileNotFoundError:
        print(f"Error: Config file not found at {CONFIG_PATH}")
        # Provide default values if config file is not found
        return {
            "es_title": "Blog Title ES (Default)",
            "en_title": "Blog Title EN (Default)",
            "base_url": "http://localhost:1313",
            "default_content_language": "es",
        }
    except Exception as e:
        print(f"Error parsing config file: {e}")
        # Provide default values in case of other errors
        return {
            "es_title": "Blog Title ES (Default)",
            "en_title": "Blog Title EN (Default)",
            "base_url": "http://localhost:1313",
            "default_content_language": "es",
        }

def generate_llms_txt_content(config_data):
    """Generates the Markdown content for llms.txt."""
    
    # Use Spanish title as default for the main llms.txt
    blog_title = config_data["es_title"]
    base_url = config_data["base_url"]
    
    content = []
    
    # H1 Header
    content.append(f"# {blog_title}")
    content.append("")
    
    # Attempt to extract summary
    summary_md_path = "site/content/es/sobre-el-blog.md"
    summary = extract_summary_from_md(summary_md_path)
    
    if summary:
        content.append(f"> {summary}")
    else:
        content.append("> Summary could not be automatically generated.")
    content.append("")
    
    # General Information section
    content.append("## Información General")
    content.append("")
    
    general_pages_es = [
        {'title': 'Sobre el blog', 'slug': 'sobre-el-blog'},
        {'title': 'Cómo se hace', 'slug': 'como-se-hace'},
    ]
    
    for page in general_pages_es:
        # Ensure clean URLs by stripping any trailing slash from base_url and then adding segments
        clean_base_url = base_url.rstrip('/')
        # Assuming pages are under content/es/ for Spanish
        # Link format: [<title>](<clean_base_url>/<lang>/<slug>.md)
        # Actual URL will be base_url + /es/slug (without .md for website navigation)
        # For llms.txt, we are linking to the source .md files for now
        content.append(f"- [{page['title']}]({clean_base_url}/es/{page['slug']}.md)")
    content.append("")
    
    # Blog Posts section
    content.append("## Artículos del Blog")
    content.append("")

    es_posts_dir = os.path.join("site", "content", "es", "posts")
    en_posts_dir = os.path.join("site", "content", "en", "posts")

    es_posts = get_blog_posts(es_posts_dir, "es", base_url)
    en_posts = get_blog_posts(en_posts_dir, "en", base_url)

    if es_posts:
        content.append("### Español")
        for post in es_posts:
            content.append(f"- [{post['title']}]({post['url']})")
        content.append("")
    else:
        content.append("### Español")
        content.append("- No posts found for this language.")
        content.append("")

    if en_posts:
        content.append("### English")
        for post in en_posts:
            content.append(f"- [{post['title']}]({post['url']})")
        content.append("")
    else:
        content.append("### English")
        content.append("- No posts found for this language.")
        content.append("")
        
    return "\n".join(content)

def extract_title_from_md(filepath, default_title):
    """
    Extracts a title from a Markdown file's front matter.
    Looks for 'title:' in YAML front matter.
    If not found, returns the default_title.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines_raw = f.readlines()
        
        lines = [line.rstrip('\n') for line in lines_raw]

        if not lines:
            return default_title

        if lines[0] == "---": # Check for front matter
            for line in lines[1:]: # Skip the first '---'
                if line == "---": # End of front matter
                    break
                if ':' in line:
                    key, *value_parts = line.split(':', 1)
                    key = key.strip()
                    value = value_parts[0].strip().strip('"').strip("'") if value_parts else ""
                    if key == "title" and value:
                        return value
        return default_title # Title not found in front matter or no front matter
    except FileNotFoundError:
        # print(f"Warning: Title file not found at {filepath}. Using default: {default_title}")
        return default_title
    except Exception as e:
        print(f"Error extracting title from {filepath}: {e}. Using default: {default_title}")
        return default_title

def get_blog_posts(posts_dir_path, lang, base_url):
    """
    Scans a directory for blog posts and extracts their titles and URLs.
    """
    posts = []
    if not os.path.isdir(posts_dir_path):
        # print(f"Warning: Posts directory not found: {posts_dir_path}")
        return posts

    for slug in os.listdir(posts_dir_path):
        post_subdir = os.path.join(posts_dir_path, slug)
        if os.path.isdir(post_subdir):
            index_md_path = os.path.join(post_subdir, "index.md")
            
            # Default title is the slug, formatted nicely (e.g., "my-post-slug" -> "My Post Slug")
            # For simplicity, just replacing hyphens with spaces and title casing for now.
            formatted_slug_title = slug.replace('-', ' ').title()
            
            title = extract_title_from_md(index_md_path, formatted_slug_title)
            
            clean_base_url = base_url.rstrip('/')
            # Link to the llms.txt for each post
            url = f"{clean_base_url}/{lang}/posts/{slug}/llms.txt"
            posts.append({'title': title, 'url': url})
            
            # Generate the post-specific llms.txt file
            generate_post_llms_file(post_subdir, title, lang)
            
    return sorted(posts, key=lambda p: p['title']) # Sort posts by title

def generate_post_llms_file(post_dir_path, post_title, lang):
    """
    Generates an llms.txt file for a specific blog post.
    post_dir_path: Absolute path to the post's content directory.
    post_title: The title of the post.
    lang: The language code ('es' or 'en').
    """
    content = []
    content.append(f"# {post_title}")
    content.append("")
    
    if lang == "es":
        content.append("## Contenido")
        content.append("")
        content.append("- [Leer Artículo](index.md)")
    elif lang == "en":
        content.append("## Content")
        content.append("")
        content.append("- [Read Post](index.md)")
    else:
        # Fallback for any other language, though not strictly needed by current spec
        content.append("## Content")
        content.append("")
        content.append("- [Read Post](index.md)")
        
    output_filepath = os.path.join(post_dir_path, "llms.txt")
    
    try:
        with open(output_filepath, 'w', encoding='utf-8') as f:
            f.write("\n".join(content))
        # print(f"Successfully generated post llms.txt: {output_filepath}")
    except Exception as e:
        print(f"Error writing post llms.txt file at {output_filepath}: {e}")


def write_llms_txt(content):
    """Writes the generated content to site/static/llms.txt."""
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Successfully generated {OUTPUT_PATH}")

def extract_summary_from_md(filepath):
    """
    Extracts a summary from a Markdown file.
    Tries to find 'description:' or 'summary:' in YAML front matter.
    If not found, takes the first non-empty line after front matter.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines_raw = f.readlines()
        
        lines = [line.rstrip('\n') for line in lines_raw] # Strip newlines for easier processing
        
        front_matter_parsed = False
        content_start_index = 0

        if not lines:
            return None

        # Try to parse front matter
        if lines[0] == "---":
            front_matter_lines = []
            for i, line in enumerate(lines):
                if i == 0:
                    continue # Skip the first '---'
                if line == "---":
                    front_matter_parsed = True
                    content_start_index = i + 1
                    break
                front_matter_lines.append(line)
            else: # No closing '---' found, treat as no front matter or malformed
                front_matter_parsed = False 
                content_start_index = 0 # Process all lines as content if malformed

            if front_matter_parsed:
                for fm_line in front_matter_lines:
                    if ':' in fm_line:
                        key, *value_parts = fm_line.split(':', 1)
                        key = key.strip()
                        value = value_parts[0].strip().strip('"').strip("'") if value_parts else ""
                        if (key == "description" or key == "summary") and value:
                            return value
        
        # If no summary from front matter, or no front matter, find first non-empty content line
        for i in range(content_start_index, len(lines)):
            line_content = lines[i].strip()
            # Skip any remaining front matter lines if it was malformed and we didn't find summary
            if line_content and line_content != "---": 
                return line_content
                
        return None # No suitable summary found

    except FileNotFoundError:
        print(f"Warning: Summary file not found at {filepath}")
        return None
    except Exception as e:
        print(f"Error extracting summary from {filepath}: {e}")
        return None

def main():
    """Main function to generate llms.txt."""
    config_data = parse_config()
    llms_txt_content = generate_llms_txt_content(config_data)
    write_llms_txt(llms_txt_content)

if __name__ == "__main__":
    main()
