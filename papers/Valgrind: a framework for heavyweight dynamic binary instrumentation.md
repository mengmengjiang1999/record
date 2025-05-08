# Valgrind: a framework for heavyweight dynamic binary instrumentation

@inproceedings{valgrind,
author = {Nethercote, Nicholas and Seward, Julian},
title = {Valgrind: a framework for heavyweight dynamic binary instrumentation},
year = {2007},
isbn = {9781595936332},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
url = {https://doi.org/10.1145/1250734.1250746},
doi = {10.1145/1250734.1250746},
abstract = {Dynamic binary instrumentation (DBI) frameworks make it easy to build dynamic binary analysis (DBA) tools such as checkers and profilers. Much of the focus on DBI frameworks has been on performance; little attention has been paid to their capabilities. As a result, we believe the potential of DBI has not been fully exploited.In this paper we describe Valgrind, a DBI framework designed for building heavyweight DBA tools. We focus on its unique support for shadow values-a powerful but previously little-studied and difficult-to-implement DBA technique, which requires a tool to shadow every register and memory value with another value that describes it. This support accounts for several crucial design features that distinguish Valgrind from other DBI frameworks. Because of these features, lightweight tools built with Valgrind run comparatively slowly, but Valgrind can be used to build more interesting, heavyweight tools that are difficult or impossible to build with other DBI frameworks such as Pin and DynamoRIO.},
booktitle = {Proceedings of the 28th ACM SIGPLAN Conference on Programming Language Design and Implementation},
pages = {89–100},
numpages = {12},
keywords = {Memcheck, Valgrind, dynamic binary analysis, dynamic binary instrumentation, shadow values},
location = {San Diego, California, USA},
series = {PLDI '07}
}

@article{10.1145/1273442.1250746,
author = {Nethercote, Nicholas and Seward, Julian},
title = {Valgrind: a framework for heavyweight dynamic binary instrumentation},
year = {2007},
issue_date = {June 2007},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
volume = {42},
number = {6},
issn = {0362-1340},
url = {https://doi.org/10.1145/1273442.1250746},
doi = {10.1145/1273442.1250746},
abstract = {Dynamic binary instrumentation (DBI) frameworks make it easy to build dynamic binary analysis (DBA) tools such as checkers and profilers. Much of the focus on DBI frameworks has been on performance; little attention has been paid to their capabilities. As a result, we believe the potential of DBI has not been fully exploited.In this paper we describe Valgrind, a DBI framework designed for building heavyweight DBA tools. We focus on its unique support for shadow values-a powerful but previously little-studied and difficult-to-implement DBA technique, which requires a tool to shadow every register and memory value with another value that describes it. This support accounts for several crucial design features that distinguish Valgrind from other DBI frameworks. Because of these features, lightweight tools built with Valgrind run comparatively slowly, but Valgrind can be used to build more interesting, heavyweight tools that are difficult or impossible to build with other DBI frameworks such as Pin and DynamoRIO.},
journal = {SIGPLAN Not.},
month = jun,
pages = {89–100},
numpages = {12},
keywords = {Memcheck, Valgrind, dynamic binary analysis, dynamic binary instrumentation, shadow values}
}

