"""
Phing plugin for stakkr"""

import sys
import click
from stakkr import command, docker_actions


@click.command(help="""Run Phing with the build.xml file located in the
current directory""", name="phing")
@click.pass_context
def phing(ctx):
    """See command help"""

    stakkr = ctx.obj['STAKKR']
    verb = stakkr.context['VERBOSE']
    debug = stakkr.context['DEBUG']
    docker_actions.check_cts_are_running(stakkr.project_name)

    print('Pulling image')
    command.launch_cmd_displays_output(['docker', 'pull', 'edyan/phing'], verb, debug)
    print('Done')

    tty = 't' if sys.stdin.isatty() else ''
    cmd = ['docker', 'run', '-i' + tty, '--rm']
    cmd += ['--volume', stakkr.cwd_abs + ':' + stakkr.cwd_abs]
    cmd += ['edyan/phing', 'phing', '-f', stakkr.cwd_abs + '/build.xml']
    command.launch_cmd_displays_output(cmd, True, True)
