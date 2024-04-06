# 2024spring week4

20240318-20240324

## tsffs相关尝试

simics启动。

配好环境了，然后读了读文档。tsffs是基于simics的硬件模拟器做的。参考tsffs文档，做了tutorial中第一章部分。

[TSFFS Documentation](https://intel.github.io/tsffs/tutorials/kernel-module/index.html)

具体遇到的问题，详见：
[tsffs-simics](../coding/tsffs-simics.md)


## tsffs talk

https://www.youtube.com/watch?v=CG410v0EWzQ

重点总结：

### tsffs的优势有几点

1. 基于SIMICS而不是qemu

qemu的很多功能对于fuzz来说是完全没必要的，SIMICS读取硬件状态更加容易一些也更加快

2. 使用了一个什么开源协议，所以（啥？没看懂）

3. 方便开发者开发，修改fuzz流程

### fuzz流程

（从23:15开始，具体直接看视频）

CLI

LibAFL Frontend

SIMICS Module：当一些（例如exception之类的）发生时，会catch这个事情并记录，并更新覆盖率信息。以及负责snapshot等（可以认为这个simulator也承担了一部分fuzz的功能）

后面就是一些演示，如何配环境，然后写一个有bug的程序，然后写fuzz的配置文件，然后演示fuzz过程，总之看起来很厉害。可以作为入门的参考，不过这个流程文档上也都有写就是了（