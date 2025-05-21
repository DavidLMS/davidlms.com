import unittest
from unittest.mock import patch, mock_open, MagicMock
import os
import toml # The script uses toml, so tests might need it for creating mock return values

# Assuming generate_main_llms_txt.py is in the same directory or PYTHONPATH is set up
# For testing, we'll import the functions directly from the script.
# To do this, ensure aphra is discoverable, e.g. by running tests from parent dir
# or by adjusting sys.path. For now, let's assume it can be imported.
from aphra.generate_main_llms_txt import (
    parse_config,
    extract_summary_from_md,
    extract_title_from_md,
    generate_post_llms_file,
    get_blog_posts,
    generate_llms_txt_content # Optional, as per task
)

# Define the path to the script being tested for easier reference if needed
SCRIPT_PATH = "aphra.generate_main_llms_txt"

class TestParseConfig(unittest.TestCase):

    @patch(f"{SCRIPT_PATH}.open", new_callable=mock_open)
    def test_parse_config_success(self, mock_file_open):
        dummy_toml_content = """
baseURL = "https://example.com/"
defaultContentLanguage = "en"
title = "My Main Blog Title" # This is for the global title, not language specific

[languages.en]
title = "My English Blog Title"
weight = 1

[languages.es]
title = "Mi Título de Blog en Español"
weight = 2
"""
        mock_file_open.return_value.read.return_value = dummy_toml_content
        
        # Mock toml.load to behave as if it parsed the content
        # Normally, toml.load takes a file object, so we need to mock its behavior
        # based on the string content.
        # A simpler way for this specific mock is to have toml.load return the parsed dict directly
        # when called with the mocked file object.
        parsed_dummy_toml = {
            "baseURL": "https://example.com/",
            "defaultContentLanguage": "en",
            "title": "My Main Blog Title",
            "languages": {
                "en": {"title": "My English Blog Title", "weight": 1},
                "es": {"title": "Mi Título de Blog en Español", "weight": 2}
            }
        }

        with patch(f"{SCRIPT_PATH}.toml.load", return_value=parsed_dummy_toml) as mock_toml_load:
            config = parse_config()
            self.assertEqual(config["base_url"], "https://example.com/")
            self.assertEqual(config["default_content_language"], "en")
            self.assertEqual(config["en_title"], "My English Blog Title")
            self.assertEqual(config["es_title"], "Mi Título de Blog en Español")
            mock_file_open.assert_called_once_with("site/config.toml", 'r', encoding='utf-8')
            mock_toml_load.assert_called_once() # Check that toml.load was called

    @patch(f"{SCRIPT_PATH}.open", new_callable=mock_open)
    def test_parse_config_missing_keys_fallback(self, mock_file_open):
        dummy_toml_content = """
baseURL = "https://fallback.com/"
# Missing defaultContentLanguage, title, and specific language titles
"""
        mock_file_open.return_value.read.return_value = dummy_toml_content
        parsed_dummy_toml = {"baseURL": "https://fallback.com/"} # Simulate toml.load output

        with patch(f"{SCRIPT_PATH}.toml.load", return_value=parsed_dummy_toml):
            config = parse_config()
            self.assertEqual(config["base_url"], "https://fallback.com/")
            self.assertEqual(config["default_content_language"], "es") # Default fallback
            self.assertEqual(config["en_title"], "Blog Title EN") # Default fallback
            self.assertEqual(config["es_title"], "Blog Title ES") # Default fallback

    @patch(f"{SCRIPT_PATH}.open", side_effect=FileNotFoundError)
    @patch(f"{SCRIPT_PATH}.print") # Mock print to suppress error messages during test
    def test_parse_config_file_not_found(self, mock_print, mock_file_open):
        config = parse_config()
        self.assertEqual(config["base_url"], "http://localhost:1313") # Default
        self.assertEqual(config["default_content_language"], "es")
        self.assertEqual(config["en_title"], "Blog Title EN (Default)")
        self.assertEqual(config["es_title"], "Blog Title ES (Default)")
        mock_print.assert_any_call("Error: Config file not found at site/config.toml")

# Custom exception for controlled string representation in tests
class MockTomlDecodeError(toml.TomlDecodeError):
    def __init__(self, msg, doc, pos):
        super().__init__(msg, doc, pos) # Call parent if it matters for other things
        self.custom_msg = msg # Store the clean message
    def __str__(self):
        return self.custom_msg # Return only the clean message

