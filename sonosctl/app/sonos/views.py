from . import sonos
from . import system

from flask import render_template, Response, abort, url_for

@sonos.route('/group')
def group():
    try:
        system.group(url_for('static', filename='confirm.mp3'))
    except Exception as e:
        print(e)
        abort(500)

    return Response(status=200)

@sonos.route('/ungroup')
def ungroup():
    try:
        system.ungroup(url_for('static', filename='confirm.mp3'))
    except Exception as e:
        print(e)
        abort(500)

    return Response(status=200)

@sonos.route('/speakers')
def speakers():
    return system.get_speakers()
