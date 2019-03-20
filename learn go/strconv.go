//学习strconv包
package main

import (
	"fmt"
	"strconv"
)

func main() {
	//布尔值转换为字符串
	var flag1 = true
	s1 := strconv.FormatBool(flag1)
	fmt.Println("布尔值转换为字符串：", s1)
	fmt.Printf("\n")

	//字符串转换为布尔值
	s2 := "1"
	flag2, err := strconv.ParseBool(s2)
	if err == nil {
		fmt.Println("字符串转换为布尔值：", flag2)
	} else {
		fmt.Println("字符串转换成布尔值失败：", err)
	}
	fmt.Println("\n")

	//整数转换为字符串
	var number1 = 100 //十进制数100
	s3 := strconv.FormatInt(int64(number1), 10)
	fmt.Println("整数转换为字符串（十进制）：", s3)
	s3 = strconv.Itoa(number1)
	fmt.Println("整数转换为字符串（十进制）：", s3) //FormatInt(i,10)的简写
	s4 := strconv.FormatInt(int64(number1), 2)
	fmt.Println("整数转换为字符串（二进制）：", s4)
	fmt.Println("\n")

	//字符串转换为整数
	number2, err := strconv.ParseInt("100", 10, 0)
	if err == nil {
		fmt.Println("（十进制）字符串转换为整数：", number2)
	} else {
		fmt.Println("（十进制）字符串转换为整数失败：", err)
	}
	number, err := strconv.Atoi("100") //ParseInt(s,10,0)的简写
	if err == nil {
		fmt.Println("（十进制）字符串转换为整数：", number)
	}
	number3, err := strconv.ParseInt("100", 2, 0)
	if err == nil {
		fmt.Println("（二进制）字符串转换为整数：", number3)
	} else {
		fmt.Println("（二进制）字符串转换为整数失败：", err)
	}
}
