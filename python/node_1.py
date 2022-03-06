

# 노드의 데이터는 노드를 생성할 때 지정되며 변경할 수 없습니다
# 링크는 초기화 시 선택 사항이며 업데이트할 수 있습니다.

class Node:
  def __init__(self, value, link_node=None):
    self.value = value
    self.link_node = link_node
    

  # 노드 내에서 데이터 및 링크에 액세스하는 방법
  def get_value(self):
    return self.value

  def get_link_node(self):
    return self.link_node