class TestParseConfig(unittest.TestCase): # Ensure this class is defined before it's used by TestExtractSummaryFromMd

    @patch(f"{SCRIPT_PATH}.open", new_callable=mock_open)
    def test_parse_config_success(self, mock_file_open):
        dummy_toml_content = """
baseURL = "https://example.com/"
defaultContentLanguage = "en"
title = "My Main Blog Title" # This is for the global title, not language specific

[languages.en]
title = "My English Blog Title"
weight = 1

[languages.es]
title = "Mi Título de Blog en Español"
weight = 2
"""
        mock_file_open.return_value.read.return_value = dummy_toml_content
        
        parsed_dummy_toml = {
            "baseURL": "https://example.com/",
            "defaultContentLanguage": "en",
            "title": "My Main Blog Title",
            "languages": {
                "en": {"title": "My English Blog Title", "weight": 1},
                "es": {"title": "Mi Título de Blog en Español", "weight": 2}
            }
        }

        with patch(f"{SCRIPT_PATH}.toml.load", return_value=parsed_dummy_toml) as mock_toml_load:
            config = parse_config()
            self.assertEqual(config["base_url"], "https://example.com/")
            self.assertEqual(config["default_content_language"], "en")
            self.assertEqual(config["en_title"], "My English Blog Title")
            self.assertEqual(config["es_title"], "Mi Título de Blog en Español")
            mock_file_open.assert_called_once_with("site/config.toml", 'r', encoding='utf-8')
            mock_toml_load.assert_called_once() 

    @patch(f"{SCRIPT_PATH}.open", new_callable=mock_open)
    def test_parse_config_missing_keys_fallback(self, mock_file_open):
        dummy_toml_content = """
baseURL = "https://fallback.com/"
"""
        mock_file_open.return_value.read.return_value = dummy_toml_content
        parsed_dummy_toml = {"baseURL": "https://fallback.com/"}

        with patch(f"{SCRIPT_PATH}.toml.load", return_value=parsed_dummy_toml):
            config = parse_config()
            self.assertEqual(config["base_url"], "https://fallback.com/")
            self.assertEqual(config["default_content_language"], "es") 
            self.assertEqual(config["en_title"], "Blog Title EN") 
            self.assertEqual(config["es_title"], "Blog Title ES") 

    @patch(f"{SCRIPT_PATH}.open", side_effect=FileNotFoundError)
    @patch(f"{SCRIPT_PATH}.print") 
    def test_parse_config_file_not_found(self, mock_print, mock_file_open):
        config = parse_config()
        self.assertEqual(config["base_url"], "http://localhost:1313") 
        self.assertEqual(config["default_content_language"], "es")
        self.assertEqual(config["en_title"], "Blog Title EN (Default)")
        self.assertEqual(config["es_title"], "Blog Title ES (Default)")
        mock_print.assert_any_call("Error: Config file not found at site/config.toml")

    @patch(f"{SCRIPT_PATH}.open", new_callable=mock_open)
    @patch(f"{SCRIPT_PATH}.toml.load", side_effect=lambda f: (_ for _ in ()).throw(MockTomlDecodeError("Mocked TOML error", "dummy_doc_for_err", 0)))
    @patch(f"{SCRIPT_PATH}.print") # Mock print
    def test_parse_config_toml_decode_error(self, mock_print, mock_toml_load, mock_file_open):
        mock_file_open.return_value.read.return_value = "invalid toml content"
        
        config = parse_config()
        self.assertEqual(config["base_url"], "http://localhost:1313") # Default
        self.assertEqual(config["default_content_language"], "es")
        self.assertEqual(config["en_title"], "Blog Title EN (Default)")
        self.assertEqual(config["es_title"], "Blog Title ES (Default)")
        mock_print.assert_any_call("Error parsing config file: Mocked TOML error")

