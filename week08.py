
def in_order(node):   # 중위처리 방법 L P R
    if node is None:
        return
    in_order(node.left)
    print(node.data, end="->")
    in_order(node.right)

def pre_order(node): # 전위처리 방법 P L R
    if node is None:
        return
    print(node.data, end="->")
    pre_order(node.left)
    pre_order(node.right)


def post_order(node): # 후위처리 방법  L R P
    if node is None:
        return
    post_order(node.left)
    post_order(node.right)
    print(node.data, end="->")

class TreeNode:
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

def insert(root, value):  # 여기서 노드를 만들고 처리 한다.
    node = TreeNode()
    node.data = value

    if root is None:
        return node

    current = root
    while True:
        if value < current.data:
            if current.left is None:
                current.left = node
                break
            current = current.left  # 이동
        else:
            if current.right is None:
                current.right = node
                break
            current = current.right
    return root

# 이진탐색 트리 : BST
if __name__ == "__main__":
    numbers = [10, 15, 8, 3, 9, 100, 7, 13]
    root = None

    for number in numbers:
        root = insert(root, number)

    print('BST 구성 완료')
    post_order(root)

    # find_number = int(input())
    # current = root
    # while True:
    #     if find_number == current.data:
    #         print(f"{find_number}을(를) 찾았습니다")
    #         break
    #     elif find_number < current.data:
    #         if current.left is None:
    #             print(f"{find_number}이(가) 존재하지 않습니다")
    #             break
    #         current = current.left
    #     else:
    #         if current.right is None:
    #             print(f"{find_number}이(가) 존재하지 않습니다")
    #             break
    #         current = current.right

