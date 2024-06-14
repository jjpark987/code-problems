#!/usr/bin/env ts-node

// time: O(n), space: O(1)
class Solution {
    static spinWords = (words: string): string => {
        return words.split(' ').map(w => {
            if (w.length < 5) {
                return w
            } else {
                return w.split('').reverse().join('')
            }
        }).join(' ')
    }
}

const solution = Solution.spinWords("Hey fellow warriors")
console.log(solution)
console.log('Expected: "Hey wollef sroirraw"')

/*
Write a function that takes in a string of one or more words, and returns the same string, but with all words that have five or more letters reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

Examples:

"Hey fellow warriors"  --> "Hey wollef sroirraw" 
"This is a test        --> "This is a test" 
"This is another test" --> "This is rehtona test"
*/