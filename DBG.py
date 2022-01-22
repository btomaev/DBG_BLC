#! /usr/bin/env python
# -*- coding: utf-8 -*-
from dbg_utils_blc import *

names = ["Retry_88", "OVALEXOLK", "Dashut", "Senko_"]
names2 = ["Nimoryan"]
timing = datetime.datetime.now()

while True:
    if(datetime.datetime.now() >= timing):
        timing = datetime.datetime.now()+datetime.timedelta(minutes = 60)
        update("Retry", names)
        update("Nimoryan", names2)
    else:
        time.sleep(2)

# setup("Retry", 60, names)

# while True:
#     loop = asyncio.get_event_loop()
#     tasks = [loop.create_task(update(names)), loop.create_task(request())]
#     wait_tasks = asyncio.wait(tasks)
#     loop.run_until_complete(wait_tasks)