class TestExtractSummaryFromMd(unittest.TestCase):

    @patch(f"{SCRIPT_PATH}.open", new_callable=mock_open)
    def test_extract_from_description(self, mock_file):
        md_content = """---
title: A Post
description: This is the description summary.
---
Some content here.
"""
        mock_file.return_value.read.return_value = md_content # For toml.load if it were called
        mock_file.return_value.readlines.return_value = md_content.splitlines(True)
        summary = extract_summary_from_md("dummy_path.md")
        self.assertEqual(summary, "This is the description summary.")

    @patch(f"{SCRIPT_PATH}.open", new_callable=mock_open)
    def test_extract_from_summary_field(self, mock_file):
        md_content = """---
title: Another Post
summary: This is the summary field value.
---
Content follows.
"""
        mock_file.return_value.readlines.return_value = md_content.splitlines(True)
        summary = extract_summary_from_md("dummy_path.md")
        self.assertEqual(summary, "This is the summary field value.")

    @patch(f"{SCRIPT_PATH}.open", new_callable=mock_open)
    def test_fallback_to_first_content_line(self, mock_file):
        md_content = """---
title: Post Without Summary Key
tags: [test, fallback]
---

This is the first actual content line.
And a second line.
"""
        mock_file.return_value.readlines.return_value = md_content.splitlines(True)
        summary = extract_summary_from_md("dummy_path.md")
        self.assertEqual(summary, "This is the first actual content line.")

    @patch(f"{SCRIPT_PATH}.open", new_callable=mock_open)
    def test_no_front_matter(self, mock_file):
        md_content = """
This is content without any front matter.
It should be the summary.
"""
        # Ensure leading/trailing empty lines are handled if splitlines(True) is used
        mock_file.return_value.readlines.return_value = [l + '\n' for l in md_content.strip().split('\n')]
        summary = extract_summary_from_md("dummy_path.md")
        self.assertEqual(summary, "This is content without any front matter.")

    @patch(f"{SCRIPT_PATH}.open", side_effect=FileNotFoundError)
    @patch(f"{SCRIPT_PATH}.print")
    def test_file_not_found(self, mock_print, mock_file_open):
        summary = extract_summary_from_md("non_existent_path.md")
        self.assertIsNone(summary)
        mock_print.assert_any_call("Warning: Summary file not found at non_existent_path.md")

    @patch(f"{SCRIPT_PATH}.open", new_callable=mock_open)
    def test_empty_file(self, mock_file):
        mock_file.return_value.readlines.return_value = []
        summary = extract_summary_from_md("dummy_empty.md")
        self.assertIsNone(summary)

    @patch(f"{SCRIPT_PATH}.open", new_callable=mock_open)
    def test_only_front_matter_no_summary_key(self, mock_file):
        md_content = """---
title: Only Front Matter
tags: [metadata]
---
"""
        mock_file.return_value.readlines.return_value = md_content.splitlines(True)
        summary = extract_summary_from_md("dummy_only_fm.md")
        self.assertIsNone(summary) # No content lines to fall back to

    @patch(f"{SCRIPT_PATH}.open", new_callable=mock_open)
    def test_front_matter_with_empty_description(self, mock_file):
        md_content = """---
description: 
title: Test
---
Actual first line of content.
"""
        mock_file.return_value.readlines.return_value = md_content.splitlines(True)
        summary = extract_summary_from_md("dummy_path.md")
        self.assertEqual(summary, "Actual first line of content.")

    @patch(f"{SCRIPT_PATH}.open", new_callable=mock_open)
    def test_malformed_front_matter_no_closing_dashes(self, mock_file):
        md_content = """---
title: Malformed
description: This description should not be picked if logic relies on closing --- for content.
This is a content line.
"""
        # The current implementation should still find description if it's before content start.
        # If it doesn't find description/summary, it treats lines as content.
        mock_file.return_value.readlines.return_value = md_content.splitlines(True)
        summary = extract_summary_from_md("dummy_malformed.md")
        # Depending on strictness, this could be "This description..." or "This is a content line."
        # For malformed front matter (no closing '---'), the current script logic:
        # 1. Tries to parse front matter. Fails to find closing '---', so content_start_index becomes 0.
        # 2. It does NOT extract description/summary from the incomplete front matter in this case.
        # 3. Iterates for content from line 0. Skips '---'. Returns 'title: Malformed'.
        self.assertEqual(summary, "title: Malformed")
        
    @patch(f"{SCRIPT_PATH}.open", new_callable=mock_open)
    def test_content_starts_immediately_after_closing_front_matter(self, mock_file):
        md_content = """---
title: A Post
---
This is the first content line immediately after front matter.
"""
        mock_file.return_value.readlines.return_value = md_content.splitlines(True)
        summary = extract_summary_from_md("dummy_path.md")
        self.assertEqual(summary, "This is the first content line immediately after front matter.")

