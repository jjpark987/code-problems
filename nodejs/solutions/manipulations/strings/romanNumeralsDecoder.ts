#!/usr/bin/env ts-node

// time: O(n), space: O(n)
class Solution {
    static romanNumeralsDecoder (roman: string): any {
        const table: { [key: string]: number } = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        const intArray = roman.split('').map(char => {
            if (table.hasOwnProperty(char)) {
                return table[char]
            }
            return 0
        })

        return intArray.reduce((acc, curr, i) => {
            if (i < intArray.length - 1 && curr < intArray[i + 1]) {
                return acc - curr
            } else {
                return acc + curr
            }
        }, 0)
    }
}

console.log(Solution.romanNumeralsDecoder('MCMXC'))
console.log('Expected: 1990')
console.log(Solution.romanNumeralsDecoder('MMVIII'))
console.log('Expected: 2008')
console.log(Solution.romanNumeralsDecoder('IV'))
console.log('Expected: 4')

/*
EASY

Create a function that takes a Roman numeral as its argument and returns its value as a numeric decimal integer. You don't need to validate the form of the Roman numeral.

Modern Roman numerals are written by expressing each decimal digit of the number to be encoded separately, starting with the leftmost digit and skipping any 0s. So 1990 is rendered "MCMXC" (1000 = M, 900 = CM, 90 = XC) and 2008 is rendered "MMVIII" (2000 = MM, 8 = VIII). The Roman numeral for 1666, "MDCLXVI", uses each letter in descending order.
*/