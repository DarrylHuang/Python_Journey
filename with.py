from contextlib import contextmanager

@contextmanager
def pause(divisor):
    try:
        print("start")
        yield divisor + 1
        divisor += 1
        print("end")
    except Exception as e:
        print(f"catch：{e}")
    finally:
        print("end", divisor)

origin_divisor = -1
with pause(origin_divisor) as divisor:
    print(f"divisor is {divisor}")
    print(f"origin_divisor is {origin_divisor}")
    print(1 / divisor)