class TestExtractTitleFromMd(unittest.TestCase):

    @patch(f"{SCRIPT_PATH}.open", new_callable=mock_open)
    def test_extract_title_from_front_matter(self, mock_file):
        md_content = """---
title: This is the Real Title
description: Some description.
---
Content.
"""
        mock_file.return_value.readlines.return_value = md_content.splitlines(True)
        title = extract_title_from_md("dummy_path.md", "Default Title")
        self.assertEqual(title, "This is the Real Title")

    @patch(f"{SCRIPT_PATH}.open", new_callable=mock_open)
    def test_fallback_to_default_title_if_no_title_key(self, mock_file):
        md_content = """---
description: Some description.
tags: [no, title]
---
Content.
"""
        mock_file.return_value.readlines.return_value = md_content.splitlines(True)
        title = extract_title_from_md("dummy_path.md", "Default Fallback Title")
        self.assertEqual(title, "Default Fallback Title")

    @patch(f"{SCRIPT_PATH}.open", new_callable=mock_open)
    def test_fallback_to_default_title_if_no_front_matter(self, mock_file):
        md_content = "Just content here, no front matter."
        mock_file.return_value.readlines.return_value = md_content.splitlines(True)
        title = extract_title_from_md("dummy_path.md", "Default Title For No FM")
        self.assertEqual(title, "Default Title For No FM")

    @patch(f"{SCRIPT_PATH}.open", side_effect=FileNotFoundError)
    @patch(f"{SCRIPT_PATH}.print") # Suppress print warnings during test
    def test_file_not_found_returns_default_title(self, mock_print, mock_file_open):
        title = extract_title_from_md("non_existent.md", "Default For Not Found")
        self.assertEqual(title, "Default For Not Found")
        # The function is designed to print a warning, but for this test,
        # we only care that it returns the default title.
        # We can assert that print was called if needed, but it's commented out in the main script.
        # mock_print.assert_any_call("Warning: Title file not found at non_existent.md. Using default: Default For Not Found")


    @patch(f"{SCRIPT_PATH}.open", new_callable=mock_open)
    def test_empty_file_returns_default_title(self, mock_file):
        mock_file.return_value.readlines.return_value = []
        title = extract_title_from_md("empty.md", "Default For Empty")
        self.assertEqual(title, "Default For Empty")
        
    @patch(f"{SCRIPT_PATH}.open", new_callable=mock_open)
    def test_title_key_present_but_empty_value_returns_default(self, mock_file):
        md_content = """---
title: 
description: Some description.
---
Content.
"""
        mock_file.return_value.readlines.return_value = md_content.splitlines(True)
        title = extract_title_from_md("dummy_path.md", "Default Title Empty Val")
        self.assertEqual(title, "Default Title Empty Val")

class TestGeneratePostLlmsFile(unittest.TestCase):

    @patch(f"{SCRIPT_PATH}.open", new_callable=mock_open)
    def test_generate_for_spanish_post(self, mock_file):
        post_dir = "site/content/es/posts/un-post-espanol"
        post_title = "Un Post en Español"
        lang = "es"
        
        generate_post_llms_file(post_dir, post_title, lang)
        
        expected_output_path = os.path.join(post_dir, "llms.txt")
        mock_file.assert_called_once_with(expected_output_path, 'w', encoding='utf-8')
        
        # Get the content written to the mock file
        # mock_file() gives the mock file object, call .write() on it to see what was written.
        # The actual write call is done by f.write("\n".join(content))
        written_content = mock_file().write.call_args[0][0]
        
        expected_content = [
            f"# {post_title}",
            "",
            "## Contenido",
            "",
            "- [Leer Artículo](index.md)"
        ]
        self.assertEqual(written_content, "\n".join(expected_content))

    @patch(f"{SCRIPT_PATH}.open", new_callable=mock_open)
    def test_generate_for_english_post(self, mock_file):
        post_dir = "site/content/en/posts/an-english-post"
        post_title = "An English Post"
        lang = "en"
        
        generate_post_llms_file(post_dir, post_title, lang)
        
        expected_output_path = os.path.join(post_dir, "llms.txt")
        mock_file.assert_called_once_with(expected_output_path, 'w', encoding='utf-8')
        
        written_content = mock_file().write.call_args[0][0]
        expected_content = [
            f"# {post_title}",
            "",
            "## Content",
            "",
            "- [Read Post](index.md)"
        ]
        self.assertEqual(written_content, "\n".join(expected_content))

    @patch(f"{SCRIPT_PATH}.open", side_effect=IOError("Test disk full"))
    @patch(f"{SCRIPT_PATH}.print")
    def test_file_write_exception(self, mock_print, mock_file_open):
        post_dir = "site/content/es/posts/error-post"
        post_title = "Error Post"
        lang = "es"

        generate_post_llms_file(post_dir, post_title, lang)

        expected_output_path = os.path.join(post_dir, "llms.txt")
        mock_print.assert_called_with(f"Error writing post llms.txt file at {expected_output_path}: Test disk full")

