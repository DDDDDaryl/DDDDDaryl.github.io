---
title: Anaconda修改回默认源并配置代理
categories:
- python
tag:
- Anaconda
- proxy
---

今天准备跑一下`EfficientDet`的`Pytorch`实现，在配置环境的过程中发现之前配置的`Annaconda`清华源莫名其妙404了！于是只能选择一个一劳永逸的方法：更换会默认配置，然后配置proxy。

<!--more-->

Google了一大圈，解决方案都是如下：

- 首先移除配置好的镜像源：

  ```bash
  conda config --remove-key channels 
  ```

- 然后检查是否成功：

  ```bash
  conda config --show channels
  ```

  结果：

  ```bash
  (pytorch) C:\Users\Frank Young>conda config --show channels
  channels:
    - defaults
  ```

- 移除成功。

然而却没有移除`.condarc`中的default和custom channels，以及channel alias都没有修改，导致上述步骤完全无效，应该是当时更换清华源的时候使用了不恰当的方式。

解决：直接删除原`.condarc`，重新运行`conda prompt`会重新生成空的`.condarc`，此时配置代理：

```bash
proxy:
  - http: socks5://127.0.0.1:1080
  - https:socks5://127.0.0.1:1080
```

再安装`pyyaml`：

```bash
(pytorch) C:\Users\Frank Young>conda install -c anaconda pyyaml
Collecting package metadata (current_repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: E:\Anaconda\envs\pytorch

  added / updated specs:
    - pyyaml


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    ca-certificates-2020.1.1   |                0         165 KB  anaconda
    certifi-2020.4.5.1         |           py38_0         159 KB  anaconda
    openssl-1.1.1g             |       he774522_0         5.8 MB  anaconda
    pyyaml-5.3.1               |   py38he774522_0         168 KB  anaconda
    yaml-0.1.7                 |   vc14h4cb57cf_1         103 KB  anaconda
    ------------------------------------------------------------
                                           Total:         6.3 MB

The following NEW packages will be INSTALLED:

  pyyaml             anaconda/win-64::pyyaml-5.3.1-py38he774522_0
  yaml               anaconda/win-64::yaml-0.1.7-vc14h4cb57cf_1

The following packages will be SUPERSEDED by a higher-priority channel:

  ca-certificates    anaconda/cloud/conda-forge::ca-certif~ --> anaconda::ca-certificates-2020.1.1-0
  certifi            anaconda/cloud/conda-forge::certifi-2~ --> anaconda::certifi-2020.4.5.1-py38_0
  openssl                        anaconda/cloud/conda-forge --> anaconda


Proceed ([y]/n)? y


Downloading and Extracting Packages
certifi-2020.4.5.1   | 159 KB    | ############################################################################ | 100%
yaml-0.1.7           | 103 KB    | ############################################################################ | 100%
ca-certificates-2020 | 165 KB    | ############################################################################ | 100%
openssl-1.1.1g       | 5.8 MB    | ############################################################################ | 100%
pyyaml-5.3.1         | 168 KB    | ############################################################################ | 100%
Preparing transaction: done
Verifying transaction: done
Executing transaction: done
```

成功！特此纪念我浪费的时间......