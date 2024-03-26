# Tardis: Coverage-Guided Embedded Operating System Fuzzing
https://ieeexplore.ieee.org/document/9921188

软件学院姜宇老师组的工作

## 1. 当前的基于覆盖率的fuzz方法，为什么不能直接用于embedded os？

- architecture: Embedded OSs run on a variety of architectures and platforms
- intercafes: commonly used Embedded OSs are numerous and their interfaces are diverse, resulting in the difficulty of utilizing a unified coverage collection interface based on existing designs. many popular Embedded OSs do not support the complete suite of interfaces required. Meanwhile, different Embedded OSs normally provide different interfaces for user land, thus a unified, OS-agnostic design is needed for coverage collection
- efficiency: be efficient so that they would not significantly impact the execution throughput of the fuzzer

## 2. 对embedded OS进行fuzz的挑战主要有哪些？

- the coverage feedback mechanisms should be software-based and avoid relying on hardware-specific mechanisms to guarantee portability. 
- these mechanisms should be OS-agnostic, i.e., it is able to operate without relying on any OS-specific features and can adapt to different OSes without additional costs
- the mechanisms’ implementations should be highly efficient and avoid introducing any significant overheads. 因为embedded OS对效率要求比较高

## 3. approaches

- a bitmap-based storage for coverage collection for OS-agnostic design（这个bitmap是什么具体在后面design部分会说明）
- coverage collection during compilation（编译器插桩）
- efficiency: 
    - （通过共享内存的方式）the coverage buffer is shared between the host fuzzer and the guest though exposing partial memory space of QEMU instance
    - Tardis analyzes the collected coverage statistic on the host also with simple instructions in a CPU cache friendly manner


## 4. 具体设计

一个coverage-guide fuzzing包括下面几个步骤：

简单来说就是，fuzz程序会自动生成一些输入，喂给被测试的程序。
然后收集这些输入的覆盖率，看看新生成的这个输入是否触发了更多的程序路径去执行。
然后再根据覆盖率反馈的结果，去进一步调整输入。

我认为其中有两个关键技术，或者说两个要研究的问题：
一是关于输入数据的自动调整算法，如何根据覆盖率反馈的结果，效率更高地生成触发新的执行路径的输入
一是覆盖率的部分，如何得到程序覆盖率，并且反馈给fuzzer？


关于输入数据自动调整的部分，在其他的相关研究中应该很多了。这篇文章里不是重点，因为重点其实是先把整个fuzz流程跑起来再说。

关于覆盖率的部分，在现有的coverage-guided fuzzing中已经有了比较成熟的技术。但是这种技术是对用户态程序的测试来说比较成熟的技术，对于embedded OS，现有的技术不能直接使用。具体的原因前面的背景已经说过。

具体而言，想要得到覆盖率并反馈给fuzzer，需要进行以下几个步骤：

- coverage initialization。这个应该是coverage-guided fuzzing里面常用的专有名词，具体而言意思是：将被测试的代码划分为很多个基本块，并且通过一些厉害的技术（回调函数什么的），使得这个基本块如果被执行，那么fuzzer就可以得到通知
- 覆盖率统计。具体来说就是不仅要知道这个基本块有没有被执行过，还希望知道这个执行路径有没有被执行过。但是在这篇文章里面，统计的是边覆盖率，就是说将基本块看成节点，一个基本块到另一个基本块的执行顺序看成一条有向边，统计这条边有没有被执行过，以及被执行了多少次。
- coverage analyse。具体而言就是，在以上两个步骤完成之后，fuzzer已经得到了新的覆盖率信息。希望能够以一个比较高的效率知道，相比之前的输入，是否有覆盖到新的执行路径。因为每次输入都需要进行一次比较步骤，因此希望这个步骤尽可能高效。


### Coverage Collection initialization

