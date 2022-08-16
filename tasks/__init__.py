
from random import choice
from string import ascii_lowercase
from typing import Text

from invoke import Collection, Context, task


@task
def generate_random_string(context, length = 512):
    print(''.join(choice(ascii_lowercase) for _ in range(length)))


tasks = Collection()
tasks.add_task(generate_random_string)
