# Fuzzware: Using Precise MMIO Modeling for Effective Firmware Fuzzing
Authors: 
Tobias Scharnowski, Nils Bars, and Moritz Schloegel, Ruhr-Universität Bochum; Eric Gustafson, UC Santa Barbara; Marius Muench, Vrije Universiteit Amsterdam; Giovanni Vigna, UC Santa Barbara and VMware; Christopher Kruegel, UC Santa Barbara; Thorsten Holz and Ali Abbasi, Ruhr-Universität Bochum

Distinguished Artifact Award Winner

Abstract: 
As embedded devices are becoming more pervasive in our everyday lives, they turn into an attractive target for adversaries. Despite their high value and large attack surface, applying automated testing techniques such as fuzzing is not straightforward for such devices. As fuzz testing firmware on constrained embedded devices is inefficient, state-of-the-art approaches instead opt to run the firmware in an emulator (through a process called re-hosting). However, existing approaches either use coarse-grained static models of hardware behavior or require manual effort to re-host the firmware.

We propose a novel combination of lightweight program analysis, re-hosting, and fuzz testing to tackle these challenges. We present the design and implementation of Fuzzware, a software-only system to fuzz test unmodified monolithic firmware in a scalable way. By determining how hardware-generated values are actually used by the firmware logic, Fuzzware can automatically generate models that help focusing the fuzzing process on mutating the inputs that matter, which drastically improves its effectiveness.

We evaluate our approach on synthetic and real-world targets comprising a total of 19 hardware platforms and 77 firmware images. Compared to state-of-the-art work, Fuzzware achieves up to 3.25 times the code coverage and our modeling approach reduces the size of the input space by up to 95.5%. The synthetic samples contain 66 unit tests for various hardware interactions, and we find that our approach is the first generic re-hosting solution to automatically pass all of them. Fuzzware discovered 15 completely new bugs including bugs in targets which were previously analyzed by other works; a total of 12 CVEs were assigned.

简而言之是对MMIO进行自动化建模的工作


MMIO（Memory-Mapped I/O）建模是指在软件仿真环境中对硬件的内存映射输入/输出设备进行模拟的过程。内存映射输入/输出是一种在嵌入式系统和某些计算机体系结构中常用的技术，其中硬件设备（如串口、定时器、网络接口等）的寄存器被映射到处理器的内存空间中。这样，软件可以通过读写这些内存地址来直接与硬件设备通信。

在Fuzzware的上下文中，对MMIO进行建模是为了有效地进行固件的模糊测试。由于直接在嵌入式硬件上进行模糊测试通常是不可行的，或者效率非常低，因此Fuzzware采用了重新托管（re-hosting）的方法，即在仿真环境中运行固件。为了使固件能够在这种环境中正常运行，需要对它所依赖的硬件行为进行建模，特别是那些通过MMIO访问的硬件寄存器的行为。

Fuzzware的MMIO建模包括以下几个关键步骤：

1. **确定固件逻辑如何使用硬件生成的值**：Fuzzware通过分析固件的执行来确定哪些硬件生成的值是固件逻辑所依赖的。

2. **自动生成模型**：基于上述分析，Fuzzware自动创建模型，这些模型定义了固件如何解释从MMIO寄存器中读取的值。

3. **减少输入空间**：通过识别固件实际上使用的输入部分，Fuzzware可以减少模糊测试中需要考虑的输入空间，从而提高测试的效率。

4. **配置仿真器**：生成的模型被用来配置仿真器，以便在固件执行期间提供正确的硬件生成值。

5. **模糊测试**：在仿真环境中，模糊测试工具（fuzzer）使用这些模型来生成和变异输入，以测试固件的不同执行路径。

通过这种方式，Fuzzware能够在不需要具体硬件的情况下，有效地对固件进行模糊测试，识别潜在的安全漏洞。这种方法特别适用于单体固件（monolithic firmware），即没有传统操作系统支持的单一二进制文件。
