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


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        morse_str = ''
        res = []
        for word in words:
            for char in word:
                morse_str += codes[alphabet.index(char)]
            if morse_str not in res:
                res.append(morse_str)
            morse_str = ''
        return len(res)

        
