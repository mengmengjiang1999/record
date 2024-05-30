# ICSFuzz: Manipulating I/Os and Repurposing Binary Code to Enable Instrumented Fuzzing in ICS Control Applications
ICSFuzz: Manipulating IOs and Repurposing Binary Code to Enable Instrumented Fuzzing in ICS Control Applications

https://www.usenix.org/system/files/sec21fall-tychalas.pdf

https://github.com/momalab/ICSFuzz

https://www.usenix.org/conference/usenixsecurity21/presentation/tychalas


3.2 Comparing programming languages

尽管写了同样的功能，如果采用不同的编程语言，那么得到的二进制文件仍然可能有很大的不同。其中的原因在于，不同的编程语言会插入不同的NOP。

NOP addition is typically used in embedded systems to introduce intentional delays for timing purposes such as memory load/store in order to avoid potential problems aris- ing from non-deterministic memory access.

3.3 Potentially vulnerable functions in PLC applications

在PLC编程环境中存在一些函数，可能导致内存安全问题。

4.1 Fuzzing Control Applications

这一节讲了PLC fuzzing和常规fuzzing相比的难点。

第一步：PLCfuzzer如何知道进程因为发生crash而中止？看不懂，总之解决了这个问题。

第二步：如何给出输入

第三步：


ICSFuzz做的就是把二进制文件下载下来然后用AFL fuzzing一下。真的看不出工作量在哪里。



在6节 "Discussion and Related Work"（讨论和相关工作）中，文章讨论了与本文研究相关的其他工作，并对比了它们与本研究的不同之处。以下是该部分的翻译内容：

近年来，工业控制系统（ICS）的安全性受到了广泛关注。大部分研究集中在通过网络级别的安全措施（如入侵检测系统（IDS）或异常检测）来保护系统，而对控制应用程序本身的关注较少。传统上，PLC控制应用/软件被研究主要是作为将恶意负载部署到设备本身，以破坏连接的工业过程的手段，一个突出的例子是Stuxnet。因此，控制应用程序一直被视作恶意软件本身，或是被恶意软件感染的合法应用程序，大部分工作集中在检测和揭示恶意负载[44,45]。模糊测试也是嵌入式设备安全分析中的热门话题，目标设备包括智能电表[3]、智能手机[58]、汽车[27]以及各种其他设备[32]。一个有趣的工作是将输入生成模糊测试引入到机器人车辆（RV）控制代码的评估中，并发现可能导致不正确控制决策的案例[29]。在实践和研究中，PLC控制软件很少接受安全评估，很少有出版物与本研究相关。相反，许多先前的努力针对的是PLC控制应用/软件的安全性验证。在[7]和[25]中，作者执行特定语言的PLC控制应用验证。其他工作集中在通过运行时监控和验证来检测PLC控制应用的潜在破坏[18,26]。VETPLC[64]旨在通过考虑事件序列及其时间限制来验证现实世界的PLC代码。这些解决方案主要关注检测安全违规行为。SymPLC[23]利用OpenPLC[5]框架和Cloud9引擎[9]对控制应用进行动态分析。作者使用符号执行来评估控制应用二进制代码，将应用程序视为软件而不仅仅是控制过程的辅助工具。引入的SYMPLC框架将控制应用字节码抽象为基于C的高级表示。利用成熟的符号分析工具，作者成功地为测试的二进制文件实现了高功能覆盖率。在[28]中，作者通过手动探索目标二进制和通过符号执行进行自动化分析，解决了Codesys派生的控制应用的逆向工程。作者成功地生成了一个控制流图，覆盖了每一个函数，无论是静态还是动态调用，涵盖了整个应用程序。利用这些信息，他们展示了基于常规控制应用的自动化即时攻击制定。仿真是辅助模糊测试的一种流行方法，如[35,65]所示。然而，在我们的平台中，仿真的实现并不像在典型的基于Linux的系统中那样直接[55]。无论是部分仿真、二进制本身完全仿真，还是完整系统仿真，要纳入我们的框架中都是非常具有挑战性的：

- 部分仿真，例如I/O模块仿真，本质上可以替代我们的输入强制方法，但这并不容易。I/O模块是专有外围设备，没有公开给公众的软件规范。基于其已知功能的I/O模块的简单仿真可能是可行的，但它将无法通过Codesys框架对有效连接的I/O外围设备进行I/O检查。

- 二进制本身的完整仿真是一个极其具有挑战性的任务，考虑到其独特的加载过程。在框架之外，PLC二进制只是一堆包装在文件中的汇编指令。逐行执行是一个选项，但它将在第一个需要系统调用的输入交付处失败，该调用由框架路由和处理。

- 完整系统仿真将提供对模拟实例的完全控制，并能够操纵条件，例如前述的I/O检查。然而，带有Codesys框架的完整系统仿真本身是一个非常具有挑战性的项目。虽然最近发布了广泛的固件仿真框架，但它们缺乏特定于工业控制系统的细微差别，例如处理非通用外围设备如I/O模块，或实时调度程序。

总结来说，我们总结了问题陈述部分2.1中出现的问题的答案：

- PLC二进制文件由于PLC编程语言的高级特性以及它们所解决的非常明确的问题，本质上是健壮的。然而，随着二进制文件在大小或功能上的复杂性增加，可以引入可能危及宿主系统或工业过程的可利用漏洞。

- PLC运行时受到困扰常规C/C++开发软件的相同问题的影响，这危及整个工业控制系统计算堆栈。

- 模糊测试是发现工业控制系统中漏洞的一个很好的工具，即使在存在大量I/O和扫描周期的情况下也是如此。

致谢：
本项目部分由美国海军研究办公室资助，奖项编号N00014-15-1-2182，以及由纽约大学阿布扎比全球博士奖学金计划支持。

资源：
ICSFuzz将在以下GitHub存储库中提供：https://github.com/momalab/icsfuzz。