# Hydra：Finding Bugs in File Systems with an Extensible Fuzzing Framework

1. 对文件系统进行fuzz的困难在哪里？

- 现有的基于覆盖率的测试方法，可能很难发掘出有意义的操作序列
- 现有的fuzz反馈基于“崩溃”来回答当前给到的输入，是否会引起bug。但是在文件系统中，可能存在“不符合语义”这种类型的bug，其造成的影响当前并不会发现，而是可能在很久之后才被发现（和第一点也有关。如果我们能够将足够长的操作序列作为输入喂给文件系统，然后在一系列操作之后我们发现触发了bug，1和2问题应该都不存在了。但是现在由于一种没太搞明白的限制，使得当前做不了这么长的操作序列作为输入）（另外，或许这一个思路应该在内核中也同样适用？因为对于内核fuzz，也是只会检查crash，而不会检查不符合语义的情况）

2. Hydra关注的文件系统bug类型
 crash inconsistency, POSIX violations, and file system–specific logic bugs

3. Hydra的贡献总结

- To tackle diverse types of bugs in file systems, we propose to use fuzzing as a one-stop solution that unifies existing and future bug checkers under one umbrella.（问题：除了把很多种现有的checker放在一起之外有没有什么额外工作）
- To show this, we build Hydra, a generic and extensible file system fuzzing framework that provides the supporting services for file system bug hunting so that developers can focus on writing core logic in checking bugs of their own interests. The implementation of Hydra is open sourced at https://github.com/sslab-gatech/hydra. （简而言之：开源了，点赞）
- Leveraging in-house developed and externally available bug checkers, Hydra has discovered 157 new bugs of four different types in various file systems, out of which 125 bugs have been acknowledged and 89 bugs have been fixed, which shows its worth.（确实找到了bug）
- In this work, we extend the conference paper [31] to further discuss the motivation and design in greater detail, include more bugs found from another verified file system, Yxv6, and present in-depth analysis of bugs with test cases.

4. 文件系统的bug分类

Software bugs can be broadly categorized into semantic bugs, memory bugs, and concurrency bugs 

- Crash inconsistency：eXplode [59] and B3 [39]，除此之外几乎没有检测这个的。eXplode需要大量的手工操作来验证，而且在不同的文件系统之间无法复用。B3可用在一个设定的框架内大量生成测试用例，但是超出这个框架的有效测试用例无法生成（不确定，应该是这个意思）
- Specification violation.（给了一个语义不一致导致bug的例子）而且可以用于检测specification violation的工具也很少。虽然有SibylFS，但是 The testing scope of SibylFS is limited to its synthesized test suite, which covers a small fraction of the entire test space.
- Logic bug。 logic bugs are tightly coupled with the specific file system implementation。而且， similar to crash inconsistencies and POSIX violations, most logic bugs simply fail silently。
- Memory error.The most prominent examples are the sanitizer series (i.e., KASan [15], KMSan [16], and UBSan [51]) to address out-of-bound accesses and use-after-free, uninitialized read, and undefined behaviors, respectively.
- Other types of bugs.（看不懂）

5. 现有工作的局限性

Unfortunately, none of them have solved the problem entirely.

- Regression tests.

【AI-start】"Regression tests"（回归测试）是软件测试中的一种方法，旨在确保软件的修改、更新或新功能添加后，原有的功能没有被破坏或产生新的错误。在软件开发过程中，开发人员会对软件进行修改以增加新功能、修复已知问题或优化性能。回归测试就是在这些更改后进行的测试，以验证软件的现有功能是否仍然按预期工作。通过执行回归测试，团队可以发现和修复在修改过程中可能引入的任何问题，确保软件质量并提高用户满意度。这是确保软件稳定性和可靠性的重要步骤。【AI-end】（不懂）

regression tests并不是专注文件系统以上几类bug的方式。而且看样子测试用例是手写的。

- Bug-specific checkers.（这是什么）（举的例子也看不懂）

- Formal verification.（形式化验证）在文件系统领域，形式化验证是非常好用的方法。

6. motivation

总之，这个工作希望自己能够：
(1) definition of a bug and corresponding core checking logic, and
(2) the test case generator and the range of program states covered. 
测试用例both breadth and depth, especially to reach corner cases that cannot be covered by test cases contemplated by a human

With such an explorer, we could 
(1) harvest extensive invariant checks in the codebase to detect file system–specific logic bugs;
(2) improve and complement existing bug detectors (e.g., SibylFS); and more importantly, 
(3) focus on the core bug-hunting logic and totally decouple state exploration, as shown by the improvements of our in-house crash consistency checker, SymC3, over B3 (Section 5.6).

（2.4没看懂想说什么）


7. hydra design

主要流程：

seed是什么：Hydra initiates fuzzing by selecting a seed from the seed pool. A seed is a pack of both a file system image to be mounted and a sequence of syscalls to be executed on the mounted image

seed变异：The input mutator subsequently **mutates either the image or the syscalls or both**, and produces a batch of test cases (Section 3.2)

