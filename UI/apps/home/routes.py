# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
import subprocess
from apps.home import blueprint
from flask import render_template, request, send_file, jsonify
from jinja2 import TemplateNotFound
from apps.modules import file_upload, shell, tools_parser


@blueprint.route('/', methods=['GET', 'POST'])
def route_default():
    names, count, local_str = tools_parser.names_and_count()

    not_local = []
    for name in names:
        if name not in local_str:
            not_local.append(name)
        if request.method == 'POST':
            try:
                download_image = request.form[name]
            except:
                pass
        else:
            download_image = ''
    p = subprocess.Popen(download_image, shell=True, encoding='utf-8', universal_newlines=True)
    return render_template('home/index.html', segment='index', count=count, not_local=not_local, names=names)


@blueprint.route('/shell', methods=['GET', 'POST'])
def shell_page():
    if request.method == 'POST':
        command = request.form['command']
    else:
        command = ''
    out, pwd, err = shell.execute_shell(command)
    return render_template('home/shell.html', output=out, pwd=pwd, err=err, command=command, segment='shell')


@blueprint.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        upload_path = request.form['upload_path']
        download_path = request.form['download_path']
        try:
            file_upload.upload(request, upload_path)
        except:
            pass
        try:
            return send_file(download_path, as_attachment=True)
        except:
            pass
    return render_template('home/upload.html', segment='upload')


@blueprint.route('/<template>')
def route_template(template):
    try:
        if not template.endswith('.html'):
            template += '.html'

        # Detect the current page
        segment = get_segment(request)

        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template("home/" + template, segment=segment)

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except:
        return render_template('home/page-500.html'), 500


# Helper - Extract current page name from request
def get_segment(request):
    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None
