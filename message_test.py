# -*- coding: utf-8 -*-
from flask import Flask, request, make_response, Response, Flask, flash, redirect, render_template, request, session, abort
import plivo

app = Flask(__name__, static_url_path='')


@app.route('/send_sms/')#, method = '[POST]')
def outbound_sms():

#	from_number= request.form.get("fromnumber")
#	to_number= request.form.get("tonumber")
#	content= request.form.get("text")

	client = plivo.RestClient()
	try:
		resp = client.messages.create(
			src='111111111', # Sender's phone number with country code
			dst='918553192289', # Receiver's phone Number with country code
			text='Hello!! You have a missed call',
		)
		# print(response)
		return str(resp)
	except plivo.exceptions.PlivoRestError as e:
		print(e)

#@app.route('/send_message/', methods=['GET'])
#def outbound_sms_template():
#	return render_template('test_sms_flask.html')

if __name__ == "__main__":
    app.run(debug=True)
