#!/usr/bin/env python3

import sys
import os


def single_file(path):
    print("doning on --> ", path)
    import os
    file_name, file_ext = os.path.splitext(path)
    if file_ext == '.js':
        do_js(path)
    if file_ext == '.scss':
        do_css(path)
    if file_ext == '.css':
        do_css(path)
    if file_ext == '.html' or file_ext == '.htm':
        do_html(path)


def all_files():
    print('yep')


exclusions = ["hacks.js"]


def do_js(path, overwrite=True):
    if os.path.basename(path) not in exclusions:
        from css_html_js_minify import process_single_js_file
        process_single_js_file(path, overwrite=overwrite)
    else:
        print("Legacy mode")
        file_name, file_ext = os.path.splitext(path)
        if not overwrite:
            with open(path, "r", encoding="utf-8") as js_file:
                with open(file_name+".min.js", "w", encoding="utf-8") as output:
                    orig = js_file.readlines()
                    orig = [line.rstrip().strip() for line in orig]
                    orig = [line for line in orig if not line.startswith('//')]
                    minified = ''.join(orig)
                    output.write(minified)
        else:
            with open(path, "r+", encoding="utf-8") as js_file:
                orig = js_file.readlines()
                orig = [line.rstrip().strip() for line in orig]
                orig = [line for line in orig if not line.startswith('//')]
                minified = ''.join(orig)
                js_file.seek(0)
                js_file.write(minified)
                js_file.truncate()





def do_css(path, overwrite=True):
    file_name, file_ext = os.path.splitext(path)
    from css_html_js_minify import process_single_css_file
    if not overwrite:
        process_single_css_file(path, output_path=(file_name + ".min.scss"))
    else:
        process_single_css_file(path,
                                output_path=(file_name + ".scss"),
                                overwrite=True)


def do_scss(path, overwrite=True):
    from css_html_js_minify import process_single_css_file
    process_single_css_file(path, overwrite=overwrite)


def do_html(path, overwrite=True):
    from css_html_js_minify import process_single_html_file
    process_single_html_file(path, overwrite=overwrite)


try:
    path = sys.argv[1]
    single_file(path)
except Exception as e:
    print(e)
    print(sys.argv)
    print("Path not found: "+path)
