![App logo](https://github.com/HE-Arc/kodecupid/blob/main/identity/logo1024.png)
```> [SUCCESS] New connection established !```

*KodeCupid Dating App*
=====================

Welcome to KodeCupid, a dating app for developers and computer scientists. Our goal is to help you find your significant other based on computer-related filters, such as preferred programming languages.

**Requirements to Begin Development**
------------------------------------

* Docker
* Docker Compose

**Installation and Run**
-------------------------

Clone the repository:
```bash
git clone git@github.com:HE-Arc/kodecupid.git
cd kodecupid
```

Disable auto-crlf on Windows (some scripts will be executed on Linux):
```bash
git config --local core.autocrlf false
```

Copy the .env.example file and update it with your environment variables.
Launch the Docker container:
```bash
docker compose up
```

# Accessing the App

The KodeCupid app can be accessed on:
* localhost:80 (web interface)
* localhost:8000 (API)
