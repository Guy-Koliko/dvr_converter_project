
import os
import subprocess
ex_1 = '.dat'
ex_2 = '.mp4'

def convert_tool(src_dir,dst_dir):
    for root, dirs, files in os.walk(src_dir):
        for f in files:
            prefix, suffix = os.path.splitext(f)
            if ex_1 == suffix:
                abspath_in = root + '/' + f
                dir_out = root.replace(src_dir,dst_dir)
                if not os.path.exists(dir_out):
                    os.makedirs(dir_out)
                abspath_out = dir_out + '/' + prefix + ex_2
                subprocess.call(['ffmpeg','-i',abspath_in,'-y',abspath_out])