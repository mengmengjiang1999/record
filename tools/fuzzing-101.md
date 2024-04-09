

error：
W: An error occurred during the signature verification. The repository is not updated and the previous index files will be used. GPG error: https://mirrors.tuna.tsinghua.edu.cn/gitlab-runner/ubuntu jammy InRelease: The following signatures were invalid: EXPKEYSIG 3F01618A51312F3F GitLab B.V. (package repository signing key) <packages@gitlab.com>
W: Failed to fetch https://mirrors.tuna.tsinghua.edu.cn/gitlab-runner/ubuntu/dists/jammy/InRelease  The following signatures were invalid: EXPKEYSIG 3F01618A51312F3F GitLab B.V. (package repository signing key) <packages@gitlab.com>
W: Some index files failed to download. They have been ignored, or old ones used instead.

terminal：
sudo apt-key adv --refresh-keys --keyserver keyserver.ubuntu.com

问题：一个fuzzing包括哪几个部分？我觉得afl的好处就是它把fuzzing过程包装得非常好，非常方便用户来用。但是它的问题也是包装得实在太好了，导致我可能实际上不是真的知道它在做什么。

#### exercise1

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
The Scheduler component defines the strategy used to supply a Fuzzer’s request to the Corpus for a new testcase。选择生成新测试用例的策略。具体怎么实现应该是早就封装好了的

6. FUZZER
对应的就是fuzzer。一个fuzzer需要负责生成新的测试用例，所以需要一个scheduler。fuzzer需要知道测试用例的覆盖率，即使是black-box的fuzzer也需要知道运行时间，所以需要这样一个component。

7. EXECUTOR
这个比较重要，executor会起很多的用户进程。不过在实现中因为封装得比较好了，所以很好搞定。

8. MUTATOR + STAGE
这是干啥的？