class Solution {
    
    /**
     * @param {string[]} operations
     * @return {number}
     */

    calPoints(operations) {

        let stack = []
        let token
        let val 

        for (let i = 0; i < operations.length; i++) {
            token = operations[i]
            val = Number(token)

            if (!Number.isNaN(val)) {
                stack.push(val)
            } else {
                if(token === "+" ){
                    if(stack.length >= 2) {
                        stack.push(stack[stack.length-1] + stack[stack.length-2])
                    }
                } else if(token === "C") {
                    if (stack){
                        stack.pop()
                    }
                } else if(token === "D"){
                    if(stack){
                        stack.push(stack[stack.length-1] * 2)
                    }
                } else {
                    continue
                }
            }
        }

        const sum = stack.reduce((acc, num) => acc + num, 0)
        return  sum
    }
}
