# SoK-Attacks on Industrial Control Logic and Formal Verification-Based Defenses

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


摘要中提到了以下问题：

1. **PLC的重要性和脆弱性**：可编程逻辑控制器（PLCs）在工业控制系统中扮演着关键角色。PLC程序中的漏洞可能导致对关键基础设施的攻击，造成毁灭性后果，如Stuxnet等类似攻击所示。

2. **PLC控制逻辑漏洞的增长**：近年来，报告的PLC控制逻辑漏洞呈指数级增长。

3. **控制逻辑修改攻击和形式验证研究**：过去的研究广泛探索了控制逻辑修改攻击以及基于形式验证的安全解决方案。

4. **系统化研究的发现**：通过对这些研究进行系统化分析，作者发现存在可以破坏整个控制链并逃避检测的攻击。

5. **形式验证研究的局限性**：大多数形式验证研究调查了针对PLC程序的特定技术。作者发现了形式验证各个方面的挑战，这些挑战源于以下因素：
   - (1) 系统设计演变带来的不断扩大的攻击面；
   - (2) 程序执行期间的实时约束；
   - (3) 由于专有和厂商特定依赖不同技术而带来的安全评估障碍。

6. **未来研究方向的建议**：基于知识系统化，作者为未来的研究方向提供了一系列建议，并强调除了安全问题外，还需要防御安全问题。

7. **关键词**：PLC、攻击、形式验证。

摘要强调了PLC在工业控制系统中的重要性，以及由于PLC程序漏洞带来的安全风险，同时指出了形式验证在防御这些攻击中的潜力和挑战，并为未来的研究提供了方向。
