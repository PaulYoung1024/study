//学习函数
package main

import (
	"fmt"
)

//函数返回多个值时，可以起名字
//仅用于非常简单的函数
func div(dividend, divisor int) (quotient, remainder int) {
	quotient = dividend / divisor
	remainder = dividend % divisor
	return
}
func main() {
	q, r := div(5, 2)
	fmt.Println("商为：", q)
	fmt.Println("余数为：", r)
}
