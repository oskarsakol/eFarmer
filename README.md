# eFarmer

[![Build Status](https://travis-ci.org/oskarsakol/eFarmer.svg?branch=master)](https://travis-ci.com/oskarsakol/eFarmer)


Api for farmer sales market. Check out the project's [documentation](http://oskarsakol.github.io/eFarmer/).

# Prerequisites

- [Docker](https://docs.docker.com/docker-for-mac/install/)  
- [Travis CLI](http://blog.travis-ci.com/2013-01-14-new-client/)

# Local Development

Start the dev server for local development:
```bash
docker-compose up
```

Run a command inside the docker container:

```bash
docker-compose run --rm web [command]
```

For example creation of superuser:

```bash
docker-compose run --rm django python manage.py createsuperuser
```

# Continuous Deployment

Deployment is automated via Travis. When builds pass on the master or qa branch.

You're now ready to continuously ship! ✨ 💅 🛳
