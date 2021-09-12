import json
import boto3

def lambda_handler(event, context):
    
    if "phrase" in event:
        phrase = event["phrase"]
        comprehend = boto3.client("comprehend")
        result = comprehend.detect_sentiment(Text=phrase, LanguageCode='en')
        print(result)
        return result["Sentiment"]
    return None
    
   