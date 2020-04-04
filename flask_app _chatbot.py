from flask import Flask, render_template, request
from ibm_watson import AssistantV1
from ibm_watson import ApiException
import json
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import sys

app = Flask(__name__)

authenticator = IAMAuthenticator('API Key')
assistant = AssistantV1(
    version='2020-03-04',
    authenticator=authenticator
)

assistant.set_service_url('URL')
assistant.set_default_headers({'x-watson-learning-opt-out': "true"})

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    response = assistant.message(workspace_id='Workspace ID',input={'text': userText,'options': {'return_context':True}	}).get_result()
    response = response['output']['generic'][0]['text']
    return str(response)

if __name__ == "__main__":
    app.run()

