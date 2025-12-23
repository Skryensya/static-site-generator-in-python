import os 
from markdown_to_html_node import markdown_to_html_node
from extract_title import extract_title

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    abs_from_path = os.path.abspath(from_path)
    abs_template_path = os.path.abspath(template_path)
    abs_dest_path = os.path.abspath(dest_path)

    if not os.path.exists(abs_from_path):
        raise Exception("Content does not exist")
    
    if not os.path.exists(abs_template_path):
        raise Exception("Template does not exists")

    content = open(abs_from_path, mode="r").read()
    template = open(abs_template_path, mode="r").read()

    title = extract_title(content)
    content_html = markdown_to_html_node(content)

    print(content_html.to_html())

    # Use your markdown_to_html_node function and .to_html() method to convert the markdown file to an HTML string.

    # extract Title

    # Replace the {{ Title }} and {{ Content }} placeholders in the template with the HTML and title you generated.

    # create the new page in dest_path




    pass