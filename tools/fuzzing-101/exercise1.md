# exercise1

## 问题及解决方式：


1. 问题：
W: An error occurred during the signature verification. The repository is not updated and the previous index files will be used. GPG error: https://mirrors.tuna.tsinghua.edu.cn/gitlab-runner/ubuntu jammy InRelease: The following signatures were invalid: EXPKEYSIG 3F01618A51312F3F GitLab B.V. (package repository signing key) <packages@gitlab.com>
W: Failed to fetch https://mirrors.tuna.tsinghua.edu.cn/gitlab-runner/ubuntu/dists/jammy/InRelease  The following signatures were invalid: EXPKEYSIG 3F01618A51312F3F GitLab B.V. (package repository signing key) <packages@gitlab.com>
W: Some index files failed to download. They have been ignored, or old ones used instead.

解决方式：

在命令行里：
sudo apt-key adv --refresh-keys --keyserver keyserver.ubuntu.com


2. 问题：

error[E0658]: use of unstable library feature 'error_in_core'
   --> /home/mmj/.cargo/registry/src/mirrors.tuna.tsinghua.edu.cn-df7c3c540f42cdbd/libafl_bolts-0.13.1/src/lib.rs:640:6
    |
640 | impl core::error::Error for Error {}
    |      ^^^^^^^^^^^^^^^^^^
    |
    = note: see issue #103765 <https://github.com/rust-lang/rust/issues/103765> for more information
    = help: add `#![feature(error_in_core)]` to the crate attributes to enable
    = note: this compiler was built on 2024-04-09; consider upgrading it if it is out of date

For more information about this error, try `rustc --explain E0658`.
error: could not compile `libafl_bolts` (lib) due to 1 previous error
warning: build failed, waiting for other jobs to finish...

解决方案：

先更新一下rust工具链，然后把Cargo.toml文件更新一下，然后把libAFL的版本更新一下。不能使用default-feature=false这个选项，因为很多功能是在std feature下才能使用的。

```
[package]
name = "exercise-one-solution"
version = "0.1.0"
edition = "2021"
build = "build.rs"

[dependencies]
libafl = { version="0.13.1"}
libafl_bolts = { version="0.13.1"}
```

3. 关于0.13.1版本的很多信息

LibAFL在每次版本更新的时候，都会更新很多


## 记录

1. CORPUS + INPUT
corpus的意思就是现在有的输入。需要根据已经有的输入来变异出其他输入。或者说是“种子池”之类的东西，因为随着fuzz过程，corpus也会变的。
对于libafl来说，corpus需要指定一个文件位置，然后那个文件位置确实放了几个文件就好了。
至于变异等等这些过程，libafl都封装好了，这不是用户需要关心的事情。

2. OBSERVER
observer就是观测当前程序运行状态的。例如在exercise1的例子里，给出了对于程序运行时间的time-observer。
另外为了获得覆盖率，还可以建立一个HitcountsMapObserver等等。
(总之除了这两种observer或许还有别的吧。文档里好像没写。再说。)
不过我们可以知道，为了实现hitcountmapobserver，还需要干点别的。具体而言，首先是分配一块共享内存，使得被测试程序和observer都能读这块内存。

3. FEEDBACK
feedback来判断刚刚新生成的测试用例是否为interesting的。如果是的话，那么就将其加入corpus里面。
此外还有一个timefeedback，这个到底会用来做什么我也不知道。

4. STATE，MONITOR，EVENTMANAGER
A State component takes ownership of each of our existing FeedbackState components, a random number generator, and our corpora.
一个在实现的层面上比较关键但是在理论层面上可以没有的东西。

The Monitor component keeps track of all of the clients and offers methods on how their reported information can be displayed。
评价同上。

event manager评价同上。

5. SCHEDULER
The Scheduler component defines the strategy used to supply a Fuzzer’s request to the Corpus for a new testcase。选择生成新测试用例的策略。具体怎么实现在另一部分，scheduler只管选择策略。

6. FUZZER
对应的就是fuzzer。一个fuzzer需要负责生成新的测试用例，所以需要一个scheduler。fuzzer需要知道测试用例的覆盖率，即使是black-box的fuzzer也需要知道运行时间，所以需要这样一个component。

7. EXECUTOR
这个比较重要，executor会起很多的用户进程。不过在实现中因为封装得比较好了，所以很好搞定。

8. MUTATOR + STAGE
mutator是用来做变异的。stage是什么意思？


编译运行中可能遇到的报错：

CC=/home/mmj/Project/AFLplusplus/afl-clang-fast CXX=/home/mmj/Project/AFLplusplus/afl-clang-fast++ ./configure --prefix=/home/mmj/Project/fuzzing-101-solutions/exercise-1/xpdf/install
checking for gcc... /home/mmj/Project/AFLplusplus/afl-clang-fast
checking for C compiler default output file name... configure: error: C compiler cannot create executables
See `config.log' for more details.

CC=/home/mmj/Tools/AFLplusplus/afl-clang-fast CXX=/home/mmj/Tools/AFLplusplus/afl-clang-fast++ ./configure --prefix=/home/mmj/Project/fuzzing-101-solutions/exercise-1/xpdf/install

如果出现这个报错，说明AFLplusplus需要更新然后重新build一遍。或者也有可能是llvm-config的版本原因。总之AFLplusplus pull之后重新build就可以正常使用了


## exercise1.5

这部分主要想要解决的问题是：提高exercise1的fuzzing效率。

exercise1以及afl++中都使用了forkserver模式来做fuzz，由一个进程来启动另一个进程，然后在这个过程中对另一个进程的运行模式进行监控之类的。