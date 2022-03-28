package main

/*
Go 코드는 패키지 단위

main 패키지명은 프로그램 시작점(starting point)을 포함하는 패키지

메인 패키지는 프로그램에 오직 하나만 존재

따라서,
Go의 프로그램은 메인 패키지 1개와
다른 여러 패키지로 구성
*/

import "fmt"

/*
import 가져오다
"fmt" 가져올 패키지명

import "main" - 불가능
*/

func main() {
	/*
		func : function : 함수 선언
		main : 함수명 - main 함수명은 프로그램 시작점
	*/

	// 주석문 1 - 한줄 주석
	/* 주석문 2 - 블록 주석 */

	fmt.Println("Hello Go World")

	// fmt 패키지의 Println 함수를 호출
}

// func 함수명 입력부 출력부 { 함수 정의부분 }
// func
