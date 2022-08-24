import sys

input = sys.stdin.readline


class Node: # 바이너리 트리를 구성 할 노드 클래스 생성
    def __init__(self, data):
        self.data = data;
        self.left = None;
        self.right = None;


def preorder(node):
    print(node.data, end='')
    if node.left: preorder(node.left)
    if node.right: preorder(node.right)


def inorder(node):
    if node.left: inorder(node.left)
    print(node.data, end='')
    if node.right: inorder(node.right)


def postorder(node):
    if node.left: postorder(node.left)
    if node.right: postorder(node.right)
    print(node.data, end='')


n = int(input())
graph = []

for i in range(n):
    num, l, r = input().rstrip().split()
    node = Node(num)

    if l == '.': l = False
    if r == '.': r = False

    node.left = l
    node.right = r
    graph.append(node)

for i in range(n):
    for j in range(n):
        if graph[i].data == graph[j].left:
            graph[j].left = graph[i]
        elif graph[i].data == graph[j].right:
            graph[j].right = graph[i]

preorder(graph[0])
print()
inorder(graph[0])
print()
postorder(graph[0])
