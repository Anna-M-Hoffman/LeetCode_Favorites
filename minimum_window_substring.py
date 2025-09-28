# MINIMUM WINDOW SUBSTRING
# Given two strings s and t, return the shortest substring of s 
# such that every character in t, including duplicates, is present 
# in the substring. If such a substring does not exist, return an empty string "".
# Example: s = "OUZODYXAZV", t = "XYZ"

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if s == "": return "" # Cannot find the substring of an empty string
        countT, window = {}, {} # {'A':1}
        
        for c in t: # Count each character of t in countT hashmap
            countT[c] = 1 + countT.get(c, 0)
        
        l = 0
        having, need = 0, len(countT)
        res = [-1, -1]
        resLen = float("infinity")

        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0) # Increment count of s[r] in the current window
            if s[r] in countT and countT[s[r]] == window[s[r]]: # Enough of s[r] in the window to satisfy t’s requirement
                having += 1
            while having == need:
                if (r - l + 1) < resLen: # If a proper window is smaller than current result
                    res = [l, r] # Store the current smallest window's start and end indices
                    resLen = (r - l + 1)
                window[s[l]] -= 1 # Remove the left character from the window
                # If new left is one of the characters to find and the window count for it is less than required
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    having -= 1 # The window has one less than what to find
                l += 1               


        if resLen == float("infinity"): # No valid window was found, return empty string.
            return ""

        return s[res[0] : res[1] + 1]

# Time Complexity: O(n + len(t)) 
# Space Complexity: O(u), where u is the number of unique characters in t


