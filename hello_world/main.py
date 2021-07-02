from extract_texts import *
from texts2words import *
from put_words import *


def main(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    texts = extract_texts(bucket, key)
    words = texts2words(texts)
    put_words(words, bucket)