from flask import Blueprint,request
tone = Blueprint('tone', __name__)
from utility_functions.utils import analyseTone


@tone.route('/api/tone',methods=['POST'])
def getTone():
    msg=request.get_json()
    msg=msg['chat']
    print('In tone analyser message is ')
    print(msg)
    tone=analyseTone(msg)
    print('tone analysed is')
    print(tone)
    return {
        'tone':tone
    }

