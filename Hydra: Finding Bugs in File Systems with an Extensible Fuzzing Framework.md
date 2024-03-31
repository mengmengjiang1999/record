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

总之，这个工作希望自己能够：(1) definition of a bug and corresponding core checking logic, and (2) the test case generator and the range of program states covered. 
测试用例both breadth and depth, especially to reach corner cases that cannot be covered by test cases contemplated by a human

With such an explorer, we could (1) harvest extensive invariant checks in the codebase to detect file system–specific logic bugs; (2) improve and complement existing bug detectors (e.g., SibylFS); and more importantly, (3) focus on the core bug-hunting logic and totally decouple state exploration, as shown by the improvements of our in-house crash consistency checker, SymC3, over B3 (Section 5.6).

（2.4没看懂想说什么）


7. hydra design

主要流程：

seed是什么：Hydra initiates fuzzing by selecting a seed from the seed pool. A seed is a pack of both a file system image to be mounted and a sequence of syscalls to be executed on the mounted image

seed变异：The input mutator subsequently **mutates either the image or the syscalls or both**, and produces a batch of test cases (Section 3.2)

The test cases are sent to a test case executor that always starts in a clean-slate state, mounts the given image, and executes the syscalls (Section 3.3).

覆盖率记录，反馈：The visited code paths are profiled into a bitmap by the coverage tracker instrumented when compiling the target file system

当产生新的bug时，记录这个bug，并且还能simplify这个bug：a new bug is reported, the test case will be sent to a virtual machine for replay and confirmation.
Hydra also performs syscall sequence minimization to create a simplified test case for the ease of analyzing and fixing the bug (Section 3.6).


### input mutator

The input space of a file system consists of two major components: a file system image to mount, and file operations that access, read from, and write to the mounted image.

关于Image mutation：
为什么要对image做mutation：image可能会因为一些物理原因产生损坏而且难以避免，一个文件系统需要能正确处理这种损坏。
完全随机的方式不够高效。考虑到一个文件系统绝大多数是实际存储的数据，只有1%左右的数据是metadata。对于实际存储的数据来说，少量的偏移和损坏并不会造成很大的影响（而且相关技术有很多），再加上大多数文件操作实际上都是在修改metadata，因此hydra确定的策略是对metadata进行修改来生成新的输入。
具体做法是，先把整个image map到内存里，然后找到metadata所在的位置。
找到位置之后，it applies several common mutation strategies [64] (bit flipping, arithmetic operation on random bytes, etc.) to randomly mutate the bytes of the metadata as described in Figure 8.
