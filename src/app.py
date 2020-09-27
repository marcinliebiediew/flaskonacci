from flask import Flask


def create_app(config_filename='../application.cfg'):
    app = Flask(__name__)
    app.config.from_pyfile(config_filename)  #, silent=True)

    from src.commands import create_db, benchmark
    app.cli.add_command(create_db)
    app.cli.add_command(benchmark)

    from src.extensions import db
    db.init_app(app)

    from src.routes.fibonacci import fibonacci_bp
    from src.routes.health import health_bp
    app.register_blueprint(fibonacci_bp)
    app.register_blueprint(health_bp)

    return app
