def nlp_sentiment():
# Imports the Google Cloud client library

	import argparse
	import os
	from google.cloud import language
	from google.cloud.language import enums
	from google.cloud.language import types
	from google.oauth2 import service_account

	creds = service_account.Credentials.from_service_account_file() # insert .json file path here including the .json file's name with double air quotes ("")
	client = language.LanguageServiceClient(
	    credentials=creds,
	 )

	# The text to analyze
	text = u'The Cloud Natural Language supports a variety of languages. These languages are specified within a request using the optional language parameter.'
	
	document = types.Document(
		content=text,
		type=enums.Document.Type.PLAIN_TEXT)

		# Detects the sentiment of the text
	sentiment = client.analyze_sentiment(document=document).document_sentiment

	print('Text: {}'.format(text))
	print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))

	
	sentences = text.split('.')

	score = [0 for i in range(len(sentences))]
	magnitude = [0 for i in range(len(sentences))]

	for i in range(0,len(sentences)):

		document = types.Document(
		    content=sentences[i],
		    type=enums.Document.Type.PLAIN_TEXT)

		# Detects the sentiment of the text
		sentiment = client.analyze_sentiment(document=document).document_sentiment

		score[i] = sentiment.score
		magnitude[i] = sentiment.magnitude


	largest_impact = max(score)

	selector = score.index(largest_impact)

	print('Text: {}'.format(sentences[selector]))
	print('is the sentence with largest sentiment score individually with a score of {}'.format(largest_impact))

	return 

nlp_sentiment()