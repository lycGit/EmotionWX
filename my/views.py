from . import my_bp
from flask import request
from flask import redirect



# 填写激活码
@my_bp.route('/activecode', methods=['POST'])
def post_activeCode():
    code = request.args.get('code')
    return code


# 投诉建议
@my_bp.route('/suggestion', methods=['POST'])
def post_suggestion():
    contact = request.args.get('contact')
    content = request.args.get('content')
    return contact


@my_bp.route('/version', methods=['POST'])
def post_version():
    return '1.0.0'


# @my_bp.route('/phoneNum/<mobile:phoneNum>')
# def get_phoneNum(phoneNum):
#     return 'phone num is: '.format(phoneNum)


# http://127.0.0.1:5000/my/upload
@my_bp.route('/upload', methods=['POST'])
def post_upload():
    f = request.files['pic']
    with open('../my/images/image.png', 'wb') as new_file:
        new_file.write(f.read())
    return 'success'


# 用户协议
@my_bp.route('/redirect')
def get_agreement():
    return redirect('http://www.baidu.com')


