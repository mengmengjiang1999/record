# LibAFL: A Framework to Build Modular and Reusable Fuzzers

问题：This is due to the fact that all existing fuzzing frameworks are not designed to be extensible。并且作者认为，这并不仅仅是一个工程问题，而且This problem is not only an engineering issue, but it also highlights the lack of a standard definition of the entities that define a modern fuzzer

目前关于fuzzing的研究已经很多，但是目前的研究存在以下几个问题：

(1) Orthogonal contributions are difficult to combine. 很多种不同的研究方法太具体了，很难融合起来

(2) Individual contributions are difficult to assess. 新的贡献很难评估其有效性
（btw我好像看到过一篇评估fuzzer有效性的文章

(3) Different solutions are difficult to compare. 不同的解决方案很难进行比较
（应该也是和评估fuzzer相关？）

主要贡献：

In short, in this paper, we propose the following contributions: 
• We identify and model common building blocks used by modern fuzzers; 
• We present LibAFL, a novel open-source fuzzing framework written from scratch in Rust;
• Weimplementstate-of-the-artbuildingblocksandtechniques; 
• Basedonthesebuildingblocks,weevaluate15techniquesproposed in prior work, as well as a range of novel combinations; 
• We present a case study that re-implements a differential fuzzer using custom feedbacks; 
• Our generic fuzzer outperforms all off-the-shelf fuzzers;


### 3 ENTITIES IN MODERN FUZZING

对于一个fuzzer抽象模型的定义。

1. INPUT

对于应用程序来说，input是一串二进制文件。


2. Corpus


后面不写了，这段感觉和fuzzing-101里面的组件介绍基本是一致的。


### 4 FRAMEWORK ARCHITECTURE

框架结构。首先介绍了AFL的组件化


### 5 APPLICATIONS AND EXPERIMENTS

##### 1. roadblocks bypassing

Roadblocks bypassing是指在模糊测试（fuzzing）过程中，通过绕过那些难以通过随机变异来解决的约束或难题，以增加代码覆盖率的一种技术。这些难题或障碍可能包括复杂的输入格式、特定的程序逻辑、难以触发的比较操作等，它们会限制模糊测试的有效性，因为传统的随机或基于覆盖率的变异可能难以探索到背后的代码。

例如，在模糊测试中可能会遇到的一个典型障碍是“larger comparisons”（较大的比较），这是指多字节比较操作，由于解空间巨大，通过随机猜测来找到正确的输入是不切实际的。为了解决这个问题，研究人员开发了一些技术来绕过这些障碍，从而使模糊测试能够更有效地探索目标程序的代码路径，发现潜在的漏洞。

LibAFL提供了几种现有的技术来绕过这些roadblocks，以提高模糊测试的覆盖率和效果。这些技术可能包括特定的输入生成策略、利用程序分析来识别并绕过障碍点、或者使用特殊的变异技术来生成能够触发那些难以到达的代码路径的输入样本。通过bypassing roadblocks，模糊测试器可以更深入地探索程序，提高发现漏洞的机会。

##### 2. structure-aware fuzzing

Structure-aware fuzzing（结构感知模糊测试）是一种高级的模糊测试技术，它利用对目标程序输入格式和结构的了解来生成更加精确和有效的测试用例。与通用的模糊测试工具（它们通常对输入格式没有任何了解）不同，结构感知模糊测试工具会利用特定的输入规范或文法（grammar）来生成符合预期格式的测试输入。

这种方法的关键优势在于，它能够生成符合目标程序预期输入结构的有效测试用例，从而提高触发特定程序行为的概率，例如特定的代码路径、异常处理或安全漏洞。结构感知模糊测试可以显著提高测试的覆盖率和发现潜在漏洞的可能性。

例如，如果目标程序是一个解析JSON文件的应用程序，那么结构感知模糊测试工具将使用JSON的语法规则来生成各种JSON格式的测试用例，而不是随机生成字节序列。这样可以确保生成的测试用例不仅能够被程序解析，而且能够探索到程序处理JSON数据的各种可能情况。

在实践中，结构感知模糊测试可能涉及到以下几个方面：

1. **输入规范的定义**：定义目标输入的格式和结构，这可以通过形式化的文法、XML模式、二进制模板等方式实现。

2. **基于规则的生成器**：根据输入规范，编写或生成能够产生符合规则的测试输入的程序或脚本。

3. **变异和演化**：在保持输入有效性的前提下，对生成的测试用例进行变异，以探索程序的不同行为。

4. **反馈驱动的测试**：利用代码覆盖率、程序崩溃、性能指标等反馈信息来引导测试用例的生成和变异过程。

结构感知模糊测试在许多领域都有应用，特别是在处理复杂的文件格式、网络协议或二进制接口时，这种方法能够提供更加针对性和有效的测试。

简而言之，就是可以根据语法规则来给出合法输入吧。似乎有相关例子。

##### 3. Corpus scheduling

Corpus scheduling（语料库调度）是模糊测试（fuzzing）中的一个重要概念，它涉及到如何有效地管理和选择用于测试的输入样本集合，即语料库（corpus）。在模糊测试过程中，语料库中的输入样本会被用来探测和触发目标程序的不同行为和状态，以此来发现潜在的错误和漏洞。有效的语料库调度策略可以提高模糊测试的覆盖率和发现漏洞的能力。

语料库调度的主要目标包括：

1. **最大化代码覆盖率**：通过选择能够触发新代码路径的输入样本来不断扩展代码的执行覆盖范围。
2. **提高测试效率**：避免重复使用已经证明无效的输入样本，减少测试过程中的冗余工作。
3. **发现新的漏洞**：通过不断更新和优化语料库，增加发现新漏洞的机会。

