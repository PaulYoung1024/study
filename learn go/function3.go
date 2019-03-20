//学习函数
package main

import (
	"fmt"
)

//可变参数列表
func sumArgs(values ...int) int {
	sum := 0
	for i := range values {
		sum += values[i]
	}
	return sum
}
func main() {
	sum := sumArgs(1, 2, 3)
	fmt.Println(sum)
}
