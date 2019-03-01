from flask_script import Manager
from flask_alchemydumps import AlchemyDumps, AlchemyDumpsCommand
from flask_migrate import Migrate, MigrateCommand

from app import app, db

manager = Manager(app)

alchemydumps = AlchemyDumps(app, db)
manager.add_command('data', AlchemyDumpsCommand)

migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()

