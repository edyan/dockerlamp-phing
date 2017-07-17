import click
import os
import sys

from marina import command


@click.command(help="Run Phing with the build.xml file located in the current directory", name="phing")
@click.pass_context
def phing(ctx):
    marina = ctx.obj['MARINA']
    marina.check_vms_are_running()

    tty = 't' if sys.stdin.isatty() else ''
    cmd = ['docker', 'run', '-i' + tty, '--rm', '--volume', marina.current_dir + ':' + marina.current_dir]
    cmd += ['edyan/phing', 'phing', '-f', marina.current_dir + '/build.xml']

    command.launch_cmd_displays_output(cmd)
