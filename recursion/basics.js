ans = 1
function factorial(n){
    if(n>0){
        ans *= n
        factorial(n-1)
        return ans
    }
}

console.log(factorial(5))