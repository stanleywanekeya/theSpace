"""This is the main flask module"""
from app import app, db
import sqlalchemy as sa
import sqlalchemy as so
from app.models import User


@app.shell_context_processor
def make_shell_context():
    """This function is used to update instances to shell"""
    return {'sa': sa, 'so': so, 'db': db, 'User': User}
