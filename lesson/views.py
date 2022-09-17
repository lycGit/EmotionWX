from . import lesson_bp


@lesson_bp.route('/lesson')
def get_lesson():
    return 'lesson'