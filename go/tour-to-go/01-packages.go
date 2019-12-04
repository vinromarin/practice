// https://tour.golang.org/

package main

import (
  "fmt"
  "math"
)

const Pi = 3.14

func main() {
  fmt.Println("Pi = ", math.Pi) // name is exported if it begins with a capital letter - Pi
                                // "unexported" names are not accessible from outside the package
  fmt.Println("add:", add(42,13)) // -> 35
  fmt.Println(swap("Hello", "World")) // -> World Hello
  fmt.Println(returnNamedValues(2))   // -> 200 1400
}

func add(x, y int) int {
  return x + y
}

func swap(x, y string) (string, string) { // a func can return any number of arguments
  return y, x
}

func returnNamedValues(input int) (value1, value2 int) {
  value1 = 100 * input
  value2 = value1 * 7
  return // "naked" return = return w/o args
}
