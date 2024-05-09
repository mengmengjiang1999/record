# A Systemic Review of Kernel Fuzzing

https://dl.acm.org/doi/abs/10.1145/3444370.3444586?casa_token=DrUa44IfINoAAAAA:t5TYT4XOH-EqhNDYCWzt2yKonwgNUi8l1Q6t5vw6nK5KQ0USKfg__N7Eu1dJWZ92UksCYZjt51rC

https://dl.acm.org/doi/pdf/10.1145/3444370.3444586


Knowledge-based Fuzzer

Trinity会根据系统调用接口的数据类型来针对性地生成系统调用序列和数据

Moonshine会对应用程序进行轻量级的静态分析，并且引入了一个算法，使得裁剪后的系统调用序列仍然不会降低覆盖率

但是静态分析存在局限性，例如当出现虚函数的时候，就没有办法做这个事情。

HFL结合了传统的Knowledge-based Fuzzing方法以及动态分析方法。

5.1.2  Coverage-guided Fuzzer

syzkaller [20], TriforceAFL [21], KAFL and UnicoreFuzz [22]

（原论文里甚至拼错了，感觉不是很专业的样子···但是至少可以作为参考吧）

介绍syzkaller。

TriforceAFL  They won't need to recompile pieces of the kernel with AFL, or figure about how instrument core parts of the kernel. 具体而言就是把kernel和coverage guided的部分分开了。

kAFL：如果一个进程去fuzzing自己的kernel，那么kernel crash会严重影响fuzzing过程，因为产生bug就会crash，crash就会需要reboot。reboot开销又很大。
为了解决这个问题，使用了Virtual Machine Hypervisor and Intel's Processor Trace (PT)技术。

Unicorefuzz模拟CPU的状态，来测试特定的内核代码部分。


5.2 文件系统Fuzzer

面临的问题：

1. metadata只占1%左右，大多数mutation会变异数据，这并不会对文件系统状态产生实质的影响
2. 文件操作的结果和文件系统当前的状态有关

（这段就不具体看了）


5.3 Data Race Vulnerability

Krace [28] and Razzer [29] are typical representatives of these works.

