# 2024spring week3

20240311-20240317

计划：

1. 读论文
2. 找一个能复现的
3. 找张超组同学问问
4. 写到github上

## 关于fuzzing specifications

内核模糊测试（kernel fuzzing）的背景下，"fuzzing specification"（模糊测试规范）是指一组定义，用于指导模糊测试工具如何生成有效的系统调用（syscall）序列。这些规范详细说明了系统调用的参数类型、它们之间的关系以及如何构造这些参数的值，以便模糊测试工具可以生成既合法又有可能触发内核中潜在错误的输入。

具体来说，模糊测试规范通常包括以下几个方面：

系统调用描述：定义每个系统调用的名称、参数类型和预期的行为。例如，openat 系统调用可能需要一个文件路径字符串和一个打开模式整数。

参数类型：详细说明每个参数的数据类型，包括基本类型（如整数、指针）和复合类型（如结构体、联合体）。

参数值：指定参数可能取的具体值或值的生成规则。这可能包括常量值、范围限制或根据某些条件动态生成的值。

依赖关系：描述系统调用之间的依赖关系，例如，一个系统调用可能需要另一个系统调用返回的文件描述符作为输入。

资源管理：定义资源（如文件描述符、内存对象）的生命周期，包括它们的创建、使用和释放。

通过Syzlang语言进行描述，在内核代码越来越多的情况下，手动生成specification跟不上版本，所以需要一些自动化的方式。
相关研究：见syzgen++的总结，那个表格总结得很好。KernelGPT到底和其他工作哪里不一样？还是没明白。
需要速成一些软件分析知识。


## 论文分类及大概内容

### 1. 自动生成系统调用规范相关

##### No Grammar, No Problem: Towards Fuzzing theLinux Kernel without System-Call Descriptions

Boston University

https://par.nsf.gov/servlets/purl/10438507

FUZZNG，与syzkaller不同的是，不需要系统调用接口描述就可以fuzz内核。

FUZZNG 这个看起来也很厉害，据说实验结果也很不错。

Unlike previous approaches, FUZZNG reshapes the kernel’s input space, rather than attempting to automatically generate system-call descriptions。

reshape的意思是，希望这个fuzzer可以知道data要被存放在内存的哪个位置。然而实际上，因为数据在内存中的地址是运行的时候才给的，本质上是随机数，所以没发让fuzzer来猜这个事情。因此采用别的办法，具体来说就是给fuzzer一些新的权限：That is, at any moment, FUZZNG is aware of the memory and fds that are actively accessed by the kernel. 

设计思路：
One mechanism to realize input-space reshaping could directly replace the return values of the memory-access and file-descriptor APIs with fuzzed data. However, instead, FUZZNG places fuzzed data at the locations referenced by the memory-access and file-descriptor APIs.
FUZZNG reshapes the inputspace, so that the kernel does not reject the majority of inputs due to invalid pointers and fds.

后面还写了关于指针、fd、VM等机制如何高效fuzz。然后讲了具体实现，但是好难懂。先暂且跳过。

总之这个工作看起来特别有意义，但是应该是一个很难复现的工作吧。

##### SyzGen++: Dependency Inference for Augmenting Kernel Driver Fuzzing

University of California, Riverside

https://zhyfeng.github.io/files/2024-Oakland-SyzGen++.pdf

syzgen++的工作流程，它旨在自动推断驱动接口之间的显式依赖关系，并为基于模型的模糊器生成规范。

先不说工作怎么样，这篇文章本身写得非常好。

这篇文章在讲工作背景的时候讲得很好，我觉得是这几篇文章里面写得最好的。又简洁又清楚，摘录如下：
Fuzz testing is an automated technique for discovering vulnerabilities that randomly generates test inputs and feeds them to the target program until it crashes. For syscalls that require complex nested structures as inputs and heavily sanitize the user-provided data for security concerns, a naive fuzzer is unlikely to produce valid inputs that could reach deep code, resulting in low code coverage.ll specifications in Syzlang, a strongly typed language to specify the structures and constraints of the inputs and the relationship between fields (e.g., one field indicates the length of another one), as shown in Fig. 1. Specifically, the resource type in Syzlang represents a “handler” (i.e., explicit dependency) produced by the kernel. Other types (e.g., const) are selfexplanatory. Implementing specifications is a manual and time-consuming process, particularly when the source code is unavailable.

