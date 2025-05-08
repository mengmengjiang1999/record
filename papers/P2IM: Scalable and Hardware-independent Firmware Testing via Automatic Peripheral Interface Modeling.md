# P2IM: Scalable and Hardware-independent Firmware Testing via Automatic Peripheral Interface Modeling

@inproceedings {p2im,
author = {Bo Feng and Alejandro Mera and Long Lu},
title = {{P2IM}: Scalable and Hardware-independent Firmware Testing via Automatic Peripheral Interface Modeling},
booktitle = {29th USENIX Security Symposium (USENIX Security 20)},
year = {2020},
isbn = {978-1-939133-17-5},
pages = {1237--1254},
url = {https://www.usenix.org/conference/usenixsecurity20/presentation/feng},
publisher = {USENIX Association},
month = aug,
abstract = {Dynamic testing or fuzzing of embedded firmware is severely limited by hardware-dependence and poor scalability, partly contributing to the widespread vulnerable IoT devices. We propose a software framework that continuously executes a given firmware binary while channeling inputs from an off-the-shelf fuzzer, enabling hardware-independent and scalable firmware testing. Our framework, using a novel technique called P2IM, abstracts diverse peripherals and handles firmware I/O on the fly based on automatically generated models. P2IM is oblivious to peripheral designs and generic to firmware implementations, and therefore, applicable to a wide range of embedded devices. We evaluated our framework using 70 sample firmware and 10 firmware from real devices, including a drone, a robot, and a PLC. It successfully executed 79% of the sample firmware without any manual assistance. We also performed a limited fuzzing test on the real firmware, which unveiled 7 unique unknown bugs.}
}