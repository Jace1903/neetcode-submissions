public class Solution {
    public bool IsPalindrome(string s) {
        string ans = new string(s.Where(char.IsLetterOrDigit).ToArray()).ToLower();
        int left = 0;
        int right = ans.Length - 1;
        
        while (left < right)
        {
            if (ans[left] != ans[right])
            {
                return false;
            }
            left++;
            right--;
        }
        
        return true;
    }
}