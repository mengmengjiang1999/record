# Armor PLC: A Platform for Cyber Security Threats Assessments for PLCs

https://www.sciencedirect.com/science/article/pii/S2351978920304017

@article{armorplc,
title = {Armor PLC: A Platform for Cyber Security Threats Assessments for PLCs},
journal = {Procedia Manufacturing},
volume = {39},
pages = {270-278},
year = {2019},
note = {25th International Conference on Production Research Manufacturing Innovation: Cyber Physical Manufacturing August 9-14, 2019 | Chicago, Illinois (USA)},
issn = {2351-9789},
doi = {https://doi.org/10.1016/j.promfg.2020.01.334},
url = {https://www.sciencedirect.com/science/article/pii/S2351978920304017},
author = {Wenhui Zhang and Yizheng Jiao and Dazhong Wu and Srivatsa Srinivasa and Asmit De and Swaroop Ghosh and Peng Liu},
keywords = {Programmable Logic Controllers, Stateless Host Based Intrusion Detection, Record, Replay, Internet of Things, Byzantine Scheme, Overlayed Network},
abstract = {Programmable Logic Controllers (PLCs) are essential parts in industrial manufacturing plants. With the emerging Industry 4.0 environment, legacy PLCs are now connected to the Internet to be better automated. However, these PLCs are especially vulnerable when connected to a network, since there is limited inherent security mechanisms built in. In this paper, we discuss various vulnerabilities in these PLCs. We describe threat models, detection and protection techniques. We consider vulnerabilities as compromised PLC logic, which is introduced by over-the-network malicious data injection. We leverage Host-Based Intrusion Detection System (HIDS) techniques, such as output value comparison using majority voting, timing comparison and using known I/O values for detecting such attacks for our Network-Based Intrusion Detection System for PLCs. We mimic functionalities of PLCs, through virtualization of PLCs’ ladder logic on OpenPLC [7]. We use a record & replay technique for attack mitigation and system restoration. The record & replay system captures pin values of a Pulse Width Modulated (PWM) signal with sensitivity of 50 microseconds. We implement the attacks and our proposed security solution on the control flow logic of a sample industrial gas pipeline PLC network. We achieve a false positive rate of 1% along with a latency of 25 milliseconds in our abnormal detection with setting of 4 virtual PLCs (using OpenPLC [7]), and generated receiver operating characteristic results on different attack rates and ST file logic settings.}
}

主要是针对网络攻击的攻击和防御。


这篇文章的主要工作是提出并实现一套针对工业制造中使用的可编程逻辑控制器（PLCs）的网络安全威胁评估和保护措施。具体来说，文章的主要工作包括以下几个方面：

1. **威胁和漏洞评估**：对PLC系统中存在的各种潜在威胁和漏洞进行了分类和评估，包括配置文件漏洞、网络漏洞、操作系统漏洞以及物理I/O接口的漏洞。

2. **攻击模型**：基于上述漏洞分类，定义了五种不同的威胁模型，包括对PLC配置、操作系统、用户空间程序的黑客攻击，以及监控数据和配置的被动攻击和返回导向编程攻击。

3. **安全架构和系统设计**：提出了一个安全的网络和系统架构，使用树莓派（Raspberry Pi）运行OpenPLC来模拟多个虚拟PLCs，这些虚拟PLCs与物理PLCs在同一网络中，提供冗余并帮助监控潜在的入侵。

4. **入侵检测技术**：开发了三种基于集中式异常检测（CCAD）的检测技术，包括输出值配置比较、已知输入/输出验证控制逻辑和计时比较。

5. **缓解技术：记录和重放**：设计了一种基于记录和重放的缓解机制，包括捕获阶段（记录引脚状态）、通信阶段（多层管理）和控制阶段（引脚状态重放）。

6. **实验评估**：在树莓派平台上构建的虚拟PLCs测试床上对所提出的技术进行了性能评估，包括误报率、系统延迟和输入/输出频率的灵敏度。

7. **结果和讨论**：展示了检测和缓解技术对攻击场景的效果，并讨论了这些技术的有效性和局限性。

文章的目标是通过这些工作，提高工业4.0环境下PLCs的网络安全性，保护智能制造系统免受各种网络攻击的威胁。



目前PLC存在的漏洞：

在文章的“Vulnerabilities in PLC Ecosystem”（PLC生态系统中的漏洞）部分，作者详细讨论了PLC系统中存在的各种潜在威胁和漏洞，并根据这些威胁的特点进行了分类。以下是这部分内容的总结：

1. **配置中的漏洞（Vulnerabilities in configuration）**：
   - PLC中的配置文件通常以明文形式存储，攻击者可以通过在梯形逻辑中引入恶意逻辑来配置PLC，从而操纵提供给SCADA系统的传感器数据。

2. **网络中的漏洞（Vulnerabilities in network）**：
   - 研究中的PLC集成在Raspberry Pi中，容易暴露在恶意通信渠道中。在PLC网络中，一个被感染的PLC会扫描网络寻找新目标（本研究中的PLC），并感染这些新目标。

3. **操作系统中的漏洞（Vulnerabilities in operating system）**：
   - Raspberry Pi（RPI）是一个Linux发行版，包含许多可以被RPI继承的漏洞。由于Linux代码不是类型安全的，因此容易受到各种缓冲区溢出攻击。

4. **引脚I/O中的漏洞（Vulnerabilities in Pin I/O）**：
   - PLC不会对从引脚I/O发送的命令和控制信号进行消毒，因此容易受到无效输入攻击。

5. **PLC生态系统中的威胁（Threats in PLC Ecosystem）**：
   - 基于上述漏洞分类，作者定义了五种不同的威胁模型：
     - **黑客攻击PLC配置（Hacking PLC Configuration）**：攻击者一旦登录到RPI，就可以更改配置文件。
     - **黑客攻击操作系统（Hacking OS）**：默认情况下，Raspberry Pi给予用户root访问权限，Linux系统默认打开SSH端口，可能允许恶意来源远程控制RPI。
     - **修改用户空间程序（Modifying the User Space Programs）**：攻击者一旦登录到RPI，就可能更改虚拟OpenPLC程序。
     - **监控引脚/数据/配置（Monitoring Pin/Data/Configuration）**：有访问权限的用户可以通过监控RPI上的输入/输出引脚的数据流量模式，预测处理的数据，这可能损害PLC数据的机密性。
     - **返回导向编程攻击（Return Oriented Programming Attack）**：PLC逻辑可能被破坏，破坏后的逻辑会使设备操作偏离正常执行路径。

这部分内容强调了PLC系统在设计和实施过程中可能面临的安全风险，并为后续提出的检测和缓解技术提供了基础。


做的实验大概就是触发了一个拜占庭故障。


