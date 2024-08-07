# IEC 61850 Compatible OpenPLC for Cyber Attack Case Studies on Smart Substation Systems


https://ieeexplore.ieee.org/abstract/document/9684382/


OpenPLC本身不支持IEC 61850标准，而这个标准在智能电网中应用非常广泛。因此，本工作对OpenPLC进行了一定的扩展，使得其支持IEC 61850标准。

做的实验是应用于变电站，并且展示了对于攻击的防御效果。

这篇论文的主题是关于一种与IEC 61850标准兼容的OpenPLC在智能变电站系统的网络攻击案例研究。IEC 61850是智能电网系统中变电站自动化的全球采用标准。OpenPLC是一个广泛使用的软件，用于模拟PLC（可编程逻辑控制器）的功能，但它原本不支持IEC 61850标准。因此，论文讨论了对OpenPLC进行增强以支持IEC 61850协议和信息模型，并验证了其在智能电网范例中的应用性能。

主要内容包括：

1. **背景介绍**：PLC在工业控制系统中的作用，特别是在现代化电网系统中实现自动化控制的重要性。IEC 61850标准在变电站自动化中的地位。

2. **OpenPLC的局限性**：OpenPLC虽然被广泛用于模拟PLC，但它最初不支持IEC 61850标准，这限制了它在现代智能电网系统模拟中的应用。

3. **OpenPLC61850的开发**：作者提出了一个增强版本的OpenPLC，名为OpenPLC61850，以支持IEC 61850标准。这个项目已经作为开源项目发布，供研究和工业界使用。

4. **性能评估**：对OpenPLC61850的性能进行了评估，包括计算负担和处理IEC 61850 MMS（制造消息规范）消息的能力。

5. **网络攻击案例研究**：使用OpenPLC61850展示了针对PLC的网络攻击场景，如虚假数据注入（FDI）和虚假命令注入（FCI）攻击，并评估了安全措施的有效性和PLC控制逻辑的健壮性。

6. **系统设计和威胁模型**：论文提出了一个智能变电站的系统模型，并讨论了网络攻击可能带来的威胁。

7. **结论**：总结了OpenPLC61850的开发目的，展示了其在网络攻击测试平台中的用途，并提出了未来的研究方向，包括支持IEC 61850标准定义的其他协议（如GOOSE和SV）以及根据IEC 62351标准提供网络安全措施。

论文强调了网络安全在现代智能电网系统中的重要性，并提供了一个开源工具来帮助研究者和工程师评估和提高系统的安全性。