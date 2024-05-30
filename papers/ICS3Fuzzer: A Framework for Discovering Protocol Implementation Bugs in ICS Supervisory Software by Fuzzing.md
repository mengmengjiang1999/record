# ICS3Fuzzer: A Framework for Discovering Protocol Implementation Bugs in ICS Supervisory Software by Fuzzing

https://dl.acm.org/doi/abs/10.1145/3485832.3488028

这个fuzzing的对象是ICS监控程序  Supervisory software

监控程序的特点：

1. Windows系统下的，具体流程和GUI有很大关系

2. 和PLC的通信是专有协议

3. 监测崩溃是通过窗口崩溃来完成的

并不是基于覆盖率反馈的fuzzing，而是黑盒测试。具体来说因为作者提出，基于覆盖率反馈的测试难度比较大，开销也比较大。总体的工作量都用来处理合理的输入和输出了。


Case Study: GX Works2