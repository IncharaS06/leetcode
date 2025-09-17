class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
        def postorder(root):
            if not root:
                return
            
            postorder(root.left)
            postorder(root.right)
            res.append(root.val)

        postorder(root)
        return res

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap=[(x, i) for i, x in enumerate(nums)]
        heapify(heap)
        for _ in range(k):
            x, i=heap[0]
            heapreplace(heap, (x*multiplier, i))
        for x, i in heap:
            nums[i]=x
        return nums


        
