//学习函数
//函数作为参数
package main

import (
	"fmt"
	"reflect"
	"runtime"
)

func add(a, b int) int {
	return a + b
}
func apply(op func(int, int) int, a, b int) int {
	fmt.Printf("Calling %s with %d,%d\n", runtime.FuncForPC(reflect.ValueOf(op).Pointer()).Name(), a, b)
	return op(a, b)
}
func main() {
	result := apply(add, 1, 2)
	fmt.Println("The result is ", result)
}
