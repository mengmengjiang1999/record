# KRACE: Data Race Fuzzing for Kernel File Systems

https://ieeexplore.ieee.org/document/9152693

https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9152693




Overview. We say a pair of memory operations, <ix, iy>, is a data race candidate if, at runtime, we observed that
• they access the same memory location,
• they are issued from different contexts tx and ty,
• at least one of them is a write operation.

Such information is trivial to obtain dynamically by simply
hooking every memory access. The difficulty lies in confirming whether a data race candidate is a true race. For this, we need two more analysis steps to check that:


这段内容描述了KRACE框架中数据竞争检测的过程和概念。以下是详细解释：

1. **数据竞争候选的识别**：
   - 首先，如果两个内存操作（记为<ix, iy>）在运行时满足以下条件，则被认为是数据竞争的候选：
     a. 它们访问相同的内存位置。
     b. 它们由不同的上下文（或线程）tx和ty发出。
     c. 至少有一个操作是写操作。

2. **数据竞争候选的确认**：
   - 仅识别出候选是不够的，需要进一步分析以确认这是否是真正的数据竞争。这需要两个额外的分析步骤：
     a. **锁集分析（Lockset Analysis）**：检查在发出ix和iy操作时，tx和ty是否共同持有任何锁。如果在这两个上下文中都没有共同的锁，那么它们可能存在数据竞争。
     b. **先行发生分析（Happens-before Analysis）**：基于执行过程，检查是否存在ix和iy之间的顺序关系。如果没有理由说明ix必须在iy之前发生，或者反之亦然，那么它们可能存在数据竞争。

3. **锁集分析的优势和局限性**：
   - 锁集分析理论上不会产生假阴性（即如果存在数据竞争，锁集分析保证能够标记出来）。但这种方法可能会产生假阳性，因为它忽略了操作之间的顺序信息。

4. **先行发生分析的作用**：
   - 先行发生分析有助于过滤掉锁集分析可能产生的假阳性，通过确定操作之间的因果关系来减少误报。

5. **内核复杂性**：
   - 尽管锁集和先行发生分析在概念上简单，但它们需要对内核中的所有同步机制有一个完整的模型，以及对所有线程排序原语进行注释。否则，可能会产生假阳性。
   - Linux内核经过近30年的发展，累积了丰富的同步机制。KRACE采用了尽力而为的方法来模拟所有主要的同步原语，以及在实验中遇到的任何特别的同步机制。

6. **内核执行中的排序点数量**：
   - 内核执行中的排序点数量是巨大的，这增加了数据竞争检测的复杂性。为了展示现实世界执行中的复杂性，文中提到图18展示了跨所有用户和内核线程的排序关系的一个片段。

总的来说，这段内容强调了在KRACE中检测数据竞争的复杂性，并介绍了如何通过锁集和先行发生分析来识别和确认数据竞争。