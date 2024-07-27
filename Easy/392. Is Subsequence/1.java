class Solution {
    public boolean isSubsequence(String s, String t) {
        if(s.equals("")){
            return true;
        }
        if(t.equals("")){
            if(s.equals("")){
                return true;
            }
            else{
                return false;
            }
        }
        char[] u = s.toCharArray();
        char[] v = t.toCharArray();
        int i = 0;
        int j;
        for(j = 0 ; j < v.length ; j++){
            if(i == u.length){
                break;
            }
            if(u[i] == v[j]){
                i++;
            }
        }
        if(i == u.length){
            return true;
        }
        else{
            return false;
        }
    }
}