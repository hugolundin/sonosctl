from flask import Response, Blueprint
from soco.snapshot import Snapshot
import soco, time, json

COORDINATOR = 'Living Room'
bp = Blueprint('sonos', __name__, template_folder='templates')

def play_sound(device, uri, title, duration=2):

    # Take a snapshot. 
    snap = Snapshot(device)
    snap.snapshot()

    # Play the given sound and wait a while.
    device.play_uri(uri, title=title)
    time.sleep(duration)
    
    # Restore the snapshot. 
    snap.restore(fade=True)

@bp.route('/group')
def group():
    d = soco.discovery.by_name(COORDINATOR)
    d.group.coordinator.partymode()
    return Response(status=200)

@bp.route('/ungroup')
def ungroup():
    for zone in list(soco.discover()):
        zone.unjoin()

    return Response(status=200)

@bp.route('/speakers')
def speakers():
    return {d.player_name : d.ip_address for d in soco.discover()}
