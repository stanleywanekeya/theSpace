"""This module creates custom error settings"""
from flask import render_template
from app import app, db
@app.errorhandler(404)
def page_not_found(error):
    """Returns a page not found error"""
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    """Returns an error page if theres an internal error"""
    db.session.rollback()
    return render_template('500.html'), 500
