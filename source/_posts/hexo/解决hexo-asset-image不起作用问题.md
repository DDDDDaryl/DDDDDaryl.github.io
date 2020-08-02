---
title: 解决hexo-asset-image不起作用问题
date: 2020-06-02 10:53:03
categories:
- techissue
tags:
- hexo
- hexo-asset-image
---

首先自己的`hexo`版本如下：

```shell
$ hexo -v
hexo: 4.2.0
hexo-cli: 3.1.0
os: Windows_NT 10.0.18362 win32 x64
node: 12.16.3
v8: 7.8.279.23-node.35
uv: 1.34.2
zlib: 1.2.11
brotli: 1.0.7
ares: 1.16.0
modules: 72
nghttp2: 1.40.0
napi: 5
llhttp: 2.0.4
http_parser: 2.9.3
openssl: 1.1.1g
cldr: 36.0
icu: 65.1
tz: 2019c
unicode: 12.1

```

问题：本地图片上传到文章同名文件夹下，而 `.html`中图片引用相对链接并没有被转换为绝对路径，也就是说插件并没有工作。

解决：在 `hexo` 创建的博客文件夹下安装插件以及依赖。

在此过程中发现，实际上将本地图片拷贝到 `public` 文件夹下的操作是由 `config`中的`post_asset_folder`控制的，需要把选项置为`true`。

而我把自己的`permalink`修改为了`permalink: :category/:post_title/`，这样的话，相对路径转换为绝对路径时出现问题，字符串拆分错误，具体解决参考链接：https://nobige.cn/post/20190605-hexo-asset-imageFix/。

至此问题解决。

