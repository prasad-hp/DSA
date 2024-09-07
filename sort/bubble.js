function bubbleSort(arr){
    let temp
    for( let i = 0; i < arr.length-1; i++){
        for(let j = 1; j <= arr.length -i -1; j++){
            if(arr[j-1] > arr[j]){
                temp = arr[j-1]
                arr[j-1] = arr[j]
                arr[j] = temp
            }
        }
    }
    return arr
}

console.log(bubbleSort([9,5,4,6,7,1, 7, 3]))