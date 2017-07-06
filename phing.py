import click
import os
import sys

from lib import command


@click.command(help="Run Phing with the build.xml file located in the current directory", name="phing")
@click.pass_context
def phing(ctx):
    # Insert the parent marina dir in path to get lib/command.py
    sys.path.insert(0,'../..')

    current_dir = os.getcwd()
    tty = 't' if sys.stdin.isatty() else ''
    cmd = ['docker', 'run', '-i' + tty, '--rm', '--volume', current_dir + ':' + current_dir]
    cmd += ['edyan/phing', 'phing', '-f', current_dir + '/build.xml']
    command.launch_cmd_displays_output(cmd)