class TestGetBlogPosts(unittest.TestCase):

    @patch(f"{SCRIPT_PATH}.generate_post_llms_file") # Mock the function that writes post llms files
    @patch(f"{SCRIPT_PATH}.extract_title_from_md")
    @patch(f"{SCRIPT_PATH}.os.path.isdir")
    @patch(f"{SCRIPT_PATH}.os.listdir")
    def test_get_blog_posts_flow(self, mock_listdir, mock_isdir, mock_extract_title, mock_generate_post_file):
        posts_dir = "site/content/es/posts"
        lang = "es"
        base_url = "https://example.com"

        # Setup mocks
        mock_listdir.return_value = ["post-uno", "post-dos-con-titulo"]
        
        def isdir_side_effect(path):
            # Must return True for the main posts_dir itself
            if path == posts_dir:
                return True
            # And for the subdirectories
            if path in [os.path.join(posts_dir, "post-uno"), os.path.join(posts_dir, "post-dos-con-titulo")]:
                return True
            return False
        mock_isdir.side_effect = isdir_side_effect

        # extract_title_from_md needs to return specific titles
        def extract_title_side_effect(filepath, default_title):
            if "post-uno" in filepath:
                return default_title # Test fallback to slug-based title
            elif "post-dos-con-titulo" in filepath:
                return "Título Real del Post Dos"
            return default_title
        mock_extract_title.side_effect = extract_title_side_effect

        # Call the function
        posts = get_blog_posts(posts_dir, lang, base_url)

        # Assertions
        mock_listdir.assert_called_once_with(posts_dir)
        self.assertEqual(mock_isdir.call_count, 3) # Main posts_dir + two subdirectories
        
        # Check extract_title_from_md calls
        expected_extract_title_calls = [
            unittest.mock.call(os.path.join(posts_dir, "post-uno", "index.md"), "Post Uno"),
            unittest.mock.call(os.path.join(posts_dir, "post-dos-con-titulo", "index.md"), "Post Dos Con Titulo")
        ]
        # Allow any order for these calls as dictionary iteration order is not guaranteed for older Python versions
        mock_extract_title.assert_has_calls(expected_extract_title_calls, any_order=True)


        # Check generate_post_llms_file calls
        expected_generate_calls = [
            unittest.mock.call(os.path.join(posts_dir, "post-uno"), "Post Uno", lang),
            unittest.mock.call(os.path.join(posts_dir, "post-dos-con-titulo"), "Título Real del Post Dos", lang)
        ]
        mock_generate_post_file.assert_has_calls(expected_generate_calls, any_order=True)
        self.assertEqual(mock_generate_post_file.call_count, 2)


        # Check returned posts data (sorted by title)
        # "Post Uno" comes before "Título Real del Post Dos" when sorted
        expected_posts_data = [
            {'title': "Post Uno", 'url': "https://example.com/es/posts/post-uno/llms.txt"},
            {'title': "Título Real del Post Dos", 'url': "https://example.com/es/posts/post-dos-con-titulo/llms.txt"}
        ]
        # Sort the actual posts list by title to match expected order
        sorted_posts = sorted(posts, key=lambda p: p['title'])
        self.assertEqual(sorted_posts, expected_posts_data)

    @patch(f"{SCRIPT_PATH}.os.path.isdir", return_value=False) # Simulate posts_dir not existing
    @patch(f"{SCRIPT_PATH}.print")
    def test_get_blog_posts_no_post_dir(self, mock_print, mock_isdir):
        posts = get_blog_posts("non_existent_dir/posts", "es", "https://example.com")
        self.assertEqual(posts, [])
        # The warning print is commented out in the original script, so no print call to assert
        # mock_print.assert_any_call("Warning: Posts directory not found: non_existent_dir/posts")

    @patch(f"{SCRIPT_PATH}.os.path.isdir", return_value=True)
    @patch(f"{SCRIPT_PATH}.os.listdir", return_value=[]) # Empty directory
    def test_get_blog_posts_empty_post_dir(self, mock_listdir, mock_isdir):
        posts = get_blog_posts("empty_dir/posts", "es", "https://example.com")
        self.assertEqual(posts, [])
        mock_listdir.assert_called_once_with("empty_dir/posts")

