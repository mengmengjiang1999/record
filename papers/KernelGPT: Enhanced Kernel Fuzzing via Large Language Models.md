# kernelGPT

### 工作背景

1. 系统调用规范（or描述）在内核fuzz中的重要性
syzkaller运行时依赖syzlang语言去定义系统调用规范，并且以此引导内核fuzz的过程，生成一些更加好用的测试用例。然而 Expressing parameter types and dependencies for a syscall without specifying any concrete parameter value is impossible。作者在论文中举出了一些例子，来说明：有系统调用规范的描述可以减少测试用例构造空间

2. 现有的内核调用规范是手动生成的，会存在有错误/过时等问题


### 相关工作-syzkaller相关

主要是一些改进syzkaller的方法

KSG：符号执行收集类型和范围信息
difuse和SyzDescribe：对内核源代码进行静态分析，识别常见的实现模式以生成规范
SyzGen：目标仅为二进制macOS驱动
Moonshine：收集并提炼Syzkaller的踪迹，为Syzkaller生成种子池（这是什么意思？先不管）
SyzVegas：利用强化学习来动态改进种子和任务选择
HEALER：通过观察不同系统调用组合的覆盖变化来推断系统调用依赖关系
SyzDirect：通过将距离信息作为反馈，对Syzkaller应用定向灰盒模糊
ThunderKaller：通过跳过块调用、减少覆盖收集和消毒来提高Syzkaller的性能

KernelGPT专注于从源代码生成规范，和上述工作的改进方式可以同时使用。

### 相关工作- LLM相关

A growing body of research has focused on leveraging LLMs for testing, such as unit test generation [26,31,39,54], fuzzing [13, 14, 22, 30, 49, 52] and static analysis [27].

现有的利用LLM进行测试的工作主要集中在使用LLM直接为被测系统创建测试输入，例如生成测试C编译器的C程序。

总之就是LLM可以用于生成测试用例，不过生成的方式和KernelGPT不太一样。具体哪里不一样应该还是要看下具体实现。

### 设计和实现

Three automated phases: 
+ Driver Detection 1
+ Specification Generation 2
+ Specification Validation and Repair 3

syz-extract生成的报错指导KernelGPT去修复。

此工作专注于为Syzkaller中没有描述的驱动程序或处理程序生成描述。

（还有一些不太能看懂，再看看）

### 实验

就是比baseline达到了更高的覆盖率

总的来说我觉得这篇很厉害