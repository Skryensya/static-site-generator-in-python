import os 
from markdown_to_html_node import markdown_to_html_node
from extract_title import extract_title


def replace_section(section_to_replace, template, content):
    delimeter = "{{ " + section_to_replace + " }}"
    parts = template.split(delimeter) 
    return f"{content}".join(parts)

def create_file(dest, content): 
    containing_folders = dest.rsplit("/", 1)[0] 
    os.makedirs(containing_folders, exist_ok=True)
    with open(dest, "w") as file:
        file.write(content)


def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    abs_from_path = os.path.abspath(from_path)
    abs_template_path = os.path.abspath(template_path)
    abs_dest_path = os.path.abspath(dest_path)

    if not os.path.exists(abs_from_path):
        raise Exception("Content does not exist")
    
    if not os.path.exists(abs_template_path):
        raise Exception("Template does not exists")
    
    content = None
    with open(abs_from_path, mode="r") as content_f:
        content = content_f.read() 

    template = None
    with open(abs_template_path, mode="r") as template_f:
        template = template_f.read() 

    title = extract_title(content)
    content_html = markdown_to_html_node(content).to_html()

    # print(content_html)
    page = replace_section("Title", template, title)
    page = replace_section("Content", page, content_html)
    page = page.replace('href="/', f'href="{basepath}')
    page = page.replace('src="/', f'src="{basepath}')

    create_file(abs_dest_path, page)
    # print(page)

    # Use your markdown_to_html_node function and .to_html() method to convert the markdown file to an HTML string.

    # extract Title

    # Replace the {{ Title }} and {{ Content }} placeholders in the template with the HTML and title you generated.

    # create the new page in dest_path




    pass


     