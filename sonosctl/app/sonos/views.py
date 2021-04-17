from . import sonos
from . import system
from flask import render_template, Response, abort, url_for

@sonos.route('/group')
def group():
    try:
        system.group()
    except Exception as e:
        print(e)
        abort(500)

    return Response(status=200)

@sonos.route('/ungroup')
def ungroup():
    try:
        system.ungroup()
    except Exception as e:
        print(e)
        abort(500)

    return Response(status=200)

@sonos.route('/speakers')
def speakers():
    return system.get_speakers()

@sonos.route('/speakers/volume/<int:percentage>')
def volume(percentage):
    if percentage < 0 or percentage > 100:
        abort(500)

    system.set_volume(percentage)
    return Response(status=200)

@sonos.route('/speakers/status_light/on')
def status_light_on():
    system.set_status_light(light_on=True)
    return Response(status=200)

@sonos.route('/speakers/status_light/off')
def status_light_off():
    system.set_status_light(light_on=False)
    return Response(status=200)
