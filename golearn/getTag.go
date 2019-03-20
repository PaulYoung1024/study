package main

import (
	"encoding/json"
	"fmt"
	"reflect"
)

func main() {
	type User struct {
		UserId   int    `json:"user_id"`   //Tag
		UserName string `json:"user_name"` //Tag
	}
	//struct转成json，输出json格式
	u := User{1, "Paul"}
	j, _ := json.Marshal(u)
	fmt.Println(string(j))

	//获取Tag中的内容
	u2 := &u
	t := reflect.TypeOf(u2)
	field := t.Elem().Field(0)
	fmt.Println(field.Tag.Get("json"))
}
