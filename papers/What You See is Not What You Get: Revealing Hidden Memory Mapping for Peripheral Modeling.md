# What You See is Not What You Get: Revealing Hidden Memory Mapping for Peripheral Modeling

https://dl.acm.org/doi/abs/10.1145/3545948.3545957

@inproceedings{10.1145/3545948.3545957,
author = {Won, Jun Yeon and Wen, Haohuang and Lin, Zhiqiang},
title = {What You See is Not What You Get: Revealing Hidden Memory Mapping for Peripheral Modeling},
year = {2022},
isbn = {9781450397049},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
url = {https://doi.org/10.1145/3545948.3545957},
doi = {10.1145/3545948.3545957},
abstract = {Nowadays, there are a massive number of embedded Internet-of-Things (IoT) devices, each of which includes a microcontroller unit (MCU) that can support numerous peripherals. To detect security vulnerabilities of these embedded devices, there are a number of emulation (or rehosting) frameworks that enable scalable dynamic analysis by using only the device firmware code without involving the real hardware. However, we show that using only the firmware code for emulation is insufficient since there exists a special type of hardware-defined property among the peripheral registers that allows the bounded registers to be updated simultaneously without CPU interventions, which is called the hidden memory mapping. In this paper, we demonstrate that existing rehosting frameworks such as P2IM and μEMU have incorrect execution paths as they fail to properly handle hidden memory mapping during emulation. To address this challenge, we propose the first framework AutoMap that uses a differential hardware memory introspection approach to automatically reveal hidden memory mappings among peripheral registers for faithful firmware emulation. We have developed AutoMap atop the Unicorn emulator and evaluated it with 41 embedded device firmware developed based on the Nordic MCU and 9 real-world firmware evaluated by μEMU and P2IM on the two STMicroelectronics MCUs. Among them, AutoMap successfully extracted 2, 359 unique memory mappings in total which can be shared through a knowledge base with the rehosting frameworks. Moreover, by integrating AutoMap with μEMU, AutoMap is able to identify and correct the path of the program that will not run on the actual hardware.},
booktitle = {Proceedings of the 25th International Symposium on Research in Attacks, Intrusions and Defenses},
pages = {200–213},
numpages = {14},
keywords = {Embedded devices, Firmware analysis, Firmware emulation, Peripheral modeling},
location = {Limassol, Cyprus},
series = {RAID '22}
}