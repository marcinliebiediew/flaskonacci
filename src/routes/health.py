from flask import Blueprint, abort, jsonify

from src.extensions import db

health_bp = Blueprint('health', __name__)


@health_bp.route('/health')
def health():
    try:
        db.engine.execute("SELECT 1 FROM logs")
        return ('OK', 200)
    except:
        return ('ERR', 500)
