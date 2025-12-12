class Solution {
public:
    bool isPalindrome(int x) {
        if (x<0) {
            return false;
        }
        int org = x, ld;
        long long revn = 0;
        while (x!=0) {
            ld = x%10;
            x=x/10;
            revn=(revn*10) + ld;
        }
        return(org == revn);
    }
};
