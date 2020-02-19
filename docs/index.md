# eFarmer

[![Build Status](https://travis-ci.org/oskarsakol/eFarmer.svg?branch=master)](https://travis-ci.org/oskarsakol/eFarmer)

Api for farmer sales market. Check out the project's [documentation](http://oskarsakol.github.io/eFarmer/).

# Prerequisites

- [Docker](https://docs.docker.com/docker-for-mac/install/)  
- [Travis CLI](http://blog.travis-ci.com/2013-01-14-new-client/)

# Initialize the project

Start the dev server for local development:

```bash
docker-compose up
```

Create a superuser to login to the admin:

```bash
docker-compose run --rm web ./manage.py createsuperuser
```


# Continuous Deployment

Deployment automated via Travis. When builds pass on the master or qa branch.
You're ready to continuously ship! ✨ 💅 🛳
