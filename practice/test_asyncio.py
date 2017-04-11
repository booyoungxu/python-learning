# -*- coding: utf-8 -*-

import asyncio
import time

@asyncio.coroutine
def hello():
    print("Hello world! %s" % time.time())
    # 异步调用asyncio.sleep(1):
    r = yield from asyncio.sleep(1)
    print("Hello again! %s" % time.time())

# 获取EventLoop:
loop = asyncio.get_event_loop()
# 执行coroutine
loop.run_until_complete(hello())
loop.close()