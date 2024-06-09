from markdown.extensions import Extension
from markdown.preprocessors import Preprocessor
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
import markdown
from . import css
from . import js
from bs4 import BeautifulSoup
import base64


class CodeBlockPreprocessor(Preprocessor):
    def run(self, lines):
        new_lines = []
        language = None
        in_code_block = False
        code_block_lines = []

        for line in lines:
            if line.startswith("```"):
                in_code_block = not in_code_block

                if in_code_block:
                    language = line.strip()[3:]
                else:
                    if code_block_lines:
                        lexer = get_lexer_by_name(language)
                        formatter = HtmlFormatter()
                        highlighted = highlight(
                            "\n".join(code_block_lines), lexer, formatter
                        )
                        new_lines.append(highlighted)
                        code_block_lines = []
                    language = None

                # Do not append the line with backticks and language specification
            elif in_code_block and language:
                code_block_lines.append(line)
            else:
                new_lines.append(line)

        return new_lines


class CodeBlockExtension(Extension):
    def extendMarkdown(self, md):
        md.registerExtension(self)
        md.preprocessors.register(CodeBlockPreprocessor(md), "code_block", 175)


def convert_md_to_html(md_file, name, icon):
    # Read the markdown file
    with open(md_file, "r") as file:
        md_content = file.read()

    if icon:
        # Determine the MIME type of the icon file based on its extension
        extension = icon.split(".")[-1]
        if extension.lower() == "png":
            mime_type = "image/png"
        elif extension.lower() == "jpg" or extension.lower() == "jpeg":
            mime_type = "image/jpeg"
        elif extension.lower() == "gif":
            mime_type = "image/gif"
        else:
            raise ValueError(f"Unsupported icon file extension: {extension}")

        # Base64 encode the icon file
        icon = base64.b64encode(open(icon, "rb").read()).decode("utf-8")

        # Create the data URL for the icon
        icon_data_url = f"data:{mime_type};base64,{icon}"

    # Convert markdown to HTML with fenced code blocks and TOC
    md = markdown.Markdown(extensions=[CodeBlockExtension(), "toc"])
    html_content = md.convert(md_content)

    # Get the CSS styles for the syntax highlighting
    formatter = HtmlFormatter()
    highlight_css = formatter.get_style_defs(".highlight")

    css_content = css.get_css()

    js_content = js.get_js()

    # Create the final HTML content with custom CSS and JS
    final_html = (
        f"""
<!DOCTYPE html>
<html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta charset="UTF-8">
        <meta name="description" content="Documentation for {name}">
        """
        + (f'<link rel="icon" href="{icon_data_url}">' if icon else "")
        + f"""
        <title>{name}</title>
        <style>{css_content}</style>
        <style>{highlight_css}</style>
    </head>
    <body>
        <div class="sidebar">
            <h1>Table of Contents</h1>
            {md.toc}
        </div>
        <div class="main-content">
        {html_content}
        </div>
        <script>{js_content}</script>
    </body>
</html>
"""
    )

    # Prettify the HTML
    soup = BeautifulSoup(final_html, "html.parser")
    pretty_html = soup.prettify()

    return pretty_html

def main():
    import argparse

    argparser = argparse.ArgumentParser()
    argparser.add_argument("input", help="Input markdown file")
    argparser.add_argument("output", help="Output HTML file")
    argparser.add_argument(
        "--name", "-n", help="Documentation Name", default="Documentation"
    )
    argparser.add_argument(
        "--icon", "-i", help="Icon file for the documentation", default=""
    )
    args = argparser.parse_args()

    html_content = convert_md_to_html(args.input, args.name, args.icon)

    with open(args.output, "w") as file:
        file.write(html_content)
