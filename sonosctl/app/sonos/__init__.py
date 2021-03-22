from flask import Blueprint

sonos = Blueprint('sonos', __name__)

from . import views