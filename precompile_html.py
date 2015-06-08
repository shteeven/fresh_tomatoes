
__author__ = 'Shtav'
import re
import os


def inject_templates(templates_path, html):
    for filename in os.listdir(templates_path):
        #open and retrieve file content before var reassignment
        with open(templates_path + filename, 'r') as f:
            file_content = f.read()
        file_content = '<script type="text/ng-template" id="templates/' + filename + '">' + file_content + '</script>'
        #strip any possible special characters
        filename = ''.join(e for e in filename if e.isalnum())

        # create re match
        replace_begin = '<!--' + filename + ' begin-->'
        replace_end = '<!--' + filename + ' end-->'
        replace_re = replace_begin + '.*?' + replace_end

        # delete old and insert new content
        html = re.sub(replace_re, file_content, html, flags=re.DOTALL)

    return html


def inject_js(js_path, html):
    for filename in os.listdir(js_path):
        #open and retrieve file content before var reassignment
        with open(js_path + filename, 'r') as f:
            file_content = f.read()
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
        with open(styles_path + filename, 'r') as f:
            file_content = f.read()
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
    #create re match for HTML
    replace_begin = '<!--delete begin-->'
    replace_end = '<!--delete end-->'
    replace_re = replace_begin + '.*?' + replace_end

    #delete content in HTML
    html = re.sub(replace_re, '', html, flags=re.DOTALL)

    #create re match for JS
    replace_begin = '\/\*delete begin\*\/'
    replace_end = '\/\*delete end\*\/'
    replace_re = replace_begin + '.*?' + replace_end

    #delete content in JS
    html = re.sub(replace_re, '', html, flags=re.DOTALL)

    return html


def insert_tile_format_tag(html):
    # LAST INSERT: This uses and old formatter to insert the tiles because
    # the python format indicator '{}' gets mixed with the braces in the css and
    # js elsewhere in the file

    #create re match
    replace_begin = '<!--movietile begin-->'
    replace_end = '<!--movietile end-->'
    replace_re = replace_begin + '.*?' + replace_end

    #delete old and insert new content
    html = re.sub(replace_re, '%s', html, flags=re.DOTALL)

    return html



def main():  # compiles files to a single html file
    with open('development/main.html', 'r') as f:
        compiling_html = f.read()

    # inject_js must occur before inject_templates and inject_json_data
    compiling_html = inject_js('development/js/', compiling_html)  # JS
    compiling_html = inject_css('development/styles/', compiling_html)  # CSS
    compiling_html = inject_templates('development/templates/', compiling_html)  # TEMPLATES
    compiling_html = delete_extraneous(compiling_html)  # unnecessary components

    with open('precompiled/precompiled.html', 'w') as f:
        f.write(compiling_html)


main()
