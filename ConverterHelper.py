import base64
import json

def convertToBase64(string):
    message_bytes = string.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    return base64_message

def ObjFromJson(jsonString):
    return json.loads(jsonString)

def jsonFromObj(obj):
    return json.dumps(obj)

def createJsonData(urlList):
    obj = {'uris': urlList}
    uriJson = jsonFromObj(obj)
    return uriJson