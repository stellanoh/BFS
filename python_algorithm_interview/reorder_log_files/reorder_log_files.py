from typing import List


def reorder_log_files(self, logs: List[str]) -> List[str]:
    letters, digits = [], []
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)

    # lambda를 사용해 sorting
    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    return letters + digits
