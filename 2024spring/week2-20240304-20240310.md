# 2024spring week2

20240304-20240310

Rust程序安全相关论文调研

### 1.VRust: Automated Vulnerability Detection for Solana Smart Contracts

ACM CCS 2022

针对solana智能合约系统的rust检测框架，具体而言是把solana源代码翻译成Rust-MIR，并且使用静态分析和形式化验证的方法来检测漏洞。
VRust is able to check all of them fully automatically by translating source code into Rust MIR-based inference rules without any code annotations。

### 2.MirChecker: Detecting Bugs in Rust Programs via Static Analysis

给rust程序找漏洞的，对Rust的MIR进行静态分析。

ACM CCS 2021

在本文中，我们介绍并评估了 MirChecker，这是一个通过对 Rust 的中层中间表示（MIR）进行静态分析，对 Rust 程序进行全自动错误检测的框架。我们的方法基于对 Rust 代码库中发现的现有错误的观察，同时跟踪数值和符号信息，利用约束求解技术检测潜在的运行时崩溃和内存安全错误，并向用户输出信息诊断。我们在从现有的 "常见漏洞和暴露"（Common Vulnera- bilities and Exposures，CVE）和现实世界的 Rust 代码库中提取的错误代码片段上对 MirChecker 进行了评估。实验结果表明，MirChecker 可以检测出代码片段中的所有问题，并能在现实世界的场景中进行错误查找，它从 12 个 Rust 软件包（crate）中检测出了 33 个以前未知的错误，其中包括 16 个内存安全性问题，而且误报率在可接受范围内。


### 3.TRust: A Compilation Framework for In-process Isolation to Protect Safe Rust against Untrusted Code

sec2023

Rust里面unsafe{}包起来的代码可能有bug，通过进程内隔离，将unsafe包起来的代码块与安全代码隔离起来。


### 4.Rudra: Finding Memory Safety Bugs in Rust at the Ecosystem Scale

SOSP2021

分析rust漏洞，重点关注内存安全。在系统编程中通常不得不使用unsafe把一部分代码包起来，这部分代码的安全性成为一个问题。扫描了很多rust package，发现了很多漏洞。使用HIR和MIR进行hybrid analyse。

        // pthread_yield();
        // https://github.com/libxsmm/libxsmm/issues/684
        // there is a confirmed bug in Linux.