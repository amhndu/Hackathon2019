## Description
This is the repo for [Redactio.ml](http://redactio.ml), a solution developed during the IBM 24-hr Hackathon organised at IIITDM Jabalpur. It allows you to anonymize your data by automatically detecting fields that could be personal information and bringing them to your notice before redaction. The fields identified include: Name, Gender, govt. IDs like Aadhaar, PAN, and also bank details like Credit/Debit card numbers and Bank account number. Companies spend a lot in maintaining compliance with policies like GDPR, since experts would have to manually delete personal information from chats and other interactions with their customers for both internal and external purposes. Our solution would be a boon to them. It would also be useful for Complaint Systems online forums, automating the process done by moderators. 

Our focus was on providing a **minimalist UI** for the input area, where the user had the power to **individually** select and redact different detected fields. This input provision could replace the text input of various applications like grievances platforms, company chat systems, forums etc. Since the fields are highlighted in grey, it provides the user with a visual way to know the proportion of personal information in his otherwise inconspicuous post.

We have combined IBM Natural Language Understanding (NLU) with a custom trained model using IBM Watson Knowledge Studio (WKS) to find these fields in unstructered text. We achieve good results by using Dictionary based and Rule(Regex) based model for annotation and training custom model. We trained our IBM WKS model to identify abusive, bad words, which would be very relevant in current scenario of cyber bullying and abuse. 

## Live demo
A running instance has been deployed on AWS and is available at [Redactio.ml](http://redactio.ml).

**NOTE:** The demo link provided in the HackerEarth submission page is not working (because of https typo).

## Team details
- Team Name: TeamPsycho100
- Institute Name: IIITDM Jabalpur
- Team members
  - Amish Kumar Naidu
  - Ayaskant Panigrahi
  - Dhaval Taunk
  - Shivam Garg

## Technologies used
- IBM Watson Knowledge Studio and Natural Language Understanding
- Flask
- AWS and docker for deployment

## Screenshots
#### Homepage
![Homepage](https://github.com/amhndu/Hackathon2019/blob/master/screenshots/homepage.png)
#### A sample input
![A sample input](https://github.com/amhndu/Hackathon2019/blob/master/screenshots/homepage_example.png)
#### Personal info fields highlighted
![Personal info fields highlighted](https://github.com/amhndu/Hackathon2019/blob/master/screenshots/review_example.png)
#### Redacted text based on selection by user
![Redacted text based on selection by user](https://github.com/amhndu/Hackathon2019/blob/master/screenshots/redacted_example.png)

## Running with docker
- Clone the repo
- Copy `secret.py.sample` to `secret.py` and substitute api keys/secrets there
- Run `docker build --tag=hackathon2019 .` to build the docker image
- Then `docker run -p 5000:80 hackathon2019` to launch it at port `5000`

## Running Locally
- Setup a virtual environment (optional).
- `pip install -r requirements.txt`
- Copy `secret.py.sample` to `secret.py` and substitute api keys/secrets there
- Linux:
```
export FLASK_ENV=development
export FLASK_APP=app.py
```
Windows:
```
set FLASK_ENV=development
set FLASK_APP=app.py
```
Common:
```
flask run
```
