from __future__ import print_function
import pickle
import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from apiclient.http import MediaFileUpload
from pydrive.auth import GoogleAuth
from apiclient import discovery
from oauth2client.client import GoogleCredentials

# If modifying these scopes, delete the file token.pickle.





def main():
    g_login = GoogleAuth()
    g_login.LocalWebserverAuth()

    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "y/MyProject.json"
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    gauth = GoogleAuth()
    creds = gauth;
    ddd = GoogleCredentials.get_application_default();
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.



    service = discovery.build('drive','v2',credentials=ddd)

    # Call the Drive v3 API

    file_metadata = {'name': 'wiz.jpg'}
    media = MediaFileUpload('uu.jpg',
                        mimetype='image/jpg')
    file = service.files().insert(body=file_metadata,
                                    media_body=media,
                                    fields='id').execute()
    

    file1 = open("myfile.txt","w")  
  
# \n is placed to indicate EOL (End of Line) 
    file1.write("Hello \n") 
    file1.writelines(file.get('id')) 
    file1.close() #to change file access modes 
    print ('File ID: %s' % file.get('id'))
    



if __name__ == '__main__':
    main()