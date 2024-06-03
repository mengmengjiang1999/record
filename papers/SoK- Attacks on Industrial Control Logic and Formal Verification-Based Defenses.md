# SoK- Attacks on Industrial Control Logic and Formal Verification-Based Defenses

PLC的形式化验证综述，主要关注的是控制逻辑的形式化证明。

这篇文章里面主要有贡献的点在于：

1. 将PLC控制逻辑分为三个不同的层面。

T1: program source code.
T2: program bytecode/binary. 
T3: program runtime.

2. 将安全威胁也分为三个层面：

T1: In this threat model, attackers assume accesses to the program source code, developed in one of the languages described in Section 2.1.1. Attackers generate attacks by directly mod- ifying the source code. Such attacks happen in the en- gineering station as step ⃝1 in Figure 3. Attackers can be internal staffs who have accesses to the engineering station, or can leverage vulnerabilities of the engineering station [1], [50], [51] to access it.
T2: In this threat model, attackers have no access to program source code but can access program bytecode or binary. Attackers generate attacks by first reverse en- gineering the program bytecode/binary, then modifying the decompiled code, and finally recompiling it. Such attacks happen during the bytecode/binary transmission from the engineering station to the PLC (⃝2 in Figure 3). Attackers can intercept and modify the transmission leveraging vulnerabilities in the network communication [48], [49], [52] .
T3: In this threat model, attackers have no access to program source code nor bytecode/binary. Instead, attack- ers can guess/speculate the logic of the control program by accessing the program runtime environment, including the PLC firmware, hardware, or/and Input and Output
traces. Attackers can modify the real-time sensor input to the program (⃝3 in Figure 3). Such attacks are practical since within the same domain, the general settings of the infrastructure layout are similar, and infrastructures (e.g. traffic lights) can be publicly accessible [3], [43], [69].


3. 主要讨论形式化验证的问题

如果只考虑program source code那么形式化验证相对是好做的，目前已有一些工作可以输出一个program code，输出一个验证结果。

但是问题在于PLC是和传感器等工厂的真实设备打交道的，IO什么的对PLC的控制逻辑影响很大。那么就不得不考虑外设的问题了。目前已有研究提出，希望将工厂模型也考虑在形式化验证的框架内（具体我也不是特别懂）

