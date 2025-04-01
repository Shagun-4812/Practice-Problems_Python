
def generate_parenthesis(n):
    """
    Generates all valid combinations of n pairs of parentheses.
    
    Args:
        n: The number of pairs of parentheses to generate
        
    Returns:
        A list of strings containing all valid combinations
    """
    def backtrack(current, open_remaining, close_remaining):
        # Base case: all parentheses used
        if open_remaining == 0 and close_remaining == 0:
            result.append(current)
            return
        
        # Case 1: Add opening parenthesis if we have any left
        if open_remaining > 0:
            backtrack(current + '(', open_remaining - 1, close_remaining)
        
        # Case 2: Add closing parenthesis if we have more opened than closed
        if close_remaining > open_remaining:
            backtrack(current + ')', open_remaining, close_remaining - 1)
    
    result = []
    if n >= 0:  # Handle edge case of negative input
        backtrack("", n, n)
    return result

# Example usage and testing
if __name__ == "__main__":
    test_cases = [
        (0, [""]),
        (1, ["()"]),
        (2, ["(())", "()()"]),
        (3, ["((()))", "(()())", "(())()", "()(())", "()()()"])
    ]
    
    for n, expected in test_cases:
        print(f"\nTesting n = {n}")
        result = generate_parenthesis(n)
        print(f"Expected: {expected}")
        print(f"Result:   {result}")
        print(f"Match:    {sorted(result) == sorted(expected)}")