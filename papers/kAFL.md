

the fuzzing logic, the VM infrastructure (modified versions of QEMU and KVM denoted by QEMU-PT and KVMPT), and the user mode agent.


fuzzing的流程：

1. When the VM is started, the first part of the user mode agent (the loader) uses the hypercall HC_SUBMIT_PANIC to submit the address of the kernel panic handler (or the BugCheck kernel address in Windows) to QEMU-PT

先把kernel panic handler address想个办法让QEMU-PT知道，然后QEMU-PT就会在panic handler的位置 patch一个处理流程。

2. vm-ring3的loader会再次调用一个hypercall，调用usermode agent。

（不想读了）

总之，概括一下就是：
整个fuzzing分为三部分。（下面部分为AI生成，但是初步核对了一下这个流程没问题）

kAFL的三个主要组成部分各自负责不同的任务，并且它们运行在不同的模式下：

1. **模糊测试逻辑 (Fuzzing Logic)**：
   - **任务**：这是kAFL的核心组件，负责管理待处理的输入队列，创建变异输入，并安排它们进行评估。它使用位图来追踪基本块的转换，以确定哪些输入触发了新的行为。此外，它还负责并行地协调多个虚拟机的运行。
   - **运行模式**：模糊测试逻辑作为一个用户空间进程（ring 3）在宿主机操作系统上运行。

2. **用户模式代理 (User Mode Agent)**：
   - **任务**：这个组件负责在目标操作系统的用户空间内同步和收集由模糊测试逻辑提供的输入，并将这些输入用于与操作系统内核的交互。例如，它可能会尝试将输入作为文件系统映像挂载，或者将特定的文件传递给内核解析器。
   - **运行模式**：用户模式代理同样在目标操作系统的用户空间（ring 3）中运行。

3. **虚拟机基础设施 (VM Infrastructure)**：
   - **任务**：由修改过的QEMU（QEMU-PT）和KVM（KVM-PT）组成，负责创建和控制目标操作系统的虚拟机实例。QEMU-PT与KVM-PT协作，允许模糊测试逻辑配置和切换Intel PT，以及访问输出缓冲区来解码跟踪数据，从而获取代码执行的反馈信息。
   - **运行模式**：虚拟机基础设施的QEMU-PT部分运行在宿主机的用户空间（ring 3），而KVM-PT作为内核模块运行在宿主机的内核空间（ring 0）。

这三个组件共同工作，利用硬件辅助的反馈机制，以独立于操作系统的方式进行高效的模糊测试。通过这种分工合作，kAFL能够对操作系统内核进行深入的自动化测试，以发现潜在的安全漏洞。

至于具体的fuzzing流程，简而言之看懂了以下几点：

1. 位于VM-ring3的user agent通过hypercall来和fuzzer要输入，然后喂给target
2. 



### evaluation部分

在文档中，kAFL和TriforceAFL之间的对比主要关注于它们的执行速度、代码覆盖率以及在模糊测试过程中的性能。以下是对比的主要结论：

1. **执行速度**：
   - kAFL在执行速度上提供了比TriforceAFL更好的性能。在进行相同的模糊测试任务时，kAFL能够以更高的速率执行测试用例。

2. **代码覆盖率**：
   - kAFL能够更快地发现新的执行路径，这意味着它能够更有效地探索目标系统的代码覆盖率。文档中提到的一个例子是，kAFL在不到3分钟的时间内就找到了与TriforceAFL在30分钟内找到的相同数量的路径。

3. **性能比较**：
   - 在对JSON样本驱动程序的模糊测试性能进行比较时，kAFL在不同的操作系统上显示出了相似的性能，并且在并行处理方面表现更好。

4. **原始执行性能**：
   - 在避免由于执行不同路径、非确定性过滤器的采样过程以及各种同步机制带来的偏差的情况下，kAFL在原始执行性能方面比TriforceAFL快多达54倍。

5. **系统兼容性**：
   - TriforceAFL由于其基于QEMU的仿真后端，无法模糊测试闭源操作系统，如Windows和macOS。而kAFL由于使用了硬件辅助虚拟化和Intel PT，能够测试包括闭源操作系统在内的各种目标系统。

6. **CPU仿真与硬件辅助虚拟化**：
   - TriforceAFL依赖于QEMU的CPU仿真来执行目标代码，这在性能上不如kAFL所采用的硬件辅助虚拟化技术。

7. **解码器性能**：
   - kAFL使用的PT解码器在性能上超越了TriforceAFL所使用的解码器，特别是在处理大量跟踪数据时，kAFL的解码器能够更快速地完成任务。

综上所述，kAFL在执行速度、代码覆盖率和整体性能方面相较于TriforceAFL展现出了显著的优势。kAFL的硬件辅助方法使其更适合于现代的处理器架构，并且在测试闭源操作系统时更加有效。这些结论表明kAFL是一个强大的工具，能够用于自动化和全面地发现操作系统内核中的漏洞。


syzkaller不能直接进行对比，因为syzkaller某种程度上来说并不依赖覆盖率反馈机制也可以正常work，此外syzkaller只能fuzzing syscall，不能用来