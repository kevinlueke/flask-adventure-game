from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
bp = Blueprint('game', __name__)

from flask_adventure_game import errors

#Introduction
@bp.route('/index')
def index():
    return render_template('base.html')

#@bp.route('/help', methods=('GET', 'POST'))
    
def dir(valid_actions, action, current_scene):
    
    # Allows help to be available whenever a player needs to know controls
    if action == 'help':
        #raise HelpError
        message = """
            ---------------------------------------
            The directions to move are as follows:
            w will move forward
            a will move left
            s will move back
            d will move right
            ---------------------------------------
            When presented with a choice to do something:
            yes or y will agree to something
            no or n will disagree to something
            ---------------------------------------
            Your current mp is {player_stats.player.stats['morality_points']})"""
        return message
    elif action in valid_actions:
        return action

    else:
        #raise ValueError
        message =  "Not a valid action right now. 'help' will list all possible actions"
        return message
        #flash("Not a valid action right now")

@bp.route('/Aghrial', methods=('GET', 'POST'))
# Beginning of game that a player will start at
def aghrial():
        current_scene = """
            Welcome to The Trials of Aghrial
            Years ago, Aghrial stopped a murder from happening
            Only days after the man that he saved killed hundreds
            After that tragic day Aghrial disappeared, leaving no trace of himself behind
        
            This game will allow you to choose between good and bad
            Sometimes chosing the wrong thing will lead to
            greater morality points (mp) and vice versa
            You may choose to achieve a score of 100 mp or -100 mp
            If you only choose choices of one side then the game will be imposiible to win
            ---------------------------------------
            The directions to move are as follows:
            w will move forward
            a will move left
            s will move back
            d will move right
            ---------------------------------------
            When presented with a choice to do something:
            yes or y will agree to something
            no or n will disagree to something
            ---------------------------------------
            Typing mp will give you your current score
        
            If at any point you are unsure of all available actions just type help

        
            There's a magical door right in front of you
            """
        if request.method=='POST':
            action = request.form['action']
            #try: 
            current_scene = dir(('w',), action, current_scene)
                #variable for the tuple
            #except HelpError:
                #they type help
            #except ValueError:
                #they donti flsh this one

            if current_scene == 'w':
                current_scene = "The door you came out of slammed shut behind you and disappeared"
                return render_template('index.html', scene=current_scene)
        return render_template('index.html', scene=current_scene)

