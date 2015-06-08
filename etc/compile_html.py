
__author__ = 'Shtav'
import re
import os


def inject_templates(templates_path, html):
    for filename in os.listdir(templates_path):
        #open and retrieve file content before var reassignment
        file_content = open(templates_path + filename, 'r').read()
        file_content = '<script type="text/ng-template" id="templates/' + filename + '">' + file_content + '</script>'
        #strip any possible special characters
        filename = ''.join(e for e in filename if e.isalnum())

        #create re match
        replace_begin = '<!--' + filename + ' begin-->'
        replace_end = '<!--' + filename + ' end-->'
        replace_re = replace_begin + '.*?' + replace_end

        #delete old and insert new content
        html = re.sub(replace_re, file_content, html, flags=re.DOTALL)

    return html


def inject_json_data(json_path, html):
    for filename in os.listdir(json_path):
        #open and retrieve file content before var reassignment
        file_content = open(json_path + filename, 'r').read()
        file_content = '$scope.' + os.path.splitext(filename)[0] + ' = ' + file_content

        #strip any possible special characters
        filename = ''.join(e for e in filename if e.isalnum())

        #create re match
        replace_begin = '/\*' + filename + ' begin\*/'
        replace_end = '/\*' + filename + ' end\*/'
        replace_re = replace_begin + '.*?' + replace_end

        #delete old and insert new content
        html = re.sub(replace_re, file_content, html, flags=re.DOTALL)

    return html


def inject_js(js_path, html):
    for filename in os.listdir(js_path):
        #open and retrieve file content before var reassignment
        file_content = open(js_path + filename, 'r').read()
        file_content = '<script>' + file_content + '</script>'

        #strip any possible special characters
        filename = ''.join(e for e in filename if e.isalnum())

        #create re match
        replace_begin = '<!--' + filename + ' begin-->'
        replace_end = '<!--' + filename + ' end-->'
        replace_re = replace_begin + '.*?' + replace_end

        #delete old and insert new content
        html = re.sub(replace_re, file_content, html, flags=re.DOTALL)

    return html


def inject_css(styles_path, html):
    for filename in os.listdir(styles_path):
        #open and retrieve file content before var reassignment
        file_content = open(styles_path + filename, 'r').read()
        file_content = '<style>' + file_content + '</style>'

        #strip any possible special characters
        filename = ''.join(e for e in filename if e.isalnum())

        #create re match
        replace_begin = '<!--' + filename + ' begin-->'
        replace_end = '<!--' + filename + ' end-->'
        replace_re = replace_begin + '.*?' + replace_end

        #delete old and insert new content
        html = re.sub(replace_re, file_content, html, flags=re.DOTALL)

    return html


def delete_extraneous(html):  # replace delete tag sections with ''
    #create re match
    replace_begin = '<!--delete begin-->'
    replace_end = '<!--delete end-->'
    replace_re = replace_begin + '.*?' + replace_end

    #delete old and insert new content
    html = re.sub(replace_re, '', html, flags=re.DOTALL)

    return html


def compile_html():
    compiling_html = open('input/../input/main.html', 'r').read()

    # inject_js must occur before inject_templates and inject_json_data
    compiling_html = inject_js('input/js/', compiling_html)  # JS
    compiling_html = inject_css('input/styles/', compiling_html)  # CSS
    compiling_html = inject_json_data('input/data/', compiling_html)  # JSON
    compiling_html = inject_templates('input/templates/', compiling_html)  # TEMPLATES
    compiling_html = delete_extraneous(compiling_html)  # unnecessary components

    output_html = open('output/index.html', 'w')
    output_html.write(compiling_html)
    output_html.close()






