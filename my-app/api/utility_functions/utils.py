from ibm_watson import ToneAnalyzerV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


def analyseTone(context):
    authenticator = IAMAuthenticator('1HTFBWv249zN_OBxAcoGzOS88rZVNrBaCeBxDGYXnrNP')
    tone_analyzer = ToneAnalyzerV3(
        version='2017-09-21',
        authenticator=authenticator
    )

    tone_analyzer.set_service_url('https://api.eu-gb.tone-analyzer.watson.cloud.ibm.com/instances/805758d1-a8d0-4805-8109-8024f7eee399')

    text = context
    # print(text)
    tone_analysis = tone_analyzer.tone(
        {'text': text},
        content_type='application/json'
    ).get_result()
    # print(json.dumps(tone_analysis, indent=2))
    tone='Neutral'
    tone_analysis=tone_analysis['document_tone']['tones']
    # print(toneAnalysis)
    if len(tone_analysis)>0:
        tone=tone_analysis[0]['tone_name']
    return tone

