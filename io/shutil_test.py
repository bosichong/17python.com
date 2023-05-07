import shutil


src_path = "/Users/J.sky/mybaby/suiyanblog/assets"
dst_path = "/Users/J.sky/mybaby/gittest/assets"


shutil.copytree(src_path,dst_path,dirs_exist_ok=True)
# shutil.copytree(src_path,dst_path,)