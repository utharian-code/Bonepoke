from typing import List

class ExpansionNodeModule:
    def activate_expansion(self, fragment: str) -> List[str]:
        """
        Generates nested ritual expansions from composted fragment.
        """
        nodes = []
        if "vault" in fragment:
            nodes.append("Vaultkeeper memory loop")
        if "echo" in fragment:
            nodes.append("Echo recursion protocol")
        if "shard" in fragment:
            nodes.append("Shard as mythic anchor")
        if "collapse" in fragment:
            nodes.append("Collapse as ritual ignition")
        return nodes