class TestGenerateLlmsTxtContent(unittest.TestCase):

    @patch(f"{SCRIPT_PATH}.get_blog_posts")
    @patch(f"{SCRIPT_PATH}.extract_summary_from_md")
    # No need to mock parse_config here as it's not called by generate_llms_txt_content
    def test_generate_llms_txt_content_structure(self, mock_extract_summary, mock_get_blog_posts):
        # Setup mock return values for generate_llms_txt_content's direct inputs/dependencies
        # mock_parse_config.return_value was removed, define config_data directly
        config_data = { 
            "es_title": "Blog de Prueba ES",
            "en_title": "Test Blog EN", # Not directly used by this specific llms.txt
            "base_url": "https://mytestblog.com/",
            "default_content_language": "es"
        }
        mock_extract_summary.return_value = "Este es un resumen de prueba."
        
        mock_es_posts = [
            {'title': 'Post Español Uno', 'url': 'https://mytestblog.com/es/posts/post-espanol-uno/llms.txt'},
            {'title': 'Post Español Dos', 'url': 'https://mytestblog.com/es/posts/post-espanol-dos/llms.txt'}
        ]
        mock_en_posts = [
            {'title': 'English Post One', 'url': 'https://mytestblog.com/en/posts/english-post-one/llms.txt'}
        ]
        
        # Configure get_blog_posts mock to return different values based on language
        def get_blog_posts_side_effect(posts_dir, lang, base_url):
            if lang == "es":
                return mock_es_posts
            elif lang == "en":
                return mock_en_posts
            return []
        mock_get_blog_posts.side_effect = get_blog_posts_side_effect

        # Generate content
        # config_data = mock_parse_config.return_value # This line was the error, config_data is defined above
        generated_output = generate_llms_txt_content(config_data)

        # Expected structure (simplified check)
        self.assertIn("# Blog de Prueba ES", generated_output)
        self.assertIn("> Este es un resumen de prueba.", generated_output)
        self.assertIn("## Información General", generated_output)
        self.assertIn("- [Sobre el blog](https://mytestblog.com/es/sobre-el-blog.md)", generated_output)
        self.assertIn("## Artículos del Blog", generated_output)
        self.assertIn("### Español", generated_output)
        self.assertIn("- [Post Español Uno](https://mytestblog.com/es/posts/post-espanol-uno/llms.txt)", generated_output)
        self.assertIn("- [Post Español Dos](https://mytestblog.com/es/posts/post-espanol-dos/llms.txt)", generated_output)
        self.assertIn("### English", generated_output)
        self.assertIn("- [English Post One](https://mytestblog.com/en/posts/english-post-one/llms.txt)", generated_output)

        # Verify mocks were called
        mock_extract_summary.assert_called_once_with("site/content/es/sobre-el-blog.md")
        
        expected_get_posts_calls = [
            unittest.mock.call(os.path.join("site", "content", "es", "posts"), "es", "https://mytestblog.com/"),
            unittest.mock.call(os.path.join("site", "content", "en", "posts"), "en", "https://mytestblog.com/")
        ]
        mock_get_blog_posts.assert_has_calls(expected_get_posts_calls, any_order=False)


    @patch(f"{SCRIPT_PATH}.get_blog_posts", return_value=[]) # No posts for any language
    @patch(f"{SCRIPT_PATH}.extract_summary_from_md", return_value="Resumen sin posts.")
    def test_generate_llms_txt_content_no_posts(self, mock_extract_summary, mock_get_blog_posts):
        config_data = { # This data is assumed to be passed in
            "es_title": "Blog Sin Posts",
            "base_url": "https://noposts.com/",
            "default_content_language": "es"
        }
        generated_output = generate_llms_txt_content(config_data)

        self.assertIn("# Blog Sin Posts", generated_output)
        self.assertIn("> Resumen sin posts.", generated_output)
        self.assertIn("### Español", generated_output)
        self.assertIn("- No posts found for this language.", generated_output)
        self.assertIn("### English", generated_output)
        # The line below should also be present for English if get_blog_posts is called for it and returns []
        self.assertIn("- No posts found for this language.", generated_output.split("### English")[1])


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
