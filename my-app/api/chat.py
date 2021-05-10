from flask import Blueprint,request
chat = Blueprint('chat', __name__)
import requests

# map tone from ibm tone analyser with tone required by cake chat
toneMap={
    'Joy':'joy',
    'Sadness':'sadness',
    'Analytical':'neutral',
    'Anger':'anger',
    'Fear':'fear',
    'Confident':'neutral',
    'Tentative':'neutral',
    'Neutral':'neutral'
}

# stores context for cakechat request
context=[]
tone='Neutral'

# returns a response from cakechat server(chatbot)
@chat.route('/api/chat', methods=['POST'])
def getChatResponse():
    data=request.get_json()
    msg=data['chat']
    tone=data['tone']
    print('Inside cakechat message is ',msg)
    print('Inside cakechat tone is ',tone)
    # if len(msg)>0:
    #     context.append(msg)
    # if len(context)>3:
    #     context.pop(0)
    context=[msg]
    print(context)
    data={
        'context':context,
        'emotion': toneMap[tone]
        }
    res = requests.post('http://localhost:8080/cakechat_api/v1/actions/get_response', json=data)
    # print('response from server:',res.json())
    msg=res.json()
    return msg

