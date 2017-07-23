import click
import os
import sys

from stakkr import command


@click.command(help="Run Phing with the build.xml file located in the current directory", name="phing")
@click.pass_context
def phing(ctx):
    stakkr = ctx.obj['STAKKR']
    stakkr.check_vms_are_running()

    tty = 't' if sys.stdin.isatty() else ''
    cmd = ['docker', 'run', '-i' + tty, '--rm', '--volume', stakkr.current_dir + ':' + stakkr.current_dir]
    cmd += ['edyan/phing', 'phing', '-f', stakkr.current_dir + '/build.xml']

    command.launch_cmd_displays_output(cmd)
