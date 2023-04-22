import sys
input = sys.stdin.readline
# N = int(sys.stdin.readline().strip())에서 입력 받은 값의 타입을
# 정수형으로 바꾸고, 문자열 끝에 있는 개행 문자('\n')을 제거합니다.
N = int(sys.stdin.readline().strip())
# tree라는 딕셔너리를 생성합니다. 딕셔너리를 사용하여 트리를 구현합니다.
# for _ in range(N) 구문을 통해 루트, 왼쪽 자식, 오른쪽 자식 노드들을 입력 받고, 딕셔너리에 저장합니다.
tree = {}
for _ in range(N):
    root, left, right = sys.stdin.readline().strip().split()
    tree[root] = [left, right]

# 전위 순회
def preorder(root):
    if root != '.':
        print(root, end='') #root
        preorder(tree[root][0]) #left
        preorder(tree[root][1]) #right

# 중위 순회
def inorder(root):
    if root != '.':
        inorder(tree[root][0])  # left
        print(root, end='')  # root
        inorder(tree[root][1])  # right
# 후위 순회
def postorder(root):
    if root != '.':
        postorder(tree[root][0])  # left
        postorder(tree[root][1])  # right
        print(root, end='')  # root

preorder('A')
print()
inorder('A')
print()
postorder('A')
print()