## Overview

hunter_io_client is a Python package that provides a streamlined interface for interacting with the Hunter.io API, enabling developers to perform domain searches, find emails, and verify email information efficiently.

## Pre Reqs
* `Python 3.12`
* `virtualenv`

## Setup
* Create virtual environment

    `virtualenv -p /path/to/python env`

* Activate virtual environment

    `source ./env/bin/activate`

* Install packages using pip command

    `pip install -r requirements.txt`

* Run main for testing different functions of client

    `python main.py`

## Usage:
```
import os
from hunterio.client import HunterAPIClient

API_KEY = os.getenv("API_KEY", "")

hunter_client = HunterAPIClient(api_key=API_KEY)

# Get domain based data
domain_data = hunter_client.search_domain("test.com")

# Get domain based email data for a user
domain_email_data = hunter_client.email_finder("test.dev", first_name="test", last_name="user")

# Get email verification data
domain_data = hunter_client.verify_email("test@test.com")
```