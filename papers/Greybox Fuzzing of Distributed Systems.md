# Greybox Fuzzing of Distributed Systems

https://arxiv.org/abs/2305.02601

这一篇主要解决了几个问题：

### 1. 分布式系统的输入是什么？回答：输入就是随机注入的一些协议调度fault

在分布式系统的模糊测试（fuzzing）中，输入与传统的顺序程序不同。对于分布式系统，输入不仅包括提供给系统的数据，还包括可以影响系统行为的环境故障和操作的特定序列。具体来说，分布式系统模糊测试的输入主要包括：

1. **故障注入（Fault Injection）**：在分布式系统中，输入的形式之一是注入的故障，例如网络分区、节点故障、延迟、数据损坏等。这些故障可以模拟在实际运行中可能遇到的各种异常情况。

2. **操作序列（Operation Sequences）**：分布式系统中的另一个关键输入是操作序列，即客户端发送请求的顺序和模式。不同的请求序列可能会导致系统处于不同的状态或行为。

3. **系统配置（System Configuration）**：系统的配置，包括节点数量、网络拓扑、数据分布等，也是影响系统行为的重要因素。

4. **时间因素（Timing）**：在分布式系统中，操作和故障发生的时间也是重要的输入因素，因为它们影响事件的因果关系和系统状态的演变。

5. **数据输入（Data Inputs）**：虽然在分布式系统中数据输入可能不如操作序列和故障注入那样显著，但提供给系统的数据也是输入的一部分，尤其是在测试数据存储和处理功能时。

6. **系统控制输入（System Control Inputs）**：这可能包括对系统内部控制逻辑的输入，例如在特定条件下触发的特定操作或协议的变更。

在Mallory框架中，这些输入通过动态构建Lamport时间线来表示，时间线记录了系统事件的相对顺序和因果关系。Mallory通过观察这些输入对系统行为的影响，并使用反馈来指导测试过程，以发现潜在的错误和不一致性。

### 2. 分布式系统如何观测到故障

在每个节点上部署一个进程，记录本节点的事件以及状态变化


### 3. 分布式系统fuzzing如何获得feedback，或者说Mallory框架中的feedback是什么

Mallory通过动态构建系统行为的Lamport时间线，并将这些时间线抽象为happens-before摘要。这些摘要提供了对系统行为的高层次反馈，表明了事件之间的因果关系。



Q1 What is the space of inputs to a distributed system that could be explored adaptively?

Jepsen：the role of “inputs” for distributed systems is played by schedules, that can be manipulated by injecting faults. Even though Jepsen can control the fault injection, in the absence of a good feedback function, it (a) requires human-written generators to explore the domain of schedules if something more than random fault injection is required [2] and (b) repeatedly explores equivalent schedules.


Q2 What observations are relevant for a distributed system and how should they be represented?

To answer Q2 we recall perhaps the most popular graphical formalism to represent interactions between nodes in distributed systems: so-called Lamport diagrams (aka timelines), i.e., graphs showing relative positions of system events as well as causality relations between them [15, 24, 31]. Such diagrams have been used in the past for visualizing executions in distributed systems [7]. Our discovery is that they also can be used as distributed analogues of
“new code paths” from sequential grey-box fuzzing. In other words, being able to observe and record new shapes of Lamport diagrams is an insight that brings AFL-style fuzzing to a distributed world.

分布式系统中常常使用Lamport Diagram来表示时间线，也就是显示系统事件的相对位置以及它们之间的因果关系的图表。如果Lamport Diagram出现一个新的形态，就认为产生了更高的覆盖率。（什么叫新的形态？）

Q3 How can one obtain feedback from the observations?

如何把Lamport Diagram变成摘要。这些摘要在反馈函数的精确度和有效性之间提供了所需的权衡。


论文先介绍了一个Raft协议中可能存在的bug

然后介绍了2.2 Fuzzing Distributed Systems via Jepsen 如何使用Jepsen来fuzzing一个分布式系统


总的来说，这个目前看不懂，而且超出了我的能力范围···


