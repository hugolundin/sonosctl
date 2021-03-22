from . import sonos
from . import system

from flask import render_template, Response, abort

@sonos.route('/group')
def group():
    try:
        system.group()
    except Exception as e:
        abort(500)

@sonos.route('/ungroup')
def ungroup():
    try:
        system.ungroup()
    except Exception as e:
        abort(500)

@sonos.route('/speakers')
def speakers():
    return system.get_speakers()