设计和实现的部分：

先识别出driver，以及入口函数。对于MacOS和Linux有不同的做法，看起来不复杂。
然后对于每一个driver，使用符号执行来给出syscall输入的类型和约束。
它会识别出所有的内存操作，然后通过pattern matching去识别insertion和lookup，如果它们是对同一个地址进行操作的，就说明它们之间有依赖关系。具体而言，作者认为，具备以下三个特征的insert和look up是有依赖关系的：
(1) the insertion operation creates a new heap object and stores it; 
(2) the lookup operation retrieves different objects depending on the user input, and 
(3) both insertion and lookup operate on the same data container reachable from a global variable.
具体还挺复杂的写了整整2页，最复杂的是第3步。不过大部分是理论推导，结论似乎不长，应该可以不用看。
然后经过以上操作，就会得到这些依赖关系，最后生成fuzzing specifications（QAQ这部分看不懂）我觉得为了看懂可能需要先dfs一下符号执行等软件分析理论。


##### KSG: Augmenting Kernel Fuzzing with System Call Specification Generation

软院姜宇老师组

https://www.usenix.org/conference/atc22/presentation/sun

自动生成系统调用规范

（软院姜宇老师组）

这篇论文的工作背景也写得很好，中国人写的就是符合中国人口味（x

+ First, the kernel source code is compiled based on the given configuration, which outputs a bootable kernel image and a series of files containing the Clang AST. The AST provides the kernel with code information for each stage of the analysis. When the kernel boots, the entry extraction module hooks multiple probes dynamically before and after specific kernel functions.
+ KSG then scans various device files and network protocols, thus triggering the execution of hooked kernel functions, which can be captured by the probes. Consequently, the probes can detect and extract the submodules’ entries. Based on the AST and entries, KSG analyzes the range constraints and input types in each execution path of each entry with path-sensitive analysis.
+ Finally, based on the collected information, KSG generates specifications in domain language Syzlang for fuzzers, where the syntax mapping and semantics encoding are performed. The specifications can be generated with the aforementioned process, and the effectiveness of fuzzers can be improved with the generated specifications.

KSG steps:

1. get the entry: probe-based tracing(どう言う意味ですか) because the entry of submodules would be stored in certain data structures in the kernel. the detail is complex.(QAQ)
2. collect input information: how to get the type and constrants? symbolic execution of CSA. then KSG can get the type and range of parameters.
3. generate specifications: generate Syzlang for kernel. syntax mapping and semantic encoding.

##### SyzDescribe: Principled, Automated, Static Generation of Syscall Descriptions for Kernel Drivers

University of California

https://ieeexplore.ieee.org/abstract/document/10179298

自动为Kernel驱动生成系统调用规范

##### KernelGPT: Enhanced Kernel Fuzzing via Large Language Models

UIUC

利诺伊大学厄巴纳-香槟分校（University of Illinois at Urbana-Champaign）的缩写。这所大学位于美国伊利诺伊州的厄巴纳（Urbana）和香槟（Champaign）两个相邻的城市。UIUC 是一所著名的公立研究型大学，以其在工程、计算机科学、农业、商学等领域的强劲实力而闻名。

https://arxiv.org/abs/2401.00563

KernelGPT，这是第一个通过大型语言模型（LLMs）自动推断Syzkaller规范以增强内核模糊测试的方法

这篇文章只在arxiv上挂了一下，好像没有上什么会之类的。


KernelGPT完成Driver Detection（驱动器检测）的过程是通过以下步骤实现的：

1. **定位设备操作处理器**：
   - 使用专门的代码解析器（例如基于LLVM的工具）来搜索内核代码库，定位设备操作处理器（例如，`file_operations`结构中的`ioctl`函数指针）的初始化实例。
   - 通过查找`ioctl`或`unlocked_ioctl`字段在操作处理器结构中的初始化情况，来识别`ioctl`处理器函数。

2. **推断设备名称**：
   - 利用LLMs的能力，根据定位到的设备操作处理器和它们的使用情况来推断设备名称。
   - 为了提高推断的准确性，KernelGPT可能会使用少样本上下文学习技术，通过提供特定的提示（prompt）来指导LLMs。

