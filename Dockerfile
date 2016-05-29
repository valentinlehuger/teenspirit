FROM python:2-onbuild
CMD ["mrq-worker", "--config", "./mrq-config.py", "tweets"]