//コマンドライン引数で論文詳細画面のurlを与える

package main

import (
	"fmt"
	"os"
	"os/exec"
)

func main() {
	//articleidをString型で与える
	wc("29112865")
}
func wc(articleid string) {
	//var articleid string = "29112865"
	var url string = "https://pubmed.ncbi.nlm.nih.gov/" + articleid + "/"
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
