
def lambda_handler(event, context):
    
    phrase = event["phrase"]
    sentiment = event["sentiment"]
    translated_phrase = event["translated_phrase"]
    if sentiment == "POSITIVE":
        result = {
            "summary": f"Thank you for the {sentiment} comments. Your Spanish Translation is: {translated_phrase}"
        }
    else:
        result = {"summary":"Improve the quality of your comments to receive a translation"}
 
    return result