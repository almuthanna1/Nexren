from flask import Flask, request, jsonify, render_template
import smtplib
from email.message import EmailMessage
import os

app = Flask(__name__)


# ----------- ROUTES -----------

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index')
def home1():
    return render_template('index.html')

@app.route('/prices')
def prices():
    return render_template('prices.html')

@app.route('/team')
def our_team():
    return render_template('team.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

# Email config
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 465
EMAIL_ADDRESS = 'amshihab99@gmail.com'          # Your sending email
EMAIL_PASSWORD = 'xrri uqrd lzyr kops'            # Use App Password for Gmail or your SMTP password
RECEIVER_EMAIL = 'amshihab99@gmail.com'         # Email where you want to receive contact messages

def send_email(name, email, message):
    msg = EmailMessage()
    msg['Subject'] = f'NEXREN - New Contact Form Message from {name}'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = RECEIVER_EMAIL
    msg.set_content(f'Name: {name}\nEmail: {email}\nMessage:\n{message}')

    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

@app.route('/contact', methods=['POST'])
def contact():
    data = request.form
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')

    if not (name and email and message):
        return jsonify({'error': 'Missing data'}), 400

    # Save to file
    with open('contacts.txt', 'a') as f:
        f.write(f"{name} | {email} | {message}\n")

    try:
        # Send email notification
        send_email(name, email, message)
    except Exception as e:
        print(f"Failed to send email: {e}")
        # You can choose whether to return error or just proceed
        return jsonify({'error': 'Failed to send email'}), 500

    return jsonify({'message': 'Success'})

if __name__ == '__main__':
    # For local testing only. Use a proper WSGI server for production.
    app.run(debug=True)
