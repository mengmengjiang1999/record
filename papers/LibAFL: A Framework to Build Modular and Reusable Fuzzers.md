# LibAFL: A Framework to Build Modular and Reusable Fuzzers

@inproceedings{libafl,
author = {Fioraldi, Andrea and Maier, Dominik Christian and Zhang, Dongjia and Balzarotti, Davide},
title = {LibAFL: A Framework to Build Modular and Reusable Fuzzers},
year = {2022},
isbn = {9781450394505},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
url = {https://doi.org/10.1145/3548606.3560602},
doi = {10.1145/3548606.3560602},
abstract = {The release of AFL marked an important milestone in the area of software security testing, revitalizing fuzzing as a major research topic and spurring a large number of research studies that attempted to improve and evaluate the different aspects of the fuzzing pipeline.Many of these studies implemented their techniques by forking the AFL codebase. While this choice might seem appropriate at first, combining multiple forks into a single fuzzer requires a high engineering overhead, which hinders progress in the area and prevents fair and objective evaluations of different techniques. The highly fragmented landscape of the fuzzing ecosystem also prevents researchers from combining orthogonal techniques and makes it difficult for end users to adopt new prototype solutions.To tackle this problem, in this paper we propose LibAFL, a framework to build modular and reusable fuzzers. We discuss the different components generally used in fuzzing and map them to an extensible framework. LibAFL allows researchers and engineers to extend the core fuzzer pipeline and share their new components for further evaluations. As part of LibAFL, we integrated techniques from more than 20 previous works and conduct extensive experiments to show the benefit of our framework to combine and evaluate different approaches. We hope this can help to shed light on current advancements in fuzzing and provide a solid base for comparative and extensible research in the future.},
booktitle = {Proceedings of the 2022 ACM SIGSAC Conference on Computer and Communications Security},
pages = {1051–1065},
numpages = {15},
keywords = {fuzzing, fuzz testing, framework},
location = {Los Angeles, CA, USA},
series = {CCS '22}
}

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

5.1-5.4是想说LibAFL整合了很多已有的工作，在各种算法方面都可以使用现有研究里面比较好的工作，想要说明这个平台的通用性，以及很好用。

5.5是说明LibAFL可以支持bit-level fuzzing，并且和其他工作进行对比，说明自己性能很好。5.6是说明LibAFL可以支持Differential fuzzing并且和其他工作进行对比，来说明自己性能很好。

##### 1. roadblocks bypassing

Roadblocks bypassing是指在模糊测试（fuzzing）过程中，通过绕过那些难以通过随机变异来解决的约束或难题，以增加代码覆盖率的一种技术。这些难题或障碍可能包括复杂的输入格式、特定的程序逻辑、难以触发的比较操作等，它们会限制模糊测试的有效性，因为传统的随机或基于覆盖率的变异可能难以探索到背后的代码。LibAFL提供了几种现有的技术来绕过这些roadblocks，以提高模糊测试的覆盖率和效果。这些技术可能包括特定的输入生成策略、利用程序分析来识别并绕过障碍点、或者使用特殊的变异技术来生成能够触发那些难以到达的代码路径的输入样本。通过bypassing roadblocks，模糊测试器可以更深入地探索程序，提高发现漏洞的机会。

以“多字节比较”障碍为例。在模糊测试中可能会遇到的一个典型障碍是“larger comparisons”（较大的比较），这是指多字节比较操作，由于解空间巨大，通过随机猜测来找到正确的输入是不切实际的。为了解决这个问题，研究人员开发了一些技术来绕过这些障碍，从而使模糊测试能够更有效地探索目标程序的代码路径，发现潜在的漏洞。

在LibAFL中，综合了以下几种算法来绕过这个问题：

- 值概要（Value-profile）：由LibFuzzer在2016年提出，该技术通过最大化比较指令中两个操作数之间匹配的位数来解决比较指令。

- Cmplog：基于RedQueen和Weizz的方法，通过在运行时记录比较指令和任何带有两个指针参数的函数的相关值来绕过比较。

- Autotokens：受到AFL++的启发，通过在链接时优化（LTO）通道中提取比较指令和立即值函数的标记，并将它们编码到二进制的一个部分中，从而在不增加开销的情况下使用。

此外做了实验来比较这些不同策略对覆盖率进行的影响。这一节主要体现了LibAFL的灵活性和可扩展性，说明其能够综合很多现有的算法（或许还有新的算法？），说明这个框架非常好用。


##### 2. structure-aware fuzzing

输入数据可能具有特定的语法或者结构，但是fuzzer不一定知道这些信息。如果输入了不符合规范的语法结构，可能在格式检查的时候就直接把这种输入pass掉了，难以测试到更加深层次的代码。因此需要Structure-aware fuzzing（结构感知模糊测试）技术，更加准确地生成符合预期格式的测试输入。

这种方法的关键优势在于，它能够生成符合目标程序预期输入结构的有效测试用例，从而提高触发特定程序行为的概率，例如特定的代码路径、异常处理或安全漏洞。结构感知模糊测试可以显著提高测试的覆盖率和发现潜在漏洞的可能性。

例如，如果目标程序是一个解析JSON文件的应用程序，那么结构感知模糊测试工具将使用JSON的语法规则来生成各种JSON格式的测试用例，而不是随机生成字节序列。这样可以确保生成的测试用例不仅能够被程序解析，而且能够探索到程序处理JSON数据的各种可能情况。

在LibAFL中，可能使用一种或多种方式来利用输入格式的结构信息：

- Nautilus [4] is a grammar-based coverage-guided fuzzer
- a re-implementation of Gramatron [68], a grammar-based fuzzer that employs a grammarto-automata conversion to implement fast mutators
- Grimoire [10], a fuzzer that uses the portion of inputs that induced the novelty in coverage as tokens to build generalized “tree-like” inputs and perform grammar-like mutations.
- employs token-level fuzzing [63], an approach based on token extraction with a lexer. 而且做了一定的扩展，原始的工作只能生成

结构感知模糊测试在许多领域都有应用，特别是在处理复杂的文件格式、网络协议或二进制接口时，这种方法能够提供更加针对性和有效的测试。

简而言之，就是可以根据语法规则来给出合法输入。

##### 3. Corpus scheduling

（虽然是ai生成的，但是这次生成的内容比之前的好多了。写得挺好的，我就不改了。）

这一节讨论了在模糊测试中如何选择语料库中的下一个测试用例进行测试的问题。语料库调度是模糊测试中的一个关键环节，它决定了模糊测试器如何从已有的测试用例中选择和优先执行哪些用例，以提高发现新漏洞的效率。

在这一节中，作者介绍了几种不同的语料库调度技术，并说明了它们是如何在LibAFL框架中实现的：

1. **MinimizerScheduler**：这是基于AFL的一个调度器，它通过选择“优选”种子来优化测试过程。这些种子基于执行速度和输入长度来选择，同时保留最大覆盖率。

2. **Probabilistic Scheduler**：这是一种基于概率采样的调度器，它为语料库中的每个测试用例分配一个概率，并根据计算出的分数选择一个更有“前景”的邻近测试用例。

3. **Accounting Scheduler**：这个调度器来自TortoiseFuzz，它使用三个安全性影响指标来优先考虑输入：内存操作（块和函数粒度）、循环回边计数。

作者还讨论了这些调度技术如何与LibAFL中的其他组件（如观察器和反馈）集成，以及它们如何影响模糊测试器的性能。

在实验部分，作者执行了以下操作：

- **性能评估**：作者比较了使用不同调度器的模糊测试器在一系列基准测试上的性能。这些调度器包括随机选择（rand）、AFL的最小化器算法（minimizer）、基于概率的调度器（weighted），以及基于TortoiseFuzz的调度器（accounting）。

- **覆盖率测量**：实验测量了这些不同调度器在24小时内能够揭示的代码覆盖率，并计算了它们的平均归一化分数。

这些实验旨在说明不同的语料库调度技术对于模糊测试器性能的影响。作者指出，尽管加权调度器（weighted）在实验中表现最佳，但简单的随机方法（rand）也取得了不错的结果，这表明在快速目标上，复杂的调度技术可能并不总是必要的。此外，作者还提到，在慢速目标上，调度问题可能更加关键，因为预先决定要模糊测试的测试用例可以对模糊测试活动产生重大影响。

总体而言，这一节想要说明的问题是，虽然语料库调度是一个受到广泛关注的研究问题，但在实际的模糊测试活动中，简单的调度策略仍然有其适用性，而更复杂的调度技术可能在特定情况下更有优势。通过LibAFL框架，研究人员和开发人员可以轻松地实现和评估不同的语料库调度方法，以找到最适合其特定模糊测试需求的解决方案。

##### 4. energy assignment

能量分配（Energy Assignment）是指决定对每个测试用例（通常是语料库中的一个输入样本）进行多少次变异操作的过程。

能量分配的目标是确保模糊测试能够有效地覆盖程序的不同执行路径，同时避免在已经充分探索的区域上浪费资源。有效的能量分配策略可以帮助模糊测试工具集中精力在那些更有可能发现新问题或未被充分测试的代码区域。

在这一节中，作者介绍了几种不同的能量分配策略，并说明了它们在LibAFL框架中的实现：

Plain：这是一种简单的算法，为每个种子分配一个在给定区间内随机选择的能量值。

Explore：这种策略分配较低的能量，通过将exploit策略的能量值除以一个常数来实现。

Coe：这是一个指数方案，它将高频访问的边缘的能量值分配为0，直到它们变成低频边缘。

Fast：这是coe方案的扩展，它不是将能量值分配为0，而是将能量值分配为与访问的高频边缘数量成反比。

Lin：这种策略根据测试用例被选择进行模糊测试的次数线性分配能量。

Quad：这种策略以平方的方式分配能量，与测试用例被选择的次数有关。

作者还提到了AFLFast提出的六种不同的算法，并指出LibAFL实现了这些算法的优化版本，这些优化是在AFLFast论文发表后几年内集成到AFL++中的，并且之前没有在文献中进行过评估。

在实验部分，作者执行了以下操作：

性能评估：作者比较了LibAFL实现的三种能量分配算法（explore、coe、fast）与基于plain算法的基线的性能。

代码覆盖率测量：实验测量了这些不同能量分配策略在24小时内能够揭示的代码覆盖率，并计算了它们的平均归一化分数。

这些实验旨在说明不同的能量分配策略对于模糊测试器性能的影响。作者发现，explore策略在所有基准测试中平均表现最好，其次是fast，然后是plain，而coe的表现最差。这些结果证实了在AFL++版本中观察到的趋势，其中fast和explore是表现最好的策略，fast现在是AFL++的默认调度器。

这一节想要说明的问题是，即使是在快速目标上，简单的随机或固定能量分配可能不是最有效的策略，而更复杂的能量分配算法，如explore和fast，可以提供更好的性能。此外，作者还指出，不同的能量分配策略可能会根据目标的特点而有所不同，因此在实际应用中可能需要根据具体情况选择或调整能量分配策略。通过LibAFL框架，研究人员可以轻松地实现和评估不同的能量分配方法，以找到最适合其特定模糊测试需求的解决方案。

##### 5 A Generic Bit-level Fuzzer（一个通用的位级模糊测试器）

以下内容为Ai生成，不过我觉得讲得很好。

5.5节 "A Generic Bit-level Fuzzer"（一个通用的位级模糊测试器）介绍了LibAFL框架如何被用来构建一个通用的位级模糊测试器，并且展示了这个模糊测试器的性能如何与其他现有的先进模糊测试工具相比较。

在这一节中，作者提出了以下内容：

1. **LibAFL的通用位级模糊测试器**：作者展示了如何使用LibAFL来模糊测试LibFuzzer的harness（测试框架），并使用了一个通用的变异器。

2. **性能评估**：作者将LibAFL构建的模糊测试器与AFL++、HonggFuzz和LibFuzzer等其他模糊测试工具进行了性能比较。这些工具都是目前广泛使用的，用于模糊测试开源软件项目。

3. **实验设置**：实验在FuzzBench服务上执行，这是一个开放的模糊测试基准平台。每个模糊测试器在22个不同的基准测试上运行了23小时，并且每个实验重复了20次以减少随机性的影响。

4. **结果分析**：作者报告了每个基准测试上的覆盖率结果，并计算了所有基准测试的平均归一化分数，以评估不同模糊测试器的整体性能。

这一节的实验想要说明的问题是：

- LibAFL作为一个新开发的模糊测试框架，是否能够与现有的先进模糊测试工具竞争。
- LibAFL提供的默认实现是否足够好，以便在没有深入定制的情况下也能提供良好的模糊测试性能。
- 通过实际的基准测试，展示LibAFL在不同基准测试上的性能表现，以及它在某些情况下如何超越其他工具。

作者指出，LibAFL在所有测试中的平均归一化分数最高，表明它在这些基准测试上的性能优于其他模糊测试器。这证明了LibAFL作为一个通用模糊测试器的潜力，并且展示了其设计的有效性。此外，作者还讨论了LibAFL在某些基准测试上的性能优势，以及在其他情况下可能需要进一步优化的地方。


##### "Differential Fuzzing"（差分模糊测试）

以下内容为AI生成，不过我觉得讲得很好。

5.6节 "Differential Fuzzing"（差分模糊测试）介绍了如何使用LibAFL框架来实现差分模糊测试，这是一种比较两个或多个程序（通常是程序的不同版本或实现）的输出或行为的模糊测试方法。差分模糊测试的目的是发现程序之间的差异，这些差异可能表明存在错误、漏洞或不一致的行为。

在这一节中，作者提出了以下内容：

1. **差分模糊测试的动机**：作者解释了差分模糊测试的重要性，特别是在测试智能合约虚拟机（如以太坊虚拟机）时，这种方法可以有效地发现逻辑错误和不一致性。

2. **NeoDiff的实现**：作者讨论了如何使用LibAFL重新实现NeoDiff，这是一个用于比较两个虚拟机执行结果的差分模糊测试工具。LibAFL的实现利用了框架中的差分执行器组件，该组件充当两个底层执行器的代理。

3. **实验设置**：作者描述了如何使用LibAFL实现的NeoDiff与原始的NeoDiff进行比较。实验使用了相同的基准测试，即go-ethereum和openethereum版本，这些版本在原始的NeoDiff论文中进行了测试。

4. **性能比较**：作者报告了两种实现在12小时测试期间发现的唯一类型哈希的数量，这是一种衡量模糊测试器性能的指标。

这一节的实验想要说明的问题是：

- LibAFL框架如何简化差分模糊测试工具的实现，以及如何利用框架中现有的组件和特性来加速开发过程。

- LibAFL实现的差分模糊测试器与原始实现相比的性能如何，特别是在发现新差异和提高测试覆盖率方面。

- 通过使用LibAFL，开发者可以如何有效地利用Rust语言的性能优势和LibAFL的模块化设计来构建高效的差分模糊测试器。

作者指出，LibAFL实现的NeoDiff在发现唯一类型哈希的数量上明显优于原始实现，这表明LibAFL不仅能够提供与现有工具相当的功能，而且还能提高性能。此外，LibAFL的实现还发现了原始NeoDiff实现未发现的一些差异，这进一步证明了LibAFL在差分模糊测试领域的潜力和有效性。

### 局限性

1. solvers are hard to scale and are both time- and resource-consuming tasks. This could be mitigated by solving symbolic expressions [15] solver在时间和资源的消耗上都很大，这一点可以通过符号表达式技术进行推理

2. The other limitation is that fuzzers and concolic engines poorly cooperate. Even when a solver outputs a testcase that solves a complex expression, it is very hard for a generic bit-level fuzzer to mutate and stress the program points related to this testcase without breaking the validity of the solved expressions. 大概意思就是即使给出了一个很好的解（不管是作为corpus也好，作为挖出来的解也好），也很难使用fuzzer的变异策略得到其他很好的解。


future work

评估不同的fuzzing方法在scalable方面的性能；或者衡量基于tpc和基于共享内存的通信如何影响fuzzing。


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