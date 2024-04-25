# LibAFL QEMU: A Library for Fuzzing-oriented Emulation

1. 把qemu包装成一个库

2. 避免对原始QEMU代码库进行过多的更改，以最小化从更近期的上游提交合并时的冲突数量

这样可以方便LibAFL QEMU作为LibAFL的一部分被使用。

测试部分说明了自己性能很好而且功能正常。

System mode: Fast VM Snapshots

LibAFL QEMU进行了一些设计，stackbased, 使得状态的保存和恢复效率更高。allowing for fast saving and restoration of intermediate states of the target.

