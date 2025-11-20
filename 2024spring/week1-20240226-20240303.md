# 2024spring week1 

20240226-20240303

对内核fuzz相关工作的调研

1. FuzzOS

https://gamozolabs.github.io/fuzzing/2020/12/06/fuzzos.html

专门为了Fuzz设计的OS。
UEFI kernel。ACPI table parsers。multiple cores。10gbit network drivers。

every single core on the system running it’s own address space。
linear scaling will be required
MMU

2. Gustave：针对嵌入式内核的fuzz工具

3. Healer
基于syzkaller的fuzz工具。会研究syscall序列对结果的影响。

4. FISY
UNIX systems with a strong focus on BSD systems.


5. StateFuzz
用来fuzz驱动的


6. TSFFS 看起来很厉害

文档摘要：

TSFFS is focused on several primary use cases:

UEFI and BIOS code, particulary based on EDKII
Pre- and early-silicon firmware and device drivers
Hardware-dependent kernel and firmware code
Fuzzing for complex error conditions
However, TSFFS is also capable of fuzzing:

Kernel & kernel drivers
User-space applications
Network applications


