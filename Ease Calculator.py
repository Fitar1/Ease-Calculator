# Ease-Calculator
import time
import signal
import gc  # 引入垃圾回收模块

def signal_handler(signum, frame):
    print("收到中断信号，程序退出")
    exit(0)

def slow_running_program():
    counter = 0
    while True:
        result = 1
        for i in range(counter):
            result *= i
        counter += 1

        if counter % 1000 == 0:
            print(f"Iteration: {counter}")

        # 添加时间间隔，以避免程序过于占用资源
        time.sleep(0.01)

        # 每隔一定迭代次数进行垃圾回收，释放内存
        if counter % 5000 == 0:
            print("进行垃圾回收")
            gc.collect()

if __name__ == "__main__":
    # 注册中断信号处理器
    signal.signal(signal.SIGINT, signal_handler)

    try:
        slow_running_program()
    except Exception as e:
        print(f"发生异常: {e}")
    finally:
        print("程序正常退出")
