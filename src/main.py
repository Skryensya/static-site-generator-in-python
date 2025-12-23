from copy_assets import copy_assets
from generate_pages_recursive import generate_pages_recursive

def main():
    copy_assets(source_dir="static", destination_dir="public")
    generate_pages_recursive("content", "template.html" , "public")
    

if __name__ == "__main__":
    main()