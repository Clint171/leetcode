/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    if(s.length % 2 !== 0) return false;
    let stack = [];
    for(let i in s){
        if(s[i] == "(" || s[i] == "[" || s[i] == "{"){
            stack.push(s[i]) 
        }
        else {
            let el = stack.pop();
            if(
                (s[i] == ")" && el !== "(") ||
                (s[i] == "]" && el !== "[") ||
                (s[i] == "}" && el !== "{")
            ){
                return false;
            }
        }
    }
    return stack.length === 0;
}