function printStar(n) {
    for (let i = 1; i <= n; i++) {
        let line = "";
        let space = "";
        let star = "";
        for (let j = 0; j < n-i; j++) {
            space += " ";
        }
        for(let j = 0; j < 2*i-1; j++){
            star += "*"
        }
        console.log(space+star+space);
    }
}

printStar(3);
