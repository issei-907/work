# wc

# seach_word_cloud



## 必要なツールのインストール

### Go
### version  go1.15.6 darwin/amd64

### Python
### version   3.7.4

### Pythonのライブラリのインストール

```
$ pip install beautifulsoup4
$ pip install selenium
$ pip install urllib
$ pip install requests
$ pip install wordcloud
$ pip install boto3
$ pip install chromedriver-binary
$pip install webdriver_manager
```



## パッケージを取得する

```
$ git clone 
$ go get github.com/maku77/gosample
```

## 実行方法
```
$ go run wc_go ‘論文詳細画面のurl’
```

## 例
```
$ go run wc_go　https://pubmed.ncbi.nlm.nih.gov/21676388/
```

## s3のURLにwc.pngの画像が保存される

# https://s3-ap-northeast-1.amazonaws.com/wc.project/wc.png
