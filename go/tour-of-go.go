// https://tour.golang.org/

package main

import (
  "fmt"
  "math"
)

func main() {
  fmt.Println("Pi = ", math.Pi) // name is exported if it begins with a capital letter - Pi
                                // "unexported" names are not accessible from outside the package
  fmt.Println("add:", add(42,13))
  fmt.Println(swap("Hello", "World"))
}

func add(x, y int) int {
  return x + y
}

func swap(x, y string) (string, string) { // a func can return any number of arguments
  return y, x
}
