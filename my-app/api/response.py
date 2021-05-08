from __main__ import app
import requests
import json
import asyncio
from flask import Flask, render_template,request
from utility_functions.utils import analyseTone
from xml.dom import minidom
import xml.etree.ElementTree as ET

# stores context for cakechat request
context=[]
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

toneWithTagMap={
    'Joy':'joy',
    'Sadness':'motivational',
    'Analytical':'instrumental',
    'Anger':'chillout',
    'Fear':'motivational',
    'Confident':'rock',
    'Tentative':'acoustic',
    'Neutral':'experimental'
}

# stores recommended songs
songs=[]
tone='Neutral'


@app.route('/response',methods=['GET','POST'])
def cakeChatResponse():
    if request.method=='POST':
        msg=request.form['chatbox']
        context.append(msg)
        if len(context)>3:
            context.pop(0)
        # print(context)
        # Todo: 
        # send it as asynchrous call it updates automatically when it completes on ui
        # make use of flask use state for it
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        tone=loop.run_until_complete(analyseTone(msg))
        loop.close()
        print('tone1',tone)
        tag=toneWithTagMap[tone]
        # print('tag',tag)
        params={
            'api_key':'3d828a6efa0582c58a2995165911bb1f',
            'limit':5,
            'method':'tag.getTopTracks',
            'tag':tag,
            'format':'json'
        }
        res = requests.post('http://ws.audioscrobbler.com/2.0', params=params)
        
        songs=[]
        for val in res.json()['tracks']['track']:
            songs.append({'name':val['name'],'url':val['url']})
            
        data={
        'context':context,
        'emotion': toneMap[tone]
        }
        res = requests.post('http://localhost:8080/cakechat_api/v1/actions/get_response', json=data)
        print('response from server:',res.json())
        msg=res.json()['response']
        return render_template('chat.html',msg=msg,tone=tone,songs=songs)
    return render_template('chat.html')

    
