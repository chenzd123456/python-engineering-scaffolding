#!/bin/python3

import os
import shutil

import click
import PyInstaller.__main__


def delete_path(path):
    if(os.path.exists(path)):
        print("found {}, delete...".format(path))
        if(os.path.isdir):
            shutil.rmtree(path)
        else:
            os.remove(path)


@click.group()
def cli():
    pass


@cli.command()
def run(*args, **kwargs):
    os.system('python ' + os.path.join('src', 'main.py'))


@cli.command()
def build():
    print("build...")
    PyInstaller.__main__.run([
        os.path.join('src', 'main.py'),
        '--onefile',
        '--window'
    ])


@cli.command()
def clean():
    print("clean...")
    delete_path("./build")
    delete_path("./dist")


if __name__ == "__main__":
    cli()
