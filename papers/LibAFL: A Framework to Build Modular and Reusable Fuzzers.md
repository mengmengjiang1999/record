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


没意思不想看了TT