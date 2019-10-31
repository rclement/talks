from invoke import task


app_path = "example"


@task
def safety(ctx):
    ctx.run("safety check", pty=True)


@task
def lint(ctx):
    ctx.run(f"flake8 {app_path}", pty=True)


@task
def static_check(ctx):
    ctx.run(f"mypy --strict {app_path}", pty=True)


@task
def reformat(ctx):
    ctx.run(f"black .", pty=True)


@task(safety, lint, static_check)
def qa(ctx):
    pass
