import requests

'''
    this function will implement mailgun service for sending emails
	args -> 
	        email : destination email address
            message: confirmation or state text
'''
def mailgun_service(message , email):
	return requests.post(
		"https://api.mailgun.net/v3/sandbox0a959a3a816647a2afe7da07a693be9b.mailgun.org/messages",
		auth=("api", "6ae47f6e8e1af773643f091e0bfa453f-b02bcf9f-3c39e841"),
		data={"from": "music recommender massage <mailgun@sandbox0a959a3a816647a2afe7da07a693be9b.mailgun.org>",
			"to": [email],
			"subject": "music recommender massage",
			"text": message
		}
	)