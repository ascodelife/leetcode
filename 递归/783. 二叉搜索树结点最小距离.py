# 给定一个二叉搜索树的根结点 root, 返回树中任意两节点的差的最小值。
#
# 示例：
#
# 输入: root = [4,2,6,1,3,null,null]
# 输出: 1
# 解释:
# 注意，root是树结点对象(TreeNode object)，而不是数组。
#
# 给定的树 [4,2,6,1,3,null,null] 可表示为下图:
#
#           4
#         /   \
#       2      6
#      / \
#     1   3
#
# 最小的差值是 1, 它是节点1和节点2的差值, 也是节点3和节点2的差值。
# 注意：
#
# 1.二叉树的大小范围在 2 到 100。
# 2.二叉树总是有效的，每个节点的值都是整数，且不重复。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.last_node = None
        self.Min = float('inf')
    def minDiffInBST(self, root: TreeNode) -> int:
        # 中序遍历
        if root.left:
            self.minDiffInBST(root.left)
        if self.last_node:
            self.Min = min(abs(root.val-self.last_node.val),self.Min)
        self.last_node = root
        if root.right:
            self.minDiffInBST(root.right)
        return self.Min
