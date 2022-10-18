class Node:
  def __init__(self, value=None, next=None):
    self.value = value
    self.next = next
  
  def __repr__(self):
    return f"Node({self.value})"

# 특정 값의 node 찾기 -> head_node (이미 만들어진 링크드 리스트에서 검색)
def search(head_node, target) -> bool:
  current_node = head_node
  while current_node:
    if current_node.value == target:
      return True
    current_node = current_node.next
  return False

# 새 node를 순서에 맞게 삽입 -> head_node (이미 만들어진 링크드 리스트에서 검색)
def insert_node(head_node, target) -> None:
  current_node = head_node
  while current_node.next != None:
    # 지금 노드의 value보다 작거나 같으면서 다음 노드의 값보다 작은 위치 찾기
    if current_node.value <= target and current_node.next.value > target:
      # 해당 값을 node로 추가하기
      dummy = current_node.next
      current_node.next = Node(target, dummy)
      return
    current_node = current_node.next
  current_node.next = Node(target, None)
  return None

# 모든 노드의 값을 출력하기
def see_list(head):
  while head:
    print(head.value)
    head = head.next

# 리스트를 받아서 링크드 리스트 생성하기
def build_list(values) -> list:
  head = cur = Node()
  while values:
    # 리스트의 맨 앞 요소부터 빼내서 Node로 보내기
    head.next = Node(values.pop(0))
    head = head.next
  return cur.next


if __name__ == "__main__":
  l1 = [1,2,3,4,5,6]
  node1 = build_list(l1)
  # if search(node1, 3):
  #   print("found")

  insert_node(node1, 2.5)
  see_list(node1)