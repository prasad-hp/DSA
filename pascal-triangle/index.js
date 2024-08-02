var generate = function(numRows) {
    let ans = []
    if(numRows === 0){
        return ans
    }
    ans.push([1])
    for(let i = 1; i < numRows; i++){
        let row = []
        row.push(1)
        let prevRow = ans[i-1]
        for(let j = 1; j < i; j++){
            let num = prevRow[j-1]+prevRow[j]
            row.push(num)
        }
        row.push(1) 
        ans.push(row)
    }
    return ans
};
console.log(generate(5))