from pathlib import Path

import anyio
from anyio import to_thread


def print_dir_content():
    current_dir = Path.cwd()
    for file in current_dir.iterdir():
        print(file)


async def display_dir_content(event):
    await to_thread.run_sync(print_dir_content)
    event.set()


async def wait_print_finished(event):
    print('wait dir printing is finished')
    await event.wait()
    print('finished!')


async def main():
    event = anyio.Event()
    async with anyio.create_task_group() as tg:
        tg.start_soon(display_dir_content, event)
        tg.start_soon(wait_print_finished, event)


anyio.run(main)
