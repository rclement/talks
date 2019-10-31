# Talk: Python + Celery

> Meetup Python Grenoble - 2019/10/30

> Manage your asynchronous tasks with Celery!

## Setup

This environment requires:

- `python 3.7.4` (you can use `pyenv`)
- `pipenv`
- `docker`

Setup the environment:

1. `pipenv install -d`
2. (optional) `pre-commit install --config .pre-commit-config.yml`
3. (optional) `inv qa`

## Slides

`jupyter nbconvert notebooks/talk_python_celery.ipynb --to slides --post serve`

## Demo

1. Start a Redis message broker: `docker-compose up -d`
2. Copy the configuration: `cp .env.example .env`
3. Monitor Celery tasks with Flower: `honcho start monitor` and go to `http://localhost:5555`
4. Start all the neeeded processes: `honcho start [tasks|users|mailing|cron]`
5. Run some one-shot tasks: `python -m example.app`

## VSCode

Use the following `.vscode/launch.json` config (be sure to replace `example.celery:celery_app` and `--queues=default` with appropriate values):

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Celery: worker",
      "type": "python",
      "request": "launch",
      "justMyCode": false,
      "module": "celery",
      "args": [
        "worker",
        "--app",
        "example.celery:celery_app",
        "--queues=default",
        "--loglevel=info",
        "--pool=solo"
      ]
    }
  ]
}
```
