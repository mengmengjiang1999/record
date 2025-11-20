# OpenPLC: An Open Source Alternative to Automation
https://ieeexplore.ieee.org/abstract/document/6970342/authors#authors

@INPROCEEDINGS{openplc,
  author={Alves, Thiago Rodrigues and Buratto, Mario and de Souza, Flavio Mauricio and Rodrigues, Thelma Virginia},
  booktitle={IEEE Global Humanitarian Technology Conference (GHTC 2014)}, 
  title={OpenPLC: An open source alternative to automation}, 
  year={2014},
  volume={},
  number={},
  pages={585-589},
  keywords={Central Processing Unit;Automation;Protocols;Software;Relays;Floors;Light emitting diodes;PLC;OpenPLC;Automation;MODBUS;Open source},
  doi={10.1109/GHTC.2014.6970342}}


重点：

1. 鲁棒性设计

作为PLC最重要的特性之一是其鲁棒性，因此每个模块都必须设计有诸如短路、过电流和过电压保护等防护措施。同样重要的是，还需要包括针对射频噪声的滤波器。

含义解释：

这段话强调了PLC（可编程逻辑控制器）设计中的一个关键方面——鲁棒性。鲁棒性是指系统在面对异常情况或不利条件时仍能正常工作的能力。在工业环境中，PLC需要能够承受各种电气故障和干扰，因此其设计必须包含多种保护机制，以确保系统的稳定性和可靠性。

1. **短路保护**：当电路中出现意外的直接电气连接，导致电流急剧增加时，短路保护能够防止设备损坏或安全事故。

2. **过电流保护**：也称为过载保护，防止电流超过设备的安全工作范围，这可能会由于机械故障或过载条件引起。

3. **过电压保护**：防止电压突然升高到可能损害PLC组件的水平。

4. **射频噪声滤波**：射频干扰（RFI）可能来自无线电传输或其他电子设备，这些干扰可能会影响PLC的信号完整性和控制精度。通过滤波器可以减少这些噪声对PLC操作的影响。

结合上下文，文章在讨论OpenPLC硬件架构时提到了这些保护措施。OpenPLC作为一个开源的PLC解决方案，旨在提供与工业标准相当的功能，包括必要的电气保护和抗干扰能力。这表明OpenPLC的设计考虑了工业环境中的实际需求，以确保其在恶劣条件下也能可靠地执行其控制任务。通过实现这些保护功能，OpenPLC能够提高其在各种工业应用中的适用性和实用性。



2. PLC的执行逻辑


Every rung in the ladder logic represents a rule to the program. When implemented with relays and other electromechanical devices, all the rules execute simultaneously. However, when the diagram is implemented in software using a PLC, every rung is processed sequentially in a continuous loop (scan). The scan is composed of three phases: 1) reading inputs, 2) processing ladder rungs, 3) activating outputs. To achieve the effect of simultaneous and immediate execution, outputs are all toggled at the same time at the end of the scan cycle.

大概意思就是每个scan cycle会接受一些输入，然后按照一定顺序执行逻辑，然后给出输出。

3. 关于OpenPLC是怎么做的

这个问题实话说我不是特别关注···反正知道它很厉害就对了。能实现的功能就是本来PLC需要用专门的语言去写，但是有了openPLC，就只要用C或者C++来写就好了

4. 实验部分

实验做的事情是，这个OpenPLC和原始PLC进行对比

实验部分采用的方法和得到的结论如下：

### 实验方法：
1. **模型选择**：选择了一个五层楼的电梯模型，该模型最初由西门子S7-200 PLC控制。
2. **模型修改**：对模型进行了修改，以便可以轻松地更换PLC进行测试。
3. **硬件配置**：电梯由直流电机驱动，每层楼都有限位开关来指示电梯的位置，并安装了额外的限位开关以防止电梯超出允许范围。
4. **用户界面**：安装了楼层指示灯和五个按钮，用于呼叫电梯到特定楼层。
5. **梯形图逻辑**：已经为西门子PLC编写了梯形图逻辑，使用西门子Step 7平台。
6. **OpenPLC编程**：将相同的梯形图逻辑转换为OpenPLC可以使用的格式，使用OpenPLC Ladder Editor进行编程。
7. **测试执行**：在OpenPLC上编译、模拟并上传梯形图逻辑，进行实际操作测试。
8. **问题识别与修正**：在测试中发现了一个导致系统无限循环的逻辑错误，并在两个控制器上进行了修正。

### 结论：
1. **功能对等**：修正错误后，OpenPLC和其他控制器（西门子PLC）表现出相同的行为，操作无误。
2. **性能一致性**：在所有测试情况下，OpenPLC对不同刺激的响应与西门子PLC相同，显示出OpenPLC的功能和性能与传统PLC相当。
3. **实用性验证**：通过实际的电梯模型测试，验证了OpenPLC作为一个真正的PLC的功能和可靠性。

实验部分通过实际的硬件测试和软件逻辑验证，证明了OpenPLC作为一个开源的PLC解决方案，能够达到与商业PLC相似的性能标准，并且在实际应用中具有可行性和有效性。