The test cases are sent to a test case executor that always starts in a clean-slate state, mounts the given image, and executes the syscalls (Section 3.3).

覆盖率记录，反馈：The visited code paths are profiled into a bitmap by the coverage tracker instrumented when compiling the target file system

当产生新的bug时，记录这个bug，并且还能simplify这个bug：a new bug is reported, the test case will be sent to a virtual machine for replay and confirmation.
Hydra also performs syscall sequence minimization to create a simplified test case for the ease of analyzing and fixing the bug (Section 3.6).


### 3.2 input mutator

The input space of a file system consists of two major components: a file system image to mount, and file operations that access, read from, and write to the mounted image.

关于Image mutation：
为什么要对image做mutation：image可能会因为一些物理原因产生损坏而且难以避免，一个文件系统需要能正确处理这种损坏。
完全随机的方式不够高效。考虑到一个文件系统绝大多数是实际存储的数据，只有1%左右的数据是metadata。对于实际存储的数据来说，少量的偏移和损坏并不会造成很大的影响（而且相关技术有很多），再加上大多数文件操作实际上都是在修改metadata，因此hydra确定的策略是对metadata进行修改来生成新的输入。
具体做法是，先把整个image map到内存里，然后找到metadata所在的位置。
找到位置之后，it applies several common mutation strategies [64] (bit flipping, arithmetic operation on random bytes, etc.) to randomly mutate the bytes of the metadata as described in Figure 8.
After mutating the entire metadata blob, Hydra reassembles each metadata block back to its corresponding position inside the memory buffer, which stores the original full-size image. As a result, Hydra obtains a corrupt disk image that partially reflects the consequences of various diskfailure scenarios。这个时候我们很自然就会想到，这一点真的成立吗？具体而言，对于任意一个磁盘状态，真的一定能找到对应的磁盘操作使得磁盘从空的状态变成这个状态吗？——checksum这一段没太看明白具体怎么做到的，但是回答的就是这个问题。作者认为在加入这个机制之后，可以保证在大部分情况下，虽然image是坏掉的，但是的确可以通过某种操作序列得到此状态，也就是可达的。


关于Syscall mutation：
Similar to existing OS fuzzers [20, 26], Hydra mutates syscall sequences in two ways: (1) argument mutation (randomly selecting one of the existing syscalls in the sequence and mutating its argument(s)) and (2) syscall generation (appending a new randomly chosen syscall to the end of the sequence) (Figure 10).
具体而言手工定义了一些规则（回忆一下之前还看过一些自动生成系统调用描述来加速fuzz，To generate mostly valid syscalls that explore deep into file system logic, instead of being early rejected by an error checking routine。或许两者可以结合一下）这里显然是通过手工方式增加的一些约束，有用肯定是有用的，具体多大用不清楚

Exploiting the synergy.
按照特定顺序去调度image和syscall的变异，有一些好处（据说）

Assisting bug checkers（没看懂）


### 3.3 Test Case Executor

executor：the generated test cases are concretely executed on the targeted file system. 
In general, the executor serves as (1) a fuzzing target, which mounts the given image and executes the syscall trace while collecting code coverage, and (2) a bridge to the checker dispatcher (Section 3.4), which calls a checker, collects results, and then provides an additional dimension of feedbacks to the feedback engine (Section 3.5). 

Hydra supports both inkernel file systems (e.g., ext4), and FUSE (Filesystem in Userspace) file systems (e.g., FSCQ) for performance.

因为基于Lib-OS的 executor可以以很快的方式forks a fresh instance of the executor for every test case

基于FUSE的executor，因为我们实际上可以把FUSE看成一个用户态进程，所以它同样可以以比较低的代价跑很多个test case，方便fuzz

（注意：fuzz必须考虑性能问题，因为需要起很多个instance）


### 3.4 Checker Dispatcher

checker despathcer是什么：（不想读了，让AI帮我看看吧）

【AI-start】

3.4节的“Checker Dispatcher”部分主要介绍了Hydra框架中的检查器调度器（Checker Dispatcher）的功能和作用。这一部分内容的核心要点如下：

1. **检查器调度器的作用**：检查器调度器是Hydra框架的一个关键组件，它负责启动与目标错误类型相对应的检查器插件。这些检查器插件可以针对不同类型的文件系统错误进行检测。

2. **统一接口**：尽管可以插入任何类型的漏洞检查器到Hydra中，但这些检查器可能有不同的接口。例如，SibylFS作为一个POSIX合规性检查器，是一个独立的二进制文件，它接受特定格式的测试用例，这与Hydra的输入变异器生成的测试用例不同。而KASan则是集成到内核中的，可以通过编译内核时配置一个标志来启用。Hydra的检查器调度器考虑到这些差异，并提供了一个统一的接口，抽象了测试用例如何被不同检查器消费，以及测试结果如何从检查器转移出来。

