from . import sonos
from flask import render_template, url_for, redirect, Response

@sonos.route('/group')
def group():
    try:
        pass
        # sonos.group()
    except Exception as e:
        return Response(status=500)

@sonos.route('/ungroup')
def ungroup():
    try:
        pass
        # sonos.ungroup()
    except Exception as e:
        return Response(status=500) 

@sonos.route('/speakers')
def speakers():
    return ''
    # return sonos.speakers()
