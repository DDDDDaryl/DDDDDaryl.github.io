---
title: git error - protocol 'https' not supported.
date: 2020-05-26 16:46:03
categories:
- techissue
tag:
- git
---

精准到位一针见血的回答：https://stackoverflow.com/questions/53988638/git-fatal-protocol-https-is-not-supported

具体来说，我们是如何遇到问题的呢？

- 在 github 仓库中 paste url
- 在 git bash 中`ctrl+v`，发现没用
- 于是右键点击`paste` 
- 事实上在`ctrl+v`时命令行有一个不可见的错误编码的`^?`
- 因此删掉重新打就好了