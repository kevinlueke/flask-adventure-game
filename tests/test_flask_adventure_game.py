import flask_adventure_game

def test_import():
    assert flask_adventure_game

def test_config():
    assert not flask_adventure_game.create_app().testing
    assert flask_adventure_game.create_app({'TESTING': True}).testing