3. **检查器的集成**：为了使新检查器的集成尽可能简单，Hydra提供了一个API，帮助开发者编写与Hydra兼容的检查器。这一部分讨论了如何将内部开发的检查器SymC3和其他检查器集成到Hydra中，以暴露各种类型的文件系统错误。

4. **检查器的例子**：文中提到了几个具体的检查器例子，包括SymC3（一个内部开发的崩溃一致性检查器）、SibylFS（一个POSIX合规性检查器）和KASan（一个内存错误检查器）。

总结来说，3.4节描述了Hydra框架中用于管理和调度不同检查器的组件，这些检查器用于发现和验证文件系统中的错误。通过提供一个统一的接口和API，Hydra能够灵活地集成多种检查器，从而发现各种类型的文件系统错误。从而发现各种类型的文件系统错误。



3.5节的“Feedback Engine”部分主要讨论了Hydra框架中的反馈引擎，它的作用是衡量测试用例的“新颖性”并决定是否值得进一步变异。这一部分内容的核心要点如下：

1. **反馈类型**：Hydra的反馈引擎考虑两种类型的反馈：分支覆盖率和检查器定义的信号。分支覆盖率是传统fuzzer中常用的一种反馈，它通过追踪测试用例执行过程中访问的代码分支来衡量新颖性。而检查器定义的信号则允许每个检查器注册自己的反馈格式，这可以是一个简单的布尔变量，表示测试用例是否触发了错误条件。

2. **分支覆盖率**：Hydra使用控制流图（CFG）来表示文件系统，其中顶点是基本块，边是从一块到另一块的分支。执行测试用例时，Hydra跟踪访问的边集合，并根据触发的新分支数量和独特分支组合来衡量测试用例的新颖性。

3. **检查器反馈**：作为一个通用的fuzzing框架，Hydra允许每个检查器注册自己的反馈格式。例如，一个旨在揭示规范违规的检查器可能会提供一个跟踪已断言规则数量的反馈格式，这将惩罚那些生成已断言部分的测试用例的输入变异器，并最终推动Hydra朝着尚未测试的规范部分发展。

4. **反馈引擎的作用**：反馈引擎通过衡量测试用例的新颖性来指导输入变异器的搜索方向。如果一个测试用例报告了新的覆盖率或被检查器标记为有趣，那么它将被保存到种子池中，并期望沿着这个方向进行更多的探索；否则，测试用例将被丢弃。

总结来说，3.5节描述了Hydra框架中反馈引擎的工作原理和作用，它通过分析测试用例的执行结果来提供反馈，这些反馈用于指导输入变异器的搜索策略，以更有效地发现文件系统中的错误。通过这种方式，Hydra能够专注于探索那些可能会触发检查器定义的错误状态的输入空间。


【AI-end】

（一些评论）
fuzz需要对被测试的系统有足够多的了解才能做，而且这个具体的方法会根据被测试系统的不同而有很大的不同。
不过尽管如此，fuzz方法层面还是有一些共同的地方。



# Hydra：Finding Bugs in File Systems with an Extensible Fuzzing Framework

Hydra Introduction

The article introduces Hydra, an extensible fuzzing framework developed by researchers at the Georgia Institute of Technology. Hydra is designed to find bugs in file systems, which are notoriously difficult to keep bug-free due to their size and complexity. Traditional testing methods, such as handwritten test suites, struggle to keep up with the rapid growth of file system code, leading to the introduction of new bugs. These can range from buffer overflows to complex semantic errors.

Hydra addresses these challenges by providing a generic way to apply fuzzing techniques to uncover a wide variety of file system bugs. The framework includes several components:

1. **Input Mutators**: To generate diverse and complex test inputs.
2. **Feedback Engines**: To guide the fuzzing process towards more effective test cases.
3. **Test Executors**: To run tests in a clean environment and ensure reproducibility.
4. **Bug Post-Processors**: To handle the results and identify actual bugs.

The framework is extensible, allowing developers to focus on creating core logic for specific types of bugs while Hydra handles the exploration of file system states. The article showcases Hydra's effectiveness with four types of checkers designed to find crash inconsistencies, POSIX violations, logic assertion failures, and memory errors. Notably, Hydra has discovered 157 new bugs in Linux file systems, including some in verified file systems like FSCQ and Yxv6.

Hydra's approach is significant because it unifies the checking effort for various aspects of a file system under one umbrella, where no turnkey solution existed before. The framework's design allows for a separation of concerns, enabling developers to concentrate on bug detection logic while Hydra automates the input exploration, checker incorporation, and validation of found bugs. This separation is shown to improve the accuracy and efficiency of bug detection.

The article also discusses the implementation details of Hydra, its integration with existing tools like SibylFS and KASan, and the results of evaluating Hydra against other state-of-the-art fuzzers like Syzkaller and kAFL. Hydra outperforms these tools in terms of code coverage and speed, and it has been successfully used to find and report bugs in real-world file systems.

In conclusion, Hydra represents an important advancement in the field of software testing, particularly for complex systems like file systems. Its extensible and automated approach to fuzzing has the potential to significantly improve the quality and reliability of such systems.