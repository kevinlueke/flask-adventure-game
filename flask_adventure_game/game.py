from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
bp = Blueprint('game', __name__, url_prefix='/game')

#Introduction
@bp.route('/intro')
def intro():
    return render_template('intro.html', area=intro)
