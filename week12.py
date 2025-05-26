from collections import deque  # deque 입출입 양방향으로 처리됨

d = deque([91, 17, 33])
d.append(-14)
# d.appendleft(100)
d.append(99)  # enqueue
for _ in range(len(d)):
    print(d.popleft())  # dequeue