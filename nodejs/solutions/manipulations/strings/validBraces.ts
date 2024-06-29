#!/usr/bin/env ts-node

// time: O(n), space: O(n)
class Solution {
    static validBraces(braces: string): boolean {
        const stack: string[] = []
        const start = ['(', '[', '{']
        const end = [')', ']', '}']
        
        for (let index = 0; index < braces.length; index++) {
            const char = braces[index]
            
            if (start.indexOf(char) > -1) {
                stack.push(char)
            } else if (stack.pop() === start[end.indexOf(char)]) {
                continue
            } else {
                return false
            }
        }
        
        return stack.length === 0;
    }
}

console.log(Solution.validBraces('(){}[]'))
console.log('Expected: true')
console.log(Solution.validBraces('({[]})'))
console.log('Expected: true')
console.log(Solution.validBraces('[(])'))
console.log('Expected: false')

/*
EASY

Write a function that takes a string of braces, and determines if the order of the braces is valid. It should return true if the string is valid, and false if it's invalid.

This Kata is similar to the Valid Parentheses Kata, but introduces new characters: brackets [], and curly braces {}. Thanks to @arnedag for the idea!

All input strings will be nonempty, and will only consist of parentheses, brackets and curly braces: ()[]{}.

What is considered Valid?
A string of braces is considered valid if all braces are matched with the correct brace.
*/