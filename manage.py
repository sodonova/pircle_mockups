def deploy():
    """Run deployment tasks."""
    from app import create_app, db, SUser
    from flask_migrate import upgrade, migrate, init, stamp

    app = create_app()
    app.app_context().push()
    db.create_all()

    # migrate database to latest revision
    init()
    stamp()
    migrate()
    upgrade()

def update_tables():
    from app import create_app, db, SUser
    from flask import Flask
    from flask_migrate import upgrade, migrate, init, stamp

    app = Flask(__name__)

    app.secret_key = 'secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db" # makes it a file called databse.db
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    db.init_app(app)
    app.app_context().push()
    db.create_all()


# deploy()
