from six.moves import urllib
import json
import subprocess


def names_and_count():

    # get request
    page = urllib.request.urlopen('https://hub.docker.com/v2/repositories/sygnialabs').read()
    page = page.decode()

    # str to dict
    res = json.loads(page)

    # get local docker images
    local_imgs = local()

    return get_names(res), count(res), local_imgs  # list, int


def get_names(res):
    images = res['results']
    tools = []
    for i in images:
        if i["name"] != "qemuno-ui":
            tools.append(i["name"])

    # create alias
    # for i in tools:
    #     command_docker = 'docker run %s' % i
    #     command_alias = 'alias "%s"=\'%s\'' % (i, command_docker)
    #     command_load = ". ~/.ash_aliases"
    #     all_together = 'echo "%s" >> ~/.ash_aliases ; %s' % (command_alias,command_load)
    #     p1 = subprocess.Popen(all_together, shell=True, stdout=subprocess.PIPE, encoding='utf-8',
    #                           universal_newlines=True)
    return tools


def count(res):
    count_images = res['count'] - 1
    return count_images


def local():
    command = "docker images"
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, encoding='utf-8', universal_newlines=True)
    out = '<br>'.join(p.stdout.readlines())
    return out
