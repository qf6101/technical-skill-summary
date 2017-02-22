### scala io (better-files)

* http://colobu.com/2016/05/11/better-files-Simple-safe-and-intuitive-Scala-I-O/

* https://github.com/pathikrit/better-files

### scalikejdbc

* http://scalikejdbc.org/

### json

* http://json4s.org/

* https://github.com/lift/lift/tree/master/framework/lift-base/lift-json

### tokenizers

* https://github.com/NLPchina/ansj_seg

* https://github.com/ysc/word

* https://github.com/ysc/cws_evaluation

### python regex to match http urls 

```
regex = re.compile(
    r'^(?:http|ftp)s?://' # http:// or https://
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' # domain...
    r'localhost|' # localhost...
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|' # ...or ipv4
    r'\[?[A-F0-9]*:[A-F0-9:]+\]?)' # ...or ipv6
    r'(?::\d+)?' # optional port
    r'(?:/?|[/?]\S+)$', re.IGNORECASE)
 ```
(from: http://codereview.stackexchange.com/questions/19663/http-url-validating)
