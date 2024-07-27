class Solution {
    public boolean isPalindrome(int x) {
        char[] arr = String.valueOf(x).toCharArray();
        boolean check = false;
        int a;
        int b;
        if(x < 0){
            return check;
        }
        else if(arr.length == 1){
            check = true;
            return check;
        }
        else{
            b = arr.length - 1;
        for(a = 0 ; a < arr.length ; a++){
            if(!(arr[a]==arr[b])){
                break;
            }
            b--;
            if(b < a){
                check = true;
                break;
            }
        }
        return check;
        }
    }
}