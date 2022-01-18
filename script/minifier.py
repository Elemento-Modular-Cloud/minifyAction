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


def do_js(path, overwrite=True):
    from css_html_js_minify import process_single_js_file
    process_single_js_file(path, overwrite=overwrite)


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
    print("Path not found: "+path)
