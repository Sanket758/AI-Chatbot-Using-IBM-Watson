from ibm_watson import AssistantV1
from ibm_watson import ApiException
import json
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import sys

authenticator = IAMAuthenticator('API Key')
assistant = AssistantV1(
    version='2020-03-04',
    authenticator=authenticator
)

assistant.set_service_url('Your APi URL')
assistant.set_default_headers({'x-watson-learning-opt-out': "true"})


while True:
	try:
		# Invoke a Watson Assistant method
		#response=assistant.list_workspaces().get_result()
		#response=assistant.list_intents(workspace_id='Workspace ID').get_result()
		#print(json.dumps(response, indent=2))
		query = input("Enter Message:")
		response = assistant.message(workspace_id='WorkSpace ID',input={'text': query,'options': {'return_context':True}}).get_result()
		if query in ['quit','bye','goodbye','exit']:
			sys.exit()
		#print(json.dumps(response, indent=2))
		print(response['output']['generic'][0]['text'])
		
	except ApiException as ex:
		print ("Method failed with status code " + str(ex.code) + ": " + ex.message)
    
#64628a18-ff86-40e9-b650-2ee816fd9986	
