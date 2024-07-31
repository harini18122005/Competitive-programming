class Solution:
    def dataTypeSize(self, data_type: str) -> int:
        size_map = {
            "Character": 1,
            "Integer": 4,
            "Long": 8,
            "Float": 4,
            "Double": 8
        }
        return size_map.get(data_type, -1)

# Example usage
solution = Solution()