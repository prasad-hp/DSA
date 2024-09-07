function selSort(arr){
    let temp
    let count
    for(let i = 0; i < arr.length; i++){
        let min = arr[i]
        for(let j = i; j < arr.length; j++){
            min = Math.min(arr[j], min)
            if(arr[j] == min){
                count = j
            }
        }
        temp = arr[i]
        arr[i] = min
        arr[count] = temp
    }
    return arr
}
console.log(selSort([6,9,5,3,7,6, 2]))