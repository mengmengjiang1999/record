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

TriforceAFL
