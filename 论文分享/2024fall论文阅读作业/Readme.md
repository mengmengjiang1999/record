
讲遗下4篇论文：

1. SoK-Attacks on Industrial Control Logic and Formal Verification-Based Defenses
第一篇文章介绍PLC面临的安全威胁，以及形式化验证的方法和局限。

2. Fuzzware: Using Precise MMIO Modeling for Effective Firmware Fuzzing

第二篇文章介绍了对MMIO进行自动化建模的方法
MMIO（Memory-Mapped I/O）建模是指在软件仿真环境中对硬件的内存映射输入/输出设备进行模拟的过程。内存映射输入/输出是一种在嵌入式系统和某些计算机体系结构中常用的技术，其中硬件设备（如串口、定时器、网络接口等）的寄存器被映射到处理器的内存空间中。这样，软件可以通过读写这些内存地址来直接与硬件设备通信。
在Fuzzware的上下文中，对MMIO进行建模是为了有效地进行固件的模糊测试。由于直接在嵌入式硬件上进行模糊测试通常是不可行的，或者效率非常低，因此Fuzzware采用了重新托管（re-hosting）的方法，即在仿真环境中运行固件。为了使固件能够在这种环境中正常运行，需要对它所依赖的硬件行为进行建模，特别是那些通过MMIO访问的硬件寄存器的行为。




3. From Library Portability to Para-rehosting: Natively Executing Microcontroller Software on Commodity Hardware

4. HALucinator: Firmware Re-hosting Through Abstraction Layer Emulation
第四篇文章介绍了一种新的方法，即通过抽象层模拟（ALM）来实现固件的重新托管。ALM是一种基于抽象机理的模拟技术，它可以将复杂的硬件行为简化为一个抽象层，并将其映射到软件模型中。通过ALM，可以将复杂的硬件行为简化为一个抽象层，并将其映射到软件模型中。这样，就可以在软件模型中模拟复杂的硬件行为，从而实现固件的重新托管。