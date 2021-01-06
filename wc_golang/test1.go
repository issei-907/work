//コマンドライン引数で論文詳細画面のurlを与える

package main

import (
	"fmt"
	"os"
	"os/exec"
)

func main() {
	var url string = "https://pubmed.ncbi.nlm.nih.gov/33385359/"
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
