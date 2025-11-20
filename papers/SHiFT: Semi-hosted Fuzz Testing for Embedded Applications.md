# SHiFT: Semi-hosted Fuzz Testing for Embedded Applications

虽然叫semi-hosted fuzzing testing，但是跟para-rehosting中说的semi-rehosting并不一样。这是外设进行了转发，但是固件部分直接在硬件上跑的。

rehosting存在的问题：

软件行为可能和硬件并不完全一致
外设接口错误（？
时序和同步问题
和DMA相关的一些问题

只能模拟简单的固件-外设交互


所以shift做的事情 其实是几乎完全在硬件上做fuzzing。做关于性能的实验的时候，是和其他直接在硬件上做fuzzing的工作进行对比的。


