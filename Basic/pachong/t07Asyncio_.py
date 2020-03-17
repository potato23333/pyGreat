# asyncio异步方式
# 可以加速的原因是网页响应的问题，大多数情况下，网页响应无法跟上计算机的处理速度
# 所以可以在等待一个网页时，先进行另一个网页的请求
import asyncio
import time

async def job(t):                   # async 形式的功能
    print('Start job ', t)
    await asyncio.sleep(t)          # 等待 "t" 秒, 期间切换其他任务
    print('Job ', t, ' takes ', t, ' s')

async def main(loop):                       # async 形式的功能
    tasks = [
        loop.create_task(job(t)) for t in range(1, 3)
    ]                                       # 创建任务, 但是不执行
    await asyncio.wait(tasks)               # 执行并等待所有任务完成

t1 = time.time()
loop = asyncio.get_event_loop()             # 建立 loop
loop.run_until_complete(main(loop))         # 执行 loop
loop.close()                                # 关闭 loop
print("Async total time : ", time.time() - t1)
# Start job  1
# Start job  2
# Job  1  takes  1  s
# Job  2  takes  2  s
# Async total time :  2.0259742736816406