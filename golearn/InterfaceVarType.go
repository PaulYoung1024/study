//反向知道interface变量里实际保存的是哪个类型的对象
package main

import (
	"fmt"
	"strconv"
)

type Element interface{}
type List []Element
type person struct {
	name string
	age  int
}

//print person type
func (p person) String() string {
	return "(name:" + p.name + "-age:" + strconv.Itoa(p.age) + " years)"
}

func main() {
	list := make(List, 3)
	list[0] = 1                  //int type
	list[1] = "hello"            //string type
	list[2] = person{"Paul", 26} // person type
	for index, element := range list {
		if value, ok := element.(int); ok {
			fmt.Printf("list[%d] is int type, and its value is %d\n", index, value)
		} else {
			if value, ok := element.(string); ok {
				fmt.Printf("list[%d] is string type, and its value is %s\n", index, value)
			} else {
				if value, ok := element.(person); ok {
					fmt.Printf("list[%d] is person type, and its value is %s\n", index, value)
				} else {
					fmt.Println("list[%d] is of a different type", index)
				}
			}
		}
	}
}
