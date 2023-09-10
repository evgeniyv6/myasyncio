
from collections import deque
def isPol(s: str) -> bool:
    de = deque()
    for ch in s.lower():
        if ch.isalpha():
            de.append(ch.lower())
    for ch in s.lower():
        if ch.isalpha():
            if ch.lower() != de.pop():
                return False
    return True

if __name__ == '__main__':
    print(isPol('A man, a plan, a canal: Panama'))
    print(isPol('0p'))