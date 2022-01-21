import libcst as cst
from typing import List, Tuple, Dict, Optional

#print(dump(cst.parse_module("EMATradingBot.py")))
#print(dump(cst.parse_expression("1 + 2 + 3")))
cst.parse_module("EMATradingBot.py")

class TypingCollector(cst.CSTVisitor):
    def __init__(self):
        self.stack: List[Tuple[str, ...]] = []
        self.annotations : Dict [
            Tuple[str, ...],
            Tuple[cst.Parameters, Optional[cst.Annotation]],
        ] = {}

    def count_IfDef(self, node: cst.If) -> Optional[bool]:
        self.stack.append(node.name.value)

    def leave_IfDef(self, node: cst.If) -> None:
        self.stack.pop()




