from copy_assets import copy_assets
from generate_page import generate_page

def main():
    copy_assets(source_dir="static", destination_dir="public")
    generate_page("content/index.md", "template.html", "public/index.html")
    

if __name__ == "__main__":
    main()