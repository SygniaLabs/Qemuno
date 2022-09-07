import subprocess
import os
from apps.modules import tools_parser


def execute_shell(command):
    check_newpwd(command)
    command = check_docker(command)
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8',
                         universal_newlines=True)
    out = '<br>'.join(p.stdout.readlines())
    err = '<br>'.join(p.stderr.readlines())
    return out, os.getcwd(), err


def check_newpwd(command):
    if command[0:3] == "cd ":
        os.chdir(command[3:])


def check_docker(command):
    names, count, local_str = tools_parser.names_and_count()
    for i in range(len(names)):
        if command.startswith(names[i]):
            command = "docker run --rm -v /qemuno:/qemuno nm10pt/" + command
    return command