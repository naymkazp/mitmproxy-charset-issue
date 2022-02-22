# mitmproxy-charset-issue


## Error


Bug: When you pass flow.response to response(flow) method the encoding breaks in the content.
The screenshot shows a comparison of the text output in the two terminals:
    ![Bug](/bug.png)
The second terminal displays the text of the file, received in curl. A regular expression has been applied to it, to quickly find encoding problems.

The first terminal displays the response text passed to the response(flow) method. It displays the same regular expression as in curl. You can see that some characters have encoding problems.

## Steps to reproduce 
1. Run in 1st terminal
```
mitmdump --ssl-insecure -p 8182 -s proxy.py --set block_global=false
```
2. Run in 2nd terminal
```
curl --insecure https://csdnimg.cn/release/cmsfe/public/js/chunk/tpl/www-index-new/index.b37193db.js --proxy "localhost:8182" 2>&1 | grep -ioE " e\}\)\(e\)\}s=function\(e\)\{\"use strict\";var t=\{1:(.{15})"
```
