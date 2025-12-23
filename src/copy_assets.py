import os 
import shutil

def copy_assets(source_dir="static", destination_dir="public"):
    # convert the paths into absolute paths to be able to use them
    abs_source = os.path.abspath(source_dir)
    abs_destination = os.path.abspath(destination_dir)

    # you cannot copy form un-existing source
    if not os.path.exists(abs_source):
        raise Exception("Source path does not exists")

    # remove destination_dir completely
    shutil.rmtree(abs_destination, ignore_errors=True)
    # create it again
    os.mkdir(abs_destination)

    source_tree = os.listdir(abs_source) 

    recursively_copy(source_tree, abs_source, abs_destination)

def copy(src, dst):
     shutil.copy(src, dst)
     print(dst)

def recursively_copy(paths, abs_source, abs_destination):
    for item in paths:
        item_path = os.path.join(abs_source, item)
        dst_path = os.path.join(abs_destination, item)
         
        if os.path.isfile(item_path):
            copy(item_path, dst_path)
            continue
        else:  
            os.mkdir(dst_path)
            recursively_copy(os.listdir(item_path), item_path, dst_path)