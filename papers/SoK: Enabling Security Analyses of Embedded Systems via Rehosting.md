# SoK: Enabling Security Analyses of Embedded Systems via Rehosting

@inproceedings{enablingsecurityanalysesofembeddedsystems,
author = {Fasano, Andrew and Ballo, Tiemoko and Muench, Marius and Leek, Tim and Bulekov, Alexander and Dolan-Gavitt, Brendan and Egele, Manuel and Francillon, Aur\'{e}lien and Lu, Long and Gregory, Nick and Balzarotti, Davide and Robertson, William},
title = {SoK: Enabling Security Analyses of Embedded Systems via Rehosting},
year = {2021},
isbn = {9781450382878},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
url = {https://doi.org/10.1145/3433210.3453093},
doi = {10.1145/3433210.3453093},
abstract = {Closely monitoring the behavior of a software system during its execution enables developers and analysts to observe, and ultimately understand, how it works. This kind of dynamic analysis can be instrumental to reverse engineering, vulnerability discovery, exploit development, and debugging. While these analyses are typically well-supported for homogeneous desktop platforms (e.g., x86 desktop PCs), they can rarely be applied in the heterogeneous world of embedded systems. One approach to enable dynamic analyses of embedded systems is to move software stacks from physical systems into virtual environments that sufficiently model hardware behavior. This process which we call "rehosting" poses a significant research challenge with major implications for security analyses. Although rehosting has traditionally been an unscientific and ad-hoc endeavor undertaken by domain experts with varying time and resources at their disposal, researchers are beginning to address rehosting challenges systematically and in earnest. In this paper, we establish that emulation is insufficient to conduct large-scale dynamic analysis of real-world hardware systems and present rehosting as a firmware-centric alternative. Furthermore, we taxonomize preliminary rehosting efforts, identify the fundamental components of the rehosting process, and propose directions for future research.},
booktitle = {Proceedings of the 2021 ACM Asia Conference on Computer and Communications Security},
pages = {687–701},
numpages = {15},
keywords = {dynamic program analysis, embedded systems, emulation, firmware security, internet of things, rehosting, virtualization},
location = {Virtual Event, Hong Kong},
series = {ASIA CCS '21}
}

rehosting相关的一些总结

将强大的动态分析技术，如模糊测试和符号执行，应用于嵌入式系统。虽然以前的工作曾尝试开发针对重新托管的临时解决方案以追求其他研究目标，但我们认为重新托管本身是一个研究问题，因此应该系统地处理。
在本文中，我们从仿真中区分出重新托管领域，并表明构建完整的硬件仿真系统既不必要也无法扩展以实现固件的动态分析。我们提出了一个重新托管策略的分类，以系统化的方式强调初步方法之间的差异。我们确定了重新托管过程中的基本步骤和重新托管嵌入式系统的高层次、迭代过程。最后，我们描述了未解决的重新托管挑战，并为这一领域的未来研究提出了路线图。
通过改进重新托管过程，安全社区最终将能够将数十年的动态分析研究和成熟的工具应用于嵌入式系统的世界。我们希望这种系统化，加上我们建议的未来研究方向，将催生新的重新托管研究领域，为当前和未来的嵌入式系统提供成功的安全分析平台的基础。


rehosting相关的研究方向

我觉得sok实际上是一篇综述。


7.1 Creating Virtual Execution Engines

7.2 Widespread Adoption of Modeling Standards
具体而言就是对硬件行为有一个统一的抽象模型

7.3 Handling Peripherals
外设自动建模

7.4 Formalizing Fidelity
rehosting之后的系统行为可能和rehosting之前有很多不同。因此，需要评估rehosting之后和之前的系统有什么程度上的差异。

7.5 Rehosting of Complex Embedded Systems
对于复杂的嵌入式系统如何rehosting

