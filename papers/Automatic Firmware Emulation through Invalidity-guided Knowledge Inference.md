#  Automatic Firmware Emulation through Invalidity-guided Knowledge Inference

@inproceedings {firmwareemulation,
author = {Wei Zhou and Le Guan and Peng Liu and Yuqing Zhang},
title = {Automatic Firmware Emulation through Invalidity-guided Knowledge Inference},
booktitle = {30th USENIX Security Symposium (USENIX Security 21)},
year = {2021},
isbn = {978-1-939133-24-3},
pages = {2007--2024},
abstract = {Emulating ﬁrmware for microcontrollers is challenging due to the tight coupling between the hardware and ﬁrmware. This has greatly impeded the application of dynamic analysis tools to ﬁrmware analysis. The state-of-the-art work automatically models unknown peripherals by observing their access patterns, and then leverages heuristics to calculate the appropriate responses when unknown peripheral registers are accessed. However, we empirically found that this approach and the corresponding heuristics are frequently insufﬁcient to emulate ﬁrmware. In this work, we propose a new approach called µEmu to emulate ﬁrmware with unknown peripherals. Unlike existing work that attempts to build a general model for each peripheral, our approach learns how to correctly emulate ﬁrmware execution at individual peripheral access points. It takes the image as input and symbolically executes it by representing unknown peripheral registers as symbols. During symbolic execution, it infers the rules to respond to unknown peripheral accesses. These rules are stored in a knowledge base, which is referred to during the dynamic ﬁrmware analysis. µEmu achieved a passing rate of 93% in a set of unit tests for peripheral drivers without any manual assistance. We also evaluated µEmu with real-world ﬁrmware samples and new bugs were discovered.},
url = {https://www.usenix.org/conference/usenixsecurity21/presentation/zhou},
publisher = {USENIX Association},
month = aug
}