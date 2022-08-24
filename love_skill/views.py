from . import love_skill_bp


@love_skill_bp.route('/loveskill')
def get_love_skill():
    return 'loveskill'