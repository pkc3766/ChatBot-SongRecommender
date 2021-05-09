from flask import Blueprint,request
tone = Blueprint('tone', __name__)
from utility_functions.utils import analyseTone


@tone.route('/api/tone',methods=['POST'])
def getTone():
    msg=request.get_json()
    msg=msg['chat']
    print('In tone analyser message is ',msg)
    tone=analyseTone(msg)
    print('In tone analyser tone analysed is ',tone)
    return {
        'tone':tone
    }

