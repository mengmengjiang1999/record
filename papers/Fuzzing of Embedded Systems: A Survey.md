# Fuzzing of Embedded Systems: A Survey

@article{embeddedsystemsurvey,
author = {Yun, Joobeom and Rustamov, Fayozbek and Kim, Juhwan and Shin, Youngjoo},
title = {Fuzzing of Embedded Systems: A Survey},
year = {2022},
issue_date = {July 2023},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
volume = {55},
number = {7},
issn = {0360-0300},
url = {https://doi.org/10.1145/3538644},
doi = {10.1145/3538644},
abstract = {Security attacks abuse software vulnerabilities of IoT devices; hence, detecting and eliminating these vulnerabilities immediately are crucial. Fuzzing is an efficient method to identify vulnerabilities automatically, and many publications have been released to date. However, fuzzing for embedded systems has not been studied extensively owing to various obstacles, such as multi-architecture support, crash detection difficulties, and limited resources. Thus, the article introduces fuzzing techniques for embedded systems and the fuzzing differences for desktop and embedded systems. Further, we collect state-of-the-art technologies, discuss their advantages and disadvantages, and classify embedded system fuzzing tools. Finally, future directions for fuzzing research of embedded systems are predicted and discussed.},
journal = {ACM Comput. Surv.},
month = dec,
articleno = {137},
numpages = {33},
keywords = {Firmware fuzzing, IoT devices, firmware analysis, fuzzing, embedded systems, software testing, symbolic execution, concolic execution}
}

## RQ1: What are the differences between traditional fuzzing and ESF?

问题：嵌入式系统和固件是什么？

3.1大概介绍了一下

问题：type1, type2, type3 devices是什么？

3.2节回答了这个问题，根据operating system的特征

Type 1 (T1): Embedded Devices with General-purpose OS

Type 2 (T2): Embedded Devices with Custom-built OS

Type 3 (T3): Embedded Devices with Monolithic Software
（ai generation）
这段文字描述的是第三类（T3）嵌入式设备，这类设备具有单体软件架构。单体软件在这里指的是将系统和应用程序的功能集成在一起，并通过编译来实现的软件。
例如，许多小规模的设备，如智能卡、GPS接收器或恒温器，就属于这种形式。这些设备通常没有硬件抽象层，也就是说，它们不会隐藏物理硬件的细节，也不提供编程接口。这意味着设备的硬件组件和软件组件之间的交互更加直接，没有中间层来抽象和简化这种交互。这种设计使得设备能够以一种紧凑和高效的方式运行，尽管这可能会牺牲一些灵活性和可扩展性。

问题：Comparison between Traditional Fuzzing and ESF

3.3.1 Strong Hardware Dependency.

3.3.2 Crash Detection. 嵌入式设备通常缺少崩溃检测机制，系统挂了用户也没法及时知道。

3.3.3 Instrumentation 静态源代码插桩（编译的时候）和动态二进制插桩

静态插桩就像Tardis做的那样
动态二进制插桩另有常用的工具，不过据说在Embedded OS上会很难做

3.3.4 Performance and Scalability

Typically, fuzzing requires re-executing the program under test (PUT) to maintain a clean state for every test input. By reverting virtual machine snapshots, this technique is easy for desktop systems. However, this is difficult for embedded devices that require a substantial amount of time to reset the device. In addition, parallel fuzzing execution is possible in desktop systems. However, parallelization is frequently impossible in embedded devices, such as embedded OS devices or devices without an OS. Thus, repeated trials are impossible, or an embedded system takes a long time to fuzz.

我理解这段的意思应该是：如果想要对一个embedded os进行重复测试，需要硬件状态什么的都一致。这就使得成本很高了

3.4 Traditional Taxonomy of Fuzzers

3.4.1 Black-box Fuzzer
Similarly, the black-box fuzzer randomly mutates the seed test cases based on predefined rules without identifying the PUT’s inner information。就是这样的fuzzer只管接口正确就好了，并不会收集反馈。至于这个输入是否trig新的分支，并不关心

3.4.2 White-box Fuzzer.
先放着。我没看明白white-box到底啥意思啊？

3.4.3 Gray-box Fuzzer.

灰盒模糊测试工具位于黑盒模糊测试工具和白盒模糊测试工具之间，它只需要目标程序（即PUT，被测试程序）的部分信息。这些部分信息通常是通过插桩产生的代码覆盖率或通过污点分析产生的污点流信息。
（污点分析）


## RQ2: What are the types of fuzzing techniques for embedded systems, and how do they differ from each other?

按照：connectivity between the fuzzer and a target embedded system进行分类

4.1.1 Direct Fuzzing. This approach directly connects the target device and tests the system firmware without intervention.通过network或者debugging interface。但是这种方式需要大量的手工操作

4.1.2 Emulation-based Fuzzing. 对部分固件进行仿真，然后在仿真环境下进行测试。

4.1.3 直接进行固件分析


## RQ3: How do they solve the fuzzing challenges of embedded systems?



## RQ4: What are the research challenges and future research trends?


5 FUZZING STEPS IN DETAILS

对嵌入式设备进行fuzz，第一步是要先得到这个固件。这并不是一件容易的事情，很多时候连二进制文件都拿不到

