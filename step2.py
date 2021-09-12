import boto3

def lambda_handler(event, context):
    
    phrase = event["phrase"]
    sentiment = event["sentiment"]
    translate = boto3.client("translate")
    result = translate.translate_text(Text=phrase, 
        SourceLanguageCode='en',
        TargetLanguageCode='es')
    print(result)   #log this outcome to CloudWatch
    payload = {"phrase":phrase, "sentiment": sentiment, 
        "translated_phrase":result['TranslatedText']
    }
    return payload