如何测试覆盖率：
将每一个OS basic block给一个ID，如果跑过这个基本块的代码，host就会把它记录下来。
callback for initialzation是为用户态程序设计的，对于Embedded OS来说存在效率不高的问题（什么意思？）所以需要动态初始化机制，以及更加高效的覆盖率反馈机制（什么意思？）
As a consequence, the existing mechanism for coverage collection initialization provided by Clang compiler may not get invoked during the target kernel booting phase。虽然不懂为什么，但是现有的coverage collection initialization可能并不能在内核中有用。
解决方法是，将两个callback function在编译内核的时候插入到每一个基本块中（什么？）
提出了一个a dynamic initialization mechanism去解决coverage collection initialization的问题（但是这两个词是什么意思？）


总之大概意思是，现有的用于用户态程序的coverage collection initialization技术，并不能直接地用于embedded OS中。因为xxxx（一个我没看明白的原因）

解决方法是：Tardis通过一种厉害的技术完成初始化。完成这个操作的目的在于：完成之后可以通过callback function统计覆盖率信息。


====ai generation start=====

`pc_trace_guard_init` 是一个在编译器中用于插桩（instrumentation）的回调函数，它是由 Clang 编译器的 SanitizerCoverage 工具使用的。这个函数的主要作用是在程序的执行过程中初始化覆盖率数据收集的基础设施。在Tardis fuzzer中，coverage initialization（覆盖率初始化）是一个关键步骤，它确保在嵌入式操作系统启动时正确设置了覆盖率收集的基础设施。以下是覆盖率初始化的具体步骤：

1. **编译阶段**：
   - 使用Clang编译器对嵌入式操作系统的源代码进行交叉编译。
   - 在编译过程中，利用Clang的插桩功能，在每个基本块的入口处插入回调函数`pc_trace_guard()`，用于记录代码分支的执行情况。
   - 同时，插入`pc_trace_guard_init()`回调函数，该函数在程序启动时被调用，用于初始化覆盖率收集机制。

2. **动态初始化**：
   - 在嵌入式操作系统的启动代码中，动态调用`pc_trace_guard_init()`函数。这一步是关键，因为嵌入式操作系统可能使用高度定制的启动过程，这可能不触发静态初始化函数。
   - 为了在启动时调用`pc_trace_guard_init()`，Tardis需要定位该函数的地址。这通常是通过反汇编编译后的二进制文件来完成的，以便找到`pc_trace_guard_init()`的确切位置。
   - 使用一个间接调用（例如，通过函数指针）在操作系统启动时执行`pc_trace_guard_init()`，从而初始化覆盖率收集。

3. **分配覆盖率缓冲区**：
   - 在嵌入式操作系统的内存中分配一个专用的覆盖率缓冲区，用于存储执行期间收集的覆盖率数据。
   - 这个缓冲区被设计为在嵌入式操作系统和宿主系统（运行Tardis的系统）之间共享，以便Tardis可以直接访问覆盖率信息。

4. **设置回调函数**：
   - 为每个基本块分配一个唯一的ID，这样`pc_trace_guard()`回调函数就可以在执行到每个基本块时记录其执行情况。
   - 这些ID通过简单的二进制操作（如异或和位移）来计算，以确保覆盖率信息的准确收集。

5. **运行时收集**：
   - 在嵌入式操作系统运行时，每次执行到基本块时，`pc_trace_guard()`回调函数都会被调用，并更新覆盖率缓冲区中的相应条目。

通过这个过程，Tardis能够在嵌入式操作系统上有效地收集覆盖率信息，而无需对每个不同的操作系统进行大量的手动配置或修改。这种自动化的覆盖率初始化机制是Tardis能够在多种嵌入式操作系统上进行有效fuzzing的基础。

====ai generation end=====


### 覆盖率统计

pc_trace_guard()函数。为了效率，统计通过xor来进行。

当前基本块的id xor 前一个被覆盖的基本块的id，可以得到边的id。这样就可以根据边被命中多少次来统计效率。

这个设计真不错。

### coverage analyse

