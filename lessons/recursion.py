from __future__ import annotations
from typing import Union

class Node:
    data: int
    next: Union[Node, None]

    def __init__(self, data: int, next:Union[Node, None]):
        self.data = data
        self.next = next


head: Node = Node(3, None)
head: Node = Node(2, None)
head = Node(1, head)
# head: Node = Node(1, None)
# tail: Node = Node(2, None)
#    head.next = tail