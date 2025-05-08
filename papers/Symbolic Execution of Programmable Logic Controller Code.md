# Symbolic Execution of Programmable Logic Controller Code

@inproceedings{symbolicexecutionprogrammablelogiccontrollercode,
author = {Guo, Shengjian and Wu, Meng and Wang, Chao},
title = {Symbolic execution of programmable logic controller code},
year = {2017},
isbn = {9781450351058},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
url = {https://doi.org/10.1145/3106237.3106245},
doi = {10.1145/3106237.3106245},
abstract = {Programmable logic controllers (PLCs) are specialized computers for automating a wide range of cyber-physical systems. Since these systems are often safety-critical, software running on PLCs need to be free of programming errors. However, automated tools for testing PLC software are lacking despite the pervasive use of PLCs in industry. We propose a symbolic execution based method, named SymPLC, for automatically testing PLC software written in programming languages specified in the IEC 61131-3 standard. SymPLC takes the PLC source code as input and translates it into C before applying symbolic execution, to systematically generate test inputs that cover both paths in each periodic task and interleavings of these tasks. Toward this end, we propose a number of PLC-specific reduction techniques for identifying and eliminating redundant interleavings. We have evaluated SymPLC on a large set of benchmark programs with both single and multiple tasks. Our experiments show that SymPLC can handle these programs efficiently, and for multi-task PLC programs, our new reduction techniques outperform the state-of-the-art partial order reduction technique by more than two orders of magnitude.},
booktitle = {Proceedings of the 2017 11th Joint Meeting on Foundations of Software Engineering},
pages = {326–336},
numpages = {11},
keywords = {Test generation, Symbolic execution, SCADA, Programmable logic controller, Partial order reduction, PLC},
location = {Paderborn, Germany},
series = {ESEC/FSE 2017}
}


### 贡献总结：

1. **首个基于符号执行的PLC程序测试工具**：  
   - 提出了SymPLC，这是首个将符号执行技术应用于可编程逻辑控制器（PLC）程序的自动化测试工具。PLC程序通常用于安全关键系统，传统测试方法依赖人工编写测试用例，而SymPLC能够自动生成高覆盖率的测试输入和任务调度序列。

2. **多任务PLC程序的并发语义建模**：  
   - 通过将PLC任务翻译为多线程C程序，并精确建模PLC特有的优先级调度和周期性执行语义，解决了传统符号执行工具无法直接处理PLC非传统并发语义的问题。

3. **PLC专用的优化技术**：  
   - 提出了三种针对PLC特性的优化技术：  
     - **基于优先级的优化**：利用任务优先级避免无效的抢占。  
     - **基于周期的优化**：根据任务周期排除时间上不可能重叠的调度。  
     - **状态匹配优化**：通过检测重复状态提前终止冗余执行。  
   - 实验表明，这些优化技术比传统的部分顺序规约（POR）技术效率高出两个数量级。

4. **灵活性与可扩展性**：  
   - SymPLC将建模（PLC到C的翻译）与分析（符号执行）分离，支持多种PLC语言（如ST、LAD等），便于扩展新语言和平台。

5. **实验验证**：  
   - 在93个PLC基准程序（包括单任务和多任务）上进行了测试，覆盖了26,713行ST代码。SymPLC不仅能高效生成测试用例，还能检测程序错误并证明部分属性的正确性。

---

### 不足之处：

1. **对非终止程序的局限性**：  
   - PLC程序通常是周期性运行且不终止的，SymPLC通过设置超时或迭代次数限制来处理这一问题，但可能导致某些深层错误无法被发现。

2. **状态爆炸问题**：  
   - 尽管提出了PLC专用优化技术，但对于复杂多任务程序（如超周期内任务实例多或全局操作频繁），符号执行仍可能面临状态空间爆炸的挑战。

3. **依赖外部工具链**：  
   - SymPLC依赖MatIEC编译器（将ST翻译为C）和Cloud9符号执行引擎，工具链的稳定性或兼容性问题可能影响实际应用。

4. **形式化验证的不足**：  
   - SymPLC主要用于测试而非形式化验证，无法完全保证程序正确性。虽然能通过状态匹配证明部分属性，但覆盖性有限。

5. **输入约束的局限性**：  
   - 符号执行生成的输入可能包含冗余（如定时器的抽象建模为任意布尔值），需依赖后续优化技术进一步过滤。

---

### 总结：
SymPLC通过结合符号执行与PLC专用优化技术，填补了PLC自动化测试工具的空白，显著提升了多任务程序的测试效率。然而，其在处理复杂程序时的可扩展性、对非终止程序的完全验证能力等方面仍有改进空间。未来工作可探索更高效的状态合并技术或与形式化方法结合以进一步提升覆盖率。