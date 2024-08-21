from __future__ import annotations
import steganography.main
from pathlib import Path
import sys
import pandas as pd
from timeit import timeit


def run_test(cover: str, data: str, i: int, short_hand: str) -> list:
    cover_path = Path(cover)
    new_name = f"{cover_path.stem}-{short_hand}-{i}{cover_path.suffix}"
    args = ["embed", "-t", cover, "-p", data, "-o", new_name, "-b", str(i)]
    def func(): return steganography.main.main(*args)
    t1 = timeit(func, number=1)
    t2 = timeit(func, number=1)
    t3 = timeit(func, number=1)
    return [t1, t2, t3]


def main() -> int:
    assert len(sys.argv) == 4
    _, cover, data, data_name = sys.argv
    results: dict = {}
    for i in range(1, 9):
        res = run_test(cover, data, i, data_name)
        print(res)
        results[i] = res
    print()
    table = pd.DataFrame(results).transpose()
    print(table)
    table.to_csv(Path(cover).stem+"-"+Path(data).stem+".csv")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
