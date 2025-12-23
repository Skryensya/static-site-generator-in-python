from copy_assets import copy_assets
from generate_pages_recursive import generate_pages_recursive
import sys

def main():
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
    copy_assets(source_dir="static", destination_dir="docs")
    generate_pages_recursive("content", "template.html" , "docs", basepath)
    
if __name__ == "__main__":
    main()