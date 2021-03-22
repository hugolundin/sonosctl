from flask import Response, Blueprint
from soco.snapshot import Snapshot
import soco, time, json

DEFAULT_VOLUME = '50'
COORDINATOR = 'Living Room'

def play_sound(device, uri, title, duration=2):
    # Take a snapshot. 
    snap = Snapshot(device)
    snap.snapshot()

    # Play the given sound and wait a while.
    device.play_uri(f'http://10.0.0.52:5000{uri}', title=title)
    time.sleep(duration)
    
    # Restore the snapshot. 
    snap.restore(fade=True)

def group():
    d = soco.discovery.by_name(COORDINATOR)
    d.group.coordinator.partymode()

def ungroup(sound_url):
    for zone in list(soco.discover()):
        zone.unjoin()

    d = soco.discovery.by_name(COORDINATOR)

def set_volume(volume=DEFAULT_VOLUME):
    for d in soco.discover():
        d.volume = volume

def set_status_light(light_on):
    for d in soco.discover():
        d.status_light = light_on
    

def get_speakers():
    speakers = {}

    for s in soco.discover():
        speakers[s.player_name] = dict()
        speakers[s.player_name]['volume'] = s.volume
        speakers[s.player_name]['address'] = s.ip_address
        speakers[s.player_name]['status_light'] = s.status_light

    return speakers
