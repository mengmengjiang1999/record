# Fuzzing: a survey

（注意这篇survey是2018年的）

关于fuzzing本身的改进：


Key questions

A. How to get initial inputs?
Common used methods of gathering seed inputs include using standard benchmarks, crawling from the Table 4 Comparison of different techniques Internet and using existing POC samples. 
AFL provides a tool, which extracts a minimum set of inputs that achieve the same code coverage.

B. How to generate testcases?
Besides, good testcases could target poten- tial vulnerable locations and bring a faster discovery of program bugs. Thus how to generate good testcases based on seed inputs is an important concern.
With the development and widely use of machine learning techniques, some research try to use machine learning techniques to assist the generation of testcases.

C. How to select seed from the pool?
Previous work has prove that good seed selection strategy could significantly improve the fuzzing efficiency and help find more bugs, faster
选好这个种子有很多好处总而言之就是这个意思

D. How to efficiently test applications? 
As we know, for fuzzing of user- land applications, creation and finishing of process will consume large amount of cpu time. 
AFL employs a forkserver method, which create an identical clone of the already-loaded program and reuse the clone for each single run. 

### testcase generation phase

testcases in fuzzing are generated in generation based method or mutation based method.
如果没有说明文档的话，How to obtain the format information of inputs is a hard open problem. （再加上说明文档对此的描述可能也是不正确的。）
More state-of-the-art fuzzers employ a mutation-based fuzzing strategy.

fuzzing可能还会碰到某些具体的条件很难满足的分支，例如：
1. 边界条件检查
2. 一些魔法数字检查
等等。


### Program execution

1. Fuzzing process is often guided to cover more code and discover bugs faster, thus path execution information is required. 
kAFL，使用了Inter PT硬件特性

2. Another concern in testing execution is to explore new path.

## Fuzzing towards different applications

- fuzzing on web browsers.

- Kernel fuzzing

First, different with userland fuzzing, crashes and hangs in kernel will bring down the whole system, and how to catch the crashes is an open problem. 
Secondly, the system authority mechanism result in a relatively closed execution environment, considering that fuzzers are generally run in ring 3 and how to interact with kernels is another challenge.
Besides, widely used kernels like Windows kernel and MacOS kernel are closed source, and is hard to instrument with a low performance overhead. 

Generally, OS kernels are fuzzed by randomly calling kernel API functions with randomly generated parameter values. 
- knowledge based fuzzers
 (1) the parameters of API calls should have random yet well-formed values that follow the API specification, and (2) the ordering of kernel API calls should appear to be valid (Han and Cha 2017).
- Coverage based fuzzing
 Syzkaller, KAFL, TriforceAFL

- Fuzzing of protocols
（先跳过了）

### New trends of fuzzing

1. 通过AI等技术
2. 利用新的硬件特性加速