在实际应用中，语料库调度可能会涉及到多种策略，例如：

- **基于覆盖率的调度**：根据输入样本对代码覆盖率的影响来选择样本进行测试。
- **基于反馈的调度**：根据目标程序对输入样本的响应（如崩溃、异常等）来调整语料库。
- **基于优先级的调度**：给语料库中的样本分配优先级，并根据优先级来选择样本。

例如，中提到的K-Scheduler就是一种种子调度策略，它通过分析控制流图的结构来有效地估计到达未访问边的概率，并据此调度种子，以提高模糊测试的效率和效果。而中提到的基于组的语料库调度策略则是为了解决并行模糊测试中的效率问题，通过合理地组织和调度语料库中的样本来提高测试的整体性能。中提出的选择性混合模糊测试（SHF）方法则是通过关键分支调度来提高模糊测试的针对性和效率。中提到的TAEF框架则是通过任务分配来优化集成模糊测试，进一步提高测试效率。中的MOPT则关注于优化变异调度，以提高模糊器生成有效测试用例的能力。

##### 4. energy assignment

Energy assignment（能量分配）是模糊测试中的一个重要概念，它涉及到如何为模糊测试中的种子（seeds）分配资源或“能量”，以便更有效地探索程序的状态空间并发现潜在的缺陷或漏洞。在模糊测试的上下文中，“能量”通常指的是用于生成或变异测试用例的计算资源或时间。

能量分配的目标是确保模糊测试能够有效地覆盖程序的不同执行路径，同时避免在已经充分探索的区域上浪费资源。有效的能量分配策略可以帮助模糊测试工具集中精力在那些更有可能发现新问题或未被充分测试的代码区域。


具体不想看了，大概意思就是列举了一些关键技术，然后说明自己相比现有的算法提出了哪些优化什么的。


### 结论

6 局限性与未来工作

虽然LibAFL的设计具有可扩展性，但当前的实现仍然缺乏一些组件，这些组件对于实现某些特定的模糊测试应用是必需的。例如，在撰写本文时，LibAFL CC尚未包含链接时优化（Link Time Optimization）通道，这些通道可以对整个程序的控制流图进行推理。这种类型的仪器化是实现大多数有向模糊测试方法所必需的[13, 16, 57]，因此LibAFL目前还没有提供任何有向模糊测试应用。然而，这种局限性并不是我们设计的固有问题，我们计划在不久的将来加入对有向模糊测试的支持。

LibAFL集成了一个强大的共济追踪API，可以用来扩展SymCC或SymQEMU，添加自定义约束过滤，并将符号追踪传递给基于LibAFL的模糊测试器。目前，LibAFL提供了一个基于Z3的求解器阶段，它像传统的共济模糊测试器一样生成新的测试用例。然而，传统的共济模糊测试器存在两个主要局限性，我们的架构可以帮助克服这些问题。首先，求解器难以扩展，既耗时又消耗资源。这可以通过使用模糊测试技术[6, 17, 25]来解决符号表达式。另一个局限性是模糊测试器和共济引擎之间的协作不佳。即使求解器输出了一个解决复杂表达式的测试用例，对于一个通用的位级模糊测试器来说，要在不破坏已解决表达式的有效性的情况下，对与此测试用例相关的程序点进行变异和压力测试是非常困难的。Pangolin[39]等方法正朝着这个方向发展。LibAFL构建基于共济表达式的变异器的可能性，允许开发人员实现方法来克服上述局限性，并重现以前的实验（例如，Pangolin的工件，这些工件从未公开发布过）。然而，这些在LibAFL中尚未实现。

最后，LibAFL的核心原则是可伸缩性。因此，一个有趣的未来工作将是评估不同的模糊测试同步方法在可伸缩性方面的性能。LibAFL已经实现了一个事件管理器，如果目标允许，它可以在多个核心和机器上线性扩展。它还提供了一种类似于AFL的基于磁盘的方法，用于在节点之间同步测试用例。一个有趣的研究问题是衡量不同方法（如TCP连接或基于共享内存的通信）如何影响模糊测试，并确定它们的权衡。

7 结论

在本文中，我们介绍了一个全新的、完全可扩展的模糊测试框架LibAFL。为了展示其多功能性，以及其构建最先进的模糊测试工具的现成组件的全面性，我们展示了基于LibAFL的几个前端，并进行了实验，涵盖了模糊测试文献中的不同问题。我们强调了LibAFL设计所允许的定制化，以及结合多种正交技术的力量，从而构建出超越最佳公开工具的模糊测试器。

可用性。LibAFL在Apache 2.0和MIT许可证下开源。它可以在线获取：

https://github.com/AFLplusplus/LibAFL

为了允许我们的结果的复制，并促进开放科学，本文中每个实验的前端以及相关的设置可以在在线获取：

https://github.com/AFLplusplus/libafl_paper_artifacts

致谢

首先，我们要感谢围绕AFL++组织的社区，特别是我们的贡献者。特别感谢s1341和Marc Heuse为LibAFL投入的工作，以及我们的GSoC学生，他们在过去的工作中对此进行了研究，Rishi Ranjan和Julius Hohnerlein。我们还要感谢ACM CCS的匿名审稿人的建设性评论，以及Slasti Mormanti的有用建议。这个项目部分由国防高级研究计划局（DARPA）根据协议号FA875019C0003资助。

参考文献

[1] （无日期）。Frida - 一流的动态仪器框架。https://www.frida.re/. [在线；访问于2022年4月10日]。

[2] （无日期）。Google OSS-Fuzz：对开源软件进行持续模糊测试。https://github.com/google/oss-fuzz。[在线；访问于2022年4月10日]。