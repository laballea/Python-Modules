from time import sleep, time
from tqdm import tqdm


def ft_progress(lst):
    num = 0
    t0 = time()
    while True:
        currentTime = time() - t0
        eta = 0 if num == 0 else currentTime * len(lst) / num
        prct = num * 100 / len(lst)
        loadString = "=" * int(prct / 100 * 41)
        b = "ETA: {:.2f}s [{:.2f}%][{}] {}/{} | elapsed time {:.2f}s".format(
            float(eta),
            prct,
            (loadString + ">").ljust(41, " "),
            num,
            len(lst),
            float(currentTime)
        )
        print(b, end="\r")
        if (prct == 100):
            break
        yield num
        num += 1


listy = range(3333)
ret = 0

# for elem in tqdm(listy):
for elem in ft_progress(listy):
    ret += elem
    sleep(0.005)
print()
print(ret)