我们希望知道刚刚生成的输入，是否覆盖了一条更新的路径。而且对于每一个输入，都需要进行比较，因此希望这个比较效率更高一些。

在这一步里面，第一个技术是Host-VM Coverage Buffer: To conduct a high efficient coverage-guided fuzzing, the first and foremost is to have a data buffer that can facilitate the coverage collection, transmission, and analysis.
因为Embedded OS的资源比较有限，所以Coverage Buffer放到host上更好一些。
Suppose we can access certain positions of QEMU’s memory space, we can then access the corresponding position of the target Embedded OS directly on the host side.
shared memory in QEMU
Efficient Analysis in Host: After collecting the coverage information and storing them in a shared buffer, we can now analyze them at the host to identify whether the last execution covers any new path.
在宿主机上进行高效分析：在收集覆盖率信息并存储到共享缓冲区之后，我们现在可以在宿主机上分析它们，以识别最后一次执行是否覆盖了任何新路径。为了实现这一点，我们需要将当前的覆盖率统计与整体覆盖率统计进行比较。然而，覆盖率比较是一个频繁操作，必须在每次输入执行后执行。这样高频且复杂的操作可能会花费大量时间，并显著影响模糊测试的效率。此外，在程序执行期间，某些重复操作，例如递归或迭代，可能会导致特定边的巨大命中计数，这将影响我们对新路径的准确性，从而降低效率。因此，为了减少开销并提高模糊测试效率，我们提议使用一个紧凑的位图来记录全局覆盖率，并通过几个简单的二进制操作来检查新覆盖率。


第二个技术是计算覆盖率的方式：
首先，我们使用一个大小为64 KB的紧凑全局覆盖率位图，这样允许接收端在微秒级别内分析该位图，并且可以轻松地适应宿主机CPU的L2缓存。为了执行二进制操作，我们提议使用一个分类过滤器将边覆盖率转换为二进制形式。我们制作了一个简单的哈希映射来存储每个边的命中计数，以便于后续的二进制操作。
具体来说，由于我们使用char大小来存储每个边的命中计数，所有边的命中计数不会超过256次。此外，每个char有8位，我们将命中计数分类到位级别。最后，当我们在执行后获得覆盖率位图时，我们通过二进制操作将其与全局覆盖率位图进行比较。假设结果不等于零，我们认为一个测试用例触发了新覆盖率。最终，覆盖率位图将与全局覆盖率位图合并。由于上述覆盖率存储被设计为对缓存友好，并且整个比较只涉及简单的二进制操作，因此可以保证分析的效率。



## 5. 实验部分

我们列出以下研究问题，以帮助我们了解Tardis的性能和有效性：
1) RQ1：Tardis是否能够揭示不同嵌入式操作系统中的新漏洞？经过测试，发现了17个previously unknown bugs
2) RQ2：与黑盒模糊测试相比，Tardis的覆盖率指导机制是否有效地实现了更高的代码覆盖率？
3) RQ3：在模糊测试期间，插桩给Tardis带来了哪些开销？

实验环境：
1) UC/OS [13]; 2) FreeRTOS [2]; 3) Rt-Thread [33]; and 4) Zephyr [15]
The experiments were conducted on a Linux server with 64 GB of memory and a 16-core CPU


1. RQ1:是否能发现新的bug？总之是发现了。这一节介绍了具体发现了什么bug，还列了一个表格

2. RQ2:evaluate whether the coverage guidance can assist Tardis in achieving a better code coverage.
为了测试coverage guide的效率，用Tardis和裁剪掉coverage guide的Tardis进行对比。

3. RQ3:编译的时候插入了很多函数，会使得开销变大多少？
- 内存：不同的OS效率不同，大概10%-40%。
- 时间：也是30%左右。具体而言，选择了不同的测试用例，测试插桩前和插桩后的运行时间差。


## 6. DISCUSSTION

这一节主要探讨了Tardis模糊测试工具的一些关键方面和潜在的改进空间。具体内容包括：

