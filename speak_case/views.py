from . import speak_case_bp


# 大家都在搜
@speak_case_bp.route('/talkcase')
def get_talkcase():
    return 'talkcase'