
import json
import os

import boto3
from dotenv import load_dotenv

from python_files.attachment_processor.attachment_helper import \
    processAttachment

load_dotenv()

botName = os.getenv('BOT_NAME')
botAlias = os.getenv('BOT_ALIAS')
intentName = os.getenv('INTENT_NAME')


def generateResponse( message ):
    
    #json format of message to be followed 
    ''' {
            {
            "sender":{
                "id": "4"
                "name":"Pranjal"
            }
            "message":{
                "text":"Hi"
                "attachment":{
                    type: "image/file"
                    name: // for downlaoding    
                }
            }
        }
    } 
    '''
    sender_id = message['sender']['id']
    response = None
    if message['message'].get('attachment'):
        fileName = message['message']['attachment']['name']
        fileType = message['message']['attachment']['type']
        data = processAttachment( fileName , fileType  )
        response = sendSlotValuesToLex( data , sender_id  ) 
    
    elif message['message'].get('text'):
        response = sendTextToLex( message['message']['text'],sender_id )
    
    messageArray = [] 
    
    if response is None : 
        messageArray.append('Some error occured')
        return messageArray
    
    if response['message'][0] == '{':
        response_json = json.loads(response['message'])
        for message in response_json['messages']:
            messageArray.append( message['value'] )
    else :
        messageArray.append( response['message'] )    
    
    #print( messageArray )
    response = { "messages": messageArray }
    return  json.dumps(response)    
    #response syntax   
    '''      {
                'intentName': 'string',
                'slots': {
                    'string': 'string'
                },
                'sessionAttributes': {
                    'string': 'string'
                },
                'message': 'string',
                'sentimentResponse': {
                    'sentimentLabel': 'string',
                    'sentimentScore': 'string'
                },
                'messageFormat': 'PlainText'|'CustomPayload'|'SSML'|'Composite',
                'dialogState': 'ElicitIntent'|'ConfirmIntent'|'ElicitSlot'|'Fulfilled'|'ReadyForFulfillment'|'Failed',
                'slotToElicit': 'string',
                'responseCard': {
                    'version': 'string',
                    'contentType': 'application/vnd.amazonaws.card.generic',
                    'genericAttachments': [
                        {
                            'title': 'string',
                            'subTitle': 'string',
                            'attachmentLinkUrl': 'string',
                            'imageUrl': 'string',
                            'buttons': [
                                {
                                    'text': 'string',
                                    'value': 'string'
                                },
                            ]
                        },
                    ]
                },
                'sessionId': 'string'
            }
    '''   
        
def sendTextToLex( message , sender_id  ):
    
    #request syntax
    '''  {
            # response = client.post_text(
            #     botName='string',
            #     botAlias='string',
            #     userId='string',
            #     sessionAttributes={
            #         'string': 'string'
            #     },
            #     requestAttributes={
            #         'string': 'string'
            #     },
            #     inputText='string'
            # )
        }
    '''
    
    client = boto3.client('lex-runtime')
    response = client.post_text(
        botName= botName ,
        botAlias= botAlias,
        userId=sender_id,
        sessionAttributes={},
        requestAttributes={},
        inputText=message
    )
    return response

def sendSlotValuesToLex( data , sender_id ):
    
    slotValue = { 'receipt':'success' }
    #if data.get('unit'): slotValue['unit']=data['unit']
    if data.get('amount'): slotValue['amount']=data['amount']
    if data.get('category'): slotValue['category'] = data['category']
    if data.get('date') : slotValue['date'] = data['date']
    
    client = boto3.client('lex-runtime')
    
    get_session_response = { 'recentIntentSummaryView':[] }
    try:
        get_session_response = client.get_session(
        botName= botName ,
        botAlias= botAlias ,
        userId= sender_id 
        )
        temp = []
        for recentIntent in get_session_response['recentIntentSummaryView']:
            if recentIntent['intentName']!=intentName: 
                temp.append(recentIntent)
            else:
                for key,value in recentIntent['slots'].items():
                    if value is not None:  slotValue[key] = value
                
        get_session_response['recentIntentSummaryView'] = temp     
    except Exception as e:
        print(e)
         
    client = boto3.client('lex-runtime')
    response = client.put_session(
        botName=botName,
        botAlias=botAlias,
        userId= sender_id ,
        sessionAttributes={},
        dialogAction={
            'type': 'Delegate',
            'intentName': intentName ,
            'slots': slotValue
        },
        recentIntentSummaryView= get_session_response.get('recentIntentSummaryView') 
    ) 
    print(response)
    return response
    
     
if __name__ == "__main__":
    #sendSlotValuesToLex({'category':'Food'},'1234567')   
    message =   {
        'sender': {
            'id': '1234'
        }, 
        'message': {
          'text': 'Hi', 
          'attachment': 
            {'name': 'file.pdf', 'type': 'file'}
        }
    }
    generateResponse( message )
    # {
    #         'sender':{
    #             'id': '098',
    #             'name': 'Pranjal'
    #         },
    #         'message':{
    #             'text':"Spent rs 100"
    #             # 'attachment':{
    #             #     'type': "file",
    #             #     'url': 'http://127.0.0.1:5500/bills/bill2.pdf'   
    #             # }
    #         }
    #     }