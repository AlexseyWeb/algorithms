import concurrent.futures


def some_function(count=1, limit=2):
    for i in range(1, int(limit)):
        count = i + i
    return count


if __name__ == '__main__':
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        results = executor.map(some_function,  't2')
        print('After map')
        for r in results:
            print(f"{r=}")

    print('ended main')