====ai generation start=====

1. **可扩展性**（Extensibility）：
   - Tardis主要使用Rust编写，客户端执行程序使用C语言，通过QEMU支持嵌入式操作系统的仿真。这种框架尽量避免了不同嵌入式操作系统目标带来的问题。
   - 讨论了Tardis的性能可能受到的限制，包括QEMU仿真速度可能慢于硬件测试，以及某些硬件仿真（如外围设备）可能在某些架构上不受支持的问题。
   - 为了适配更多的嵌入式操作系统，可以采用动态分析技术，如使用ptrace等操作系统跟踪工具来收集真实的执行跟踪，并从中派生系统调用的详细信息。

2. **Bug检测能力**（Bug Detection Capability）：
   - 尽管Tardis通过覆盖率指导机制能够检测到17个新漏洞，但主要检测的是嵌入式操作系统中无法恢复的错误。
   - 讨论了嵌入式操作系统内部执行状态的频繁检查，以及如何通过QEMU的监控来检测注册表中的沉默数据错误，或者通过静态分析来增强Tardis的bug检测能力。

这一节的内容强调了Tardis在实际应用中的一些局限性，并提出了可能的解决方案和未来的改进方向，以便更好地适应和测试各种嵌入式操作系统。

====ai generation start=====

### 7. RELATED WORK

1. kernel fuzzing相关：

- syzkaller：It proposes to use the system call description as input [29], so it can encode rich semantic information into test cases to maximize the fuzzing efficiency. Healer是自动生成system call description的（也是姜老师组的工作）。HFL[11] 采用symbolic execution来生成高质量输入来触发新的内核代码执行路径。
- GPOS fuzzing：they may find it challenging to port it in Embedded OS fuzzing. Therefore, some works try to extend fuzzing into other operating system types（看不懂，什么意思？）
   - Gustave：（完全看不懂）
   - KAFL：使用Intel-PT来支持coverage-guided fuzzing，在architecture上有限制，再说embedded OS的architecture有好几十种，所以这种方案的（那个词叫什么来着）不够好
   - Rtkaller: 这个开源了，好耶。based on Syzkaller, currently only support rt-Linux fuzzing, can not be adapted to other Embedded OS scenarios。同样是architecture的问题。https://github.com/Rrooach/Rtkaller

2. Instrumentation in Fuzzing：
没有coverage guidedance的fuzz效率比较有限，因此收集coverage非常重要。现有的coverage collection方案：
- SanitizerCoverage：SanitizerCoverage offers function level, basic block level, and edge level coverage information
- AFL-GCC：AFL provides edge level coverage only

3. Main Differences between general purpose OS fuzzing and Embedded OS fuzzing
大多数coverage-guided kernel fuzzer需要比较完整的existing infrastructures, such as standard APIs and uniform memory layouts.但是Embedded OSs可能并不能对fuzzer提供这些支持。Gustave and KAFL that enable coverage-guided fuzzing of certain Embedded OS by heavily modified QEMU and introducing the binary instrumentation，但是这样做开销太大。


### 8. CONCLUSION

In this article, we present Tardis, the first coverage-guided fuzzer that is able to discover bugs in Embedded OS. Tardis proposes a coverage collection mechanism that is able to instrument Embedded OSs and conduct an OS-agnostic coverage collection. The coverage is gathered on-the-fly and stored into a data buffer shared between the host fuzzer and the guest, enabling direct accessing without extra copy. Those inputs trigger new coverage can be detected with an efficient coverage analysis mechanism, thus evolving the whole fuzz campaign.
The evaluation shows that the instrumentation brings averagely 27.05% and 30.55% memory consumption and execution overhead. While it gains an improvement of coverage by 51.32% on average, comparing with the black box fuzzing, which demonstrates the effectiveness of the proposed coverage guidance. Furthermore, we found 17 previously unknown bugs among four Embedded OSs, indicating the bug discovery capability of Tardi