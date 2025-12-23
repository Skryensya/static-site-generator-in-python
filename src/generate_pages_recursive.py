from generate_page import generate_page
import os


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    abs_content = os.path.abspath(dir_path_content) 
    abs_dest = os.path.abspath(dest_dir_path)

    for dir in os.listdir(path=abs_content):
        joined_dir = os.path.join(abs_content, dir)
        dest_dir = os.path.join(abs_dest, dir)
       
        if os.path.isfile(joined_dir):
            dest_dir = os.path.join(abs_dest, dir.rsplit(".")[0]+".html")
            generate_page(joined_dir, template_path, dest_dir)
        else:
            generate_pages_recursive(joined_dir, template_path, dest_dir)


    # generate_page("content/index.md", template_path, "public/index.html")
    # generate_page("content/blog/glorfindel/index.md", abs_template, "public/blog/glorfindel/index.html")
    # generate_page("content/blog/tom/index.md", abs_template, "public/blog/tom/index.html")
    # generate_page("content/blog/majesty/index.md", abs_template, "public/blog/majesty/index.html")
    # generate_page("content/contact/index.md", abs_template, "public/contact/index.html")
