#! /usr/bin/env python
# -*- coding: utf-8 -*-
from dbg_utils_blc import *

names = ["Retry_88", "OVALEXOLK", "Dashut", "Senko_"]

update("Retry", names)

# setup("Retry", 60, names)

# while True:
#     loop = asyncio.get_event_loop()
#     tasks = [loop.create_task(update(names)), loop.create_task(request())]
#     wait_tasks = asyncio.wait(tasks)
#     loop.run_until_complete(wait_tasks)