from sys import argv, exit
from os.path import abspath, dirname, join
try:
    from yaml import load, dump
except:
    from sys import exit, stderr
    stderr.write('[E] install pyyaml\n')
    exit(2)

try:
    from deepmerge import Merger
except:
    from sys import exit, stderr
    stderr.write('[E] install deepmerge\n')
    exit(2)

if not len(argv) > 1:
    print('pass user config as argv')
    exit(1)

searx_dir = abspath(dirname("./../searx/searx"))

def merge_settings_file(user_settings_config):
    settings_merger = Merger(
        [
            (list, ["append"]),
            (dict, ["merge"])
        ],
        # applied to all other types:
        ["override"],
        # in the case where the types conflict:
        ["override"]
    )

    with open(join(searx_dir, 'settings.yml')) as settings_yaml:
        searx_settings = load(settings_yaml)

    user_settings = load(user_settings_config)

    settings_merger.merge(searx_settings, user_settings)

    print dump(searx_settings, default_flow_style=False)


merge_settings_file(argv[1])
