# Flask bootstrap template. 

## To install dependencied

```bash
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

## to run
```bash
$  python run.py
```

Then navigate to http://localhost:5000/

# AWS services

## Install aws cli
```bash
$ brew install aws
``` 
## Install SAM

```bash 
$ sudo pip install aws-sam-cli
```

# Deploying

## zappa

```bash
$ source venv/bin/activate
$ pip install zappa
$ zappa init 
(venv) $ zappa init
(venv) $ zappa package dev
```


## SAM
_as Server less Application Model_


```bash
sam package --template-file template.yml --output-template-file packaged.yml --s3-bucket proj-input
```

```bash
sam deploy --template-file packaged.yml --stack-name xreport-sam --capabilities CAPABILITY_IAM
```