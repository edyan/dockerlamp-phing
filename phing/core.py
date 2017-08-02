import click
import sys

from stakkr import command, docker


@click.command(help="Run Phing with the build.xml file located in the current directory", name="phing")
@click.pass_context
def phing(ctx):
    stakkr = ctx.obj['STAKKR']
    verb = stakkr.context['VERBOSE']
    debug = stakkr.context['DEBUG']
    docker.check_cts_are_running(stakkr.project_name, stakkr.config_file)

    print('Pulling image')
    command.launch_cmd_displays_output(['docker', 'pull', 'edyan/phing'], verb, debug)
    print('Done')

    tty = 't' if sys.stdin.isatty() else ''
    cmd = ['docker', 'run', '-i' + tty, '--rm', '--volume', stakkr.current_dir + ':' + stakkr.current_dir]
    cmd += ['edyan/phing', 'phing', '-f', stakkr.current_dir + '/build.xml']
    command.launch_cmd_displays_output(cmd, True, True)
