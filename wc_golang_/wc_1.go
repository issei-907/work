//コマンドライン引数で論文詳細画面のurlを与える

package main

import (
	"flag"
	"fmt"
	"os"
	"os/exec"
)

func main() {

	flag.Parse()
	var url string = flag.Arg(0)
	cmd := exec.Command("python", "wc_2.py", url)
	cmd.Stderr = os.Stderr
	cmd.Stdout = os.Stdout
	cmd.Stdin = os.Stdin

	// Start the process
	if err := cmd.Start(); err != nil {
		panic(err)
	}
	if err := cmd.Wait(); err != nil {
		fmt.Println("cmd.Wait() in parent process:", err)
	}
}
