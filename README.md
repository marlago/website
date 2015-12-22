# A Website for Sol

## Setup

Use conda to recreate the environment
```
conda env create -f conda_environment.yml
```

## Firing up the server for deverlopment

There are two things we need to start developing with this server.
First, we need to make sure our changes are tracked in real time. This can be achieved
with the following command:
```
fab regenerate
```

Then we need to start up the server itself:
```
python -m http.server
```
