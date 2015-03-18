新建一个资源


拷贝

添加`.md`的文件

### 关联issue
提交commit时,在commit message里面使用`#issue`, 比如`#8`, github会自动关联`issue 8`跟这个commit. 当然在github上面写comment的时候使用这个也是有效的.

### 关闭issue
随着commit关闭一个issue,在confirm merge的时候可以使用以下命令来关闭相关issue:
```
fix #xxx
fixes #xxx
fixed #xxx
close #xxx
closes #xxx
closed #xxx
```

提交pull请求
