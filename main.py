import os
import base64
import mimetypes
from email.message import EmailMessage
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly', 'https://www.googleapis.com/auth/gmail.send']

def authenticate_gmail(): 
 creds = None 
 if os.path.exists('token.json'): 
  creds = Credentials.from_authorized_user_file('token.json', SCOPES)
 if not creds or not creds.valid: 
  if creds and creds.expired and creds.refresh_token: 
   creds.refresh(Request())
  else: 
   flow = InstalledAppFlow.from_client_secrets_file('credential.json', SCOPES)
   creds = flow.run_local_server(port=0) 
  with open('token.json', 'w') as token: 
   token.write(creds.to_json())
 return creds 


def get_email(service, user_id, msg_id): 
 try: 
  message = service.users().messages().get(userId=user_id, id=msg_id).execute() 
  print('Message Snippet: %s' % msg_str)
  return message 
 except Exception as error: 
  print(f'An error ocurred {error}')

 def list_mail(service, user_id, query=' '): 
    response = service.users().messages().list(userId=user_id, q=query).execute()
    messages = []
    if 'messages' in response:
     messages.extend(response['messages'])

    while 'nextPageToken' in response:
     page_token = response['nextPageToken']
     response = service.users().messages().list(userId=user_id, q=query, pageToken=page_token).execute()
     messages.extend(response['messages'])
     return messages
 

 def main():
    creds = authenticate_gmail()
    service = build('gmail', 'v1', credentials=creds)
    
    messages = list_messages(service, 'me', query='')

    for msg in messages[:10]:
        get_email(service, 'me', msg['id'])


if __name__ == '__main__':
    main()




