# ICS3Fuzzer: A Framework for Discovering Protocol Implementation Bugs in ICS Supervisory Software by Fuzzing

https://dl.acm.org/doi/abs/10.1145/3485832.3488028

@inproceedings{10.1145/3485832.3488028,
author = {Fang, Dongliang and Song, Zhanwei and Guan, Le and Liu, Puzhuo and Peng, Anni and Cheng, Kai and Zheng, Yaowen and Liu, Peng and Zhu, Hongsong and Sun, Limin},
title = {ICS3Fuzzer: A Framework for Discovering Protocol Implementation Bugs in ICS Supervisory Software by Fuzzing},
year = {2021},
isbn = {9781450385794},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
url = {https://doi.org/10.1145/3485832.3488028},
doi = {10.1145/3485832.3488028},
abstract = {The supervisory software is widely used in industrial control systems (ICSs) to manage field devices such as PLC controllers. Once compromised, it could be misused to control or manipulate these physical devices maliciously, endangering manufacturing process or even human lives. Therefore, extensive security testing of supervisory software is crucial for the safe operation of ICS. However, fuzzing ICS supervisory software is challenging due to the prevalent use of proprietary protocols. Without the knowledge of the program states and packet formats, it is difficult to enter the deep states for effective fuzzing. In this work, we present a fuzzing framework to automatically discover implementation bugs residing in the communication protocols between the supervisory software and the field devices. To avoid heavy human efforts in reverse-engineering the proprietary protocols, the proposed approach constructs a state-book based on the readily-available execution trace of the supervisory software and the corresponding inputs. Then, we propose a state selection algorithm to find the protocol states that are more likely to have bugs. Our fuzzer distributes more budget on those interesting states. To quickly reach the interesting states, traditional snapshot-based method does not work since the communication protocols are time sensitive. We address this issue by synchronously managing external events (GUI operations and network traffic) during the fuzzing loop. We have implemented a prototype and used it to fuzz the supervisory software of four popular ICS platforms. We have found 13 bugs and received 3 CVEs, 2 are classified as critical (CVSS3.x score CRITICAL 9.8) and affected 40 different products.},
booktitle = {Proceedings of the 37th Annual Computer Security Applications Conference},
pages = {849–860},
numpages = {12},
keywords = {GUI-driven fuzzer, ICS security, Supervisory software, fuzzing, protocol implementation bugs},
location = {Virtual Event, USA},
series = {ACSAC '21}
}

这个fuzzing的对象是ICS监控程序  Supervisory software

监控程序的特点：

1. Windows系统下的，具体流程和GUI有很大关系

2. 和PLC的通信是专有协议

3. 监测崩溃是通过窗口崩溃来完成的

并不是基于覆盖率反馈的fuzzing，而是黑盒测试。具体来说因为作者提出，基于覆盖率反馈的测试难度比较大，开销也比较大。总体的工作量都用来处理合理的输入和输出了。


Case Study: GX Works2