3. **生成初始化规范**：
   - 根据设备名称和设备操作处理器的详细信息，LLMs生成设备的初始化规范。
   - 这通常涉及到创建一个系统调用序列，如`openat`或`syz_open_dev`，用于初始化设备驱动程序。

4. **提取使用信息**：
   - 从内核代码中提取与设备操作处理器相关的使用信息，这可能包括处理器函数的调用点和它们在代码中的上下文。
   - 这些信息有助于LLMs更准确地理解设备如何在内核中被使用，从而生成更准确的规范。

5. **整合规范**：
   - 将LLMs生成的设备名称和初始化规范整合成完整的fuzzing specification，这些规范随后可以被模糊测试工具用来生成测试用例。

通过Driver Detection步骤，KernelGPT能够自动识别内核中未被描述的驱动程序，并为它们生成初始的fuzzing specification，为后续的模糊测试打下基础。这个过程减少了人工参与，提高了规范生成的效率和覆盖率。


详情见：[KernelGPT: Enhanced Kernel Fuzzing via Large Language Models.md](../papers/KernelGPT: Enhanced Kernel Fuzzing via Large Language Models.md)



### 2. 评估fuzzer的性能

##### On the Effectiveness of Synthetic Benchmarks for Evaluating Directed Grey-box Fuzzers
KAIST

https://softsec.kaist.ac.kr/~sangkilc/papers/lee-apsec23.pdf

用来评估现有fuzzer的有效工具


### 3. 其他

##### SegFuzz: Segmentizing Thread Interleaving to Discover Kernel Concurrency Bugs through Fuzzing
KAIST

https://ieeexplore.ieee.org/abstract/document/10179398/

针对内核并发性bug的fuzz

##### Horus: Accelerating Kernel Fuzzing through Efficient Host-VM Memory Access Procedures

姜宇老师组

https://dl.acm.org/doi/full/10.1145/3611665

通过加速host和guest之间的内存数据交换来加速fuzz（感觉应该不止能用来加速fuzz吧）


## 尝试回答下列问题

1. 工作背景是什么？具体而言，是kernel fuzzing非常重要，然后fuzz的时候有什么必要步骤，目前存在什么问题？参考：
   Fuzz testing is an automated technique for discovering vulnerabilities that randomly generates test inputs and feeds them to the target program until it crashes. For syscalls that require complex nested structures as inputs and heavily sanitize the user-provided data for security concerns, a naive fuzzer is unlikely to produce valid inputs that could reach deep code, resulting in low code coverage.ll specifications in Syzlang, a strongly typed language to specify the structures and constraints of the inputs and the relationship between fields (e.g., one field indicates the length of another one), as shown in Fig. 1. Specifically, the resource type in Syzlang represents a “handler” (i.e., explicit dependency) produced by the kernel. Other types (e.g., const) are selfexplanatory. Implementing specifications is a manual and time-consuming process, particularly when the source code is unavailable.
2. 解决方法有哪些？有篇论文里面总结的特别好，可以作为参考。
3. Kernel GPT说它跟其他这几种方法采用了不一样的方法，具体是哪些地方不一样？

## 选择复现哪篇论文的考虑因素

1. 这个工作的潜力，工作本身的质量如何？从这个角度考虑，KernelGPT是首选，因为似乎这是第一篇，而且在大模型现在很火的情况下应该可以沿着继续做。
2. 和原作者的距离如何？从这个角度来说清华超哥组的文章是首选（除了上面几篇应该还能在看看vul337有没有什么相关的），软院组的也可以。除此之外校内还有组在做fuzz吗
3. last but not least，复现文章不光要看别人的水平，也要看看自己的水平（

最终得到的几个备选：

KernelGPT: Enhanced Kernel Fuzzing via Large Language Models
看起来很厉害但是没有开源TT

SyzGen++: Automated Generation of Syscall Specification of Closed-Source macOS Drivers
https://github.com/seclab-ucr/SyzGenPlusPlus
这个感觉挺好的，开源了至少
钱志云老师组的工作

KextFuzz: Fuzzing macOS Kernel EXTensions on Apple Silicon via Exploiting Mitigations [USENIX Security 2023]
https://github.com/vul337/KextFuzz
declare that 自己在Kext specification方面比SyzGen更厉害
张超老师组的工作，抱大腿方便
但是不是专门搞fuzzing specification auto-generation的工作，这个是附带做的


## 根据目前在做这个方向的组进行分类

网研院张超老师组
软院姜宇老师组
University of California Riverside钱志云老师组

KAIST School of Computing
KAIST Cyber Security Research Center
韩国科学技术院的计算机系和网研院

Redhat


#### 张超老师组

张超老师组跟内核fuzz有关的论文有这么几篇：


1. StateFuzz: System Call-Based State-Aware Linux Driver Fuzzing
https://www.usenix.org/system/files/sec22-zhao-bodong.pdf
https://github.com/vul337/StateFuzz

StateFuzz is state-aware fuzzing solution for fuzzing Linux kernel drivers.

It utilizes static analysis to recognize shared variables that are accessed by multiple program actions, and use them as state-variables to characterize program states.

By tracing values of state-variables and using a combination of two state-variables as feedback, StateFuzzcan explore states during fuzzing while increasing code coverage.

fuzz Linux driver的，是fuzz方法上的改进


2. KextFuzz: Fuzzing macOS Kernel EXTensions on Apple Silicon via Exploiting Mitigations (USENIX Security'23)
https://github.com/vul337/KextFuzz

fuzz MacOS driver的。keypoint is not on how to generate specification automatically.但是它同样需要解决这个问题。

因为是专门用来fuzz MacOS的，而 We notice that the kext userspace "wrappers" can provide abundant interface information. To mitigate the potential risk from non-standard user input, macOS provides abstract layers for kernel services in userspace, which includes frameworks, libraries, system daemons, etc. These components encapsulate complex kext invocations into well-defined services and interact with kexts in standard ways. They call kext interfaces in proper sequences and set arguments that meet the value and type requirements. By analyzing these wrappers, KextFuzz can infer the interface structures.

简而言之就是MacOS里面有一层抽象层，这个抽象层在用正确的方式调用kext interface，因此只要分析一下这一个抽象层是如何调用接口的，就可以了。

（只有在MacOS才适用的工作）

3. PrIntFuzz: Fuzzing Linux Drivers via Automated Virtual Device Simulation
PrIntFuzz is an efficient and universal fuzzing framework that can test the Linux driver code, include the PRobing code and INTerrupt handlers.

The following instructions guide you to set up the fuzzing environment and perform multi-dimension fuzzing on various device drivers.

Tested on Ubuntu 20.04.1.

https://github.com/vul337/PrIntFuzz

PrIntFuzz的虚拟设备建模是通过静态分析技术从Linux驱动程序中提取关键信息，并利用这些信息来构建虚拟设备，这些设备能够在没有实际硬件支持的情况下与驱动程序进行交互。具体来说，虚拟设备建模包括以下几个方面：

数据空间建模：分析驱动程序在初始化过程中对硬件寄存器的读取操作，并执行的健全性检查。PrIntFuzz通过静态数据流分析来推断寄存器应有的正确值，并确保虚拟设备在这些检查中能够通过，从而模拟设备的正常行为。

I/O和内存空间建模：每个PCI设备可以有多个I/O地址区域，包括内存或I/O地址。PrIntFuzz识别驱动程序中用于检查区域类型的宏或函数，并记录区域的位置和资源类型，以便在模拟设备时能够正确匹配。

配置空间建模：PCI设备包含多个配置寄存器，这些寄存器保存了有关硬件的配置信息。驱动程序在扫描设备时会读取这些寄存器。PrIntFuzz执行字段敏感的静态分析来识别pci_driver结构，并从中提取pci_device_id结构，这些结构定义了驱动程序支持的设备类型列表。

系统调用模板生成：除了通过提取驱动程序的必要信息来建模虚拟设备，PrIntFuzz还分析驱动程序的接口来生成系统调用模板。这些模板用于生成与设备驱动程序交互的系统调用序列。

通过上述建模过程，PrIntFuzz能够创建出能够与Linux内核驱动程序进行有效交互的虚拟设备。这些虚拟设备可以模拟真实硬件的行为，包括设备探测、中断处理和I/O操作，从而允许模糊测试框架在没有物理硬件的情况下对驱动程序进行全面的测试。这种方法显著提高了测试的覆盖率，并有助于发现驱动程序中潜在的安全漏洞。

特别厉害，就是看起来没什么关系。


