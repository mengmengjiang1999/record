# Programmable logic controllers based systems (PLC‐BS): vulnerabilities and threats

https://link.springer.com/article/10.1007/s42452-019-0860-2

@article{plcvulneabilitiesthreats,
  author    = {Abraham Serhane and Mohamad Raad and Raad Raad and Willy Susilo},
  title     = {Programmable logic controllers based systems (PLC-BS): vulnerabilities and threats},
  journal   = {SN Applied Sciences},
  year      = {2019},
  volume    = {1},
  number    = {8},
  pages     = {924},
  issn      = {2523-3971},
  doi       = {10.1007/s42452-019-0860-2},
  url       = {https://doi.org/10.1007/s42452-019-0860-2},
  abstract  = {This paper provides a review of the state-of-the-art of major Programmable Logic Controller (PLC) based devices along with their security concerns. It discusses, mainly, the threats and vulnerabilities of PLCs and associated field devices—including local industrial networks. As PLC-BS are becoming more integrated and interconnected with other complex systems and open source solutions, they are becoming more vulnerable to critical threats and exploitations. Little attention and progress have been made in securing such devices if compared to that of securing overall Industrial Control Systems. This review shows the fact that major PLC based devices have several vulnerabilities and are insecure by design—firmware, code, or hardware. This paper suggests policies, recommendations, and countermeasures to secure PLC-BS. Securing PLC-BS is vital and crucial since a compromised PLC-BS would lead to significant financial loss and safety risks that could endanger human lives or the environment.},
  date      = {2019-07-26}
}


Abstract
This paper provides a review of the state-of-the-art of major Programmable Logic Controller (PLC) based devices along with their security concerns. It discusses, mainly, the threats and vulnerabilities of PLCs and associated field devices— including local industrial networks. As PLC-BS are becoming more integrated and interconnected with other complex systems and open source solutions, they are becoming more vulnerable to critical threats and exploitations. Little atten- tion and progress have been made in securing such devices if compared to that of securing overall Industrial Con- trol Systems. This review shows the fact that major PLC based devices have several vulnerabilities and are insecure by design—firmware, code, or hardware. This paper suggests policies, recommendations, and countermeasures to secure PLC-BS. Securing PLC-BS is vital and crucial since a compromised PLC-BS would lead to significant financial loss and safety risks that could endanger human lives or the environment.

这个论文也是关于PLC安全的综述。这里面比较值得看的是：

第三章的部分。


在文章的 "3.1 PLC code vulnerabilities" 部分，作者详细讨论了PLC（可编程逻辑控制器）代码中存在的安全漏洞。以下是该部分的主要内容：

1. **代码漏洞的关注不足**：相较于网络相关的安全问题，PLC代码的安全漏洞并没有得到足够的关注。一些公司、开发者和程序员错误地认为，只要没有网络入侵者，PLC内部运行的代码就是安全的。但实际上，PLC代码可能包含可以被黑客或其他不满用户利用的破坏性威胁和漏洞。

2. **代码编写或设计的问题**：PLC代码中的漏洞主要来源于代码的编写或设计方式。以下是一些典型的漏洞示例：
   - **不完整的故障或报警处理**：恶意代码可以禁用或静默某些报警，导致操作员无法注意到问题。
   - **伪造的结果**：PLC代码跳过某些梯级或参数，可能导致不正确的输出。
   - **监听代码**：某些指令可能被用来记录或监视敏感数据或参数。
   - **溢出**：指令或操作数的输入或输出长度与PLC预期的不匹配，这可能是由于编程技能不足或恶意攻击操纵参数所致。
   - **重复指令**：在多个梯级中重复某些指令可能导致它们的值不可预测，影响逻辑代码和控制过程。
   - **未使用的标签**：在控制器数据库中定义的未使用标签可能增加威胁级别。
   - **缺少某些线圈或指令**：可能导致不良行为，用户可以利用这种情况进行恶意攻击。
   - **绕过指令**：通过空的并行分支绕过指令，影响梯级条件输出。
   - **硬编码值**：在某些情况下，使用硬编码参数可能增加漏洞。
   - **竞赛条件**：错误放置的分支、调用或指令可能导致不一致的结果。
   - **编译器警告**：PLC程序员通常会关注编译错误，但经常忽视警告。
   - **拒绝服务（DoS）**：通过PLC逻辑代码中的恶意代码或不当编程，可以使PLC崩溃。

3. **PLC代码漏洞的严重性**：文章强调，PLC代码中的漏洞可能导致严重后果，包括设备损坏、生产中断甚至对环境和人类生命构成威胁。

这一部分强调了PLC编程实践中的安全重要性，并指出了PLC代码中可能存在的各种漏洞，以及这些漏洞可能被利用的方式。作者提醒读者，为了确保工业控制系统的安全性，需要对PLC代码的安全性给予足够的重视。

Incomplete faults or alarms handling: a malicious code can disable or silent certain alarms. Basically, the manipulated logic code does not handle or scan all critical faults, alarms, related logic code, or parameters. By that operators would not notice the problem since a malicious code is going stealthy and unnoticed way; i.e. recognizing threats after the damage occurs [17]. 这一段讲的是什么意思？

这段内容讨论的是PLC（可编程逻辑控制器）代码中存在的一类安全漏洞，即不完整的故障或报警处理。下面是对这段内容的详细解释：

1. **不完整的故障或报警处理**：这意味着PLC程序中可能存在缺陷，它不能妥善处理或记录所有的故障情况或报警信号。

2. **恶意代码的风险**：如果PLC被恶意代码攻击，这段代码可能会禁用或使某些报警信号静默，即不向操作员发出警告。

3. **操纵逻辑代码**：攻击者可能会操纵PLC的逻辑代码，使得它故意忽略或不扫描关键的故障、报警、相关的逻辑代码或参数。

4. **隐蔽性**：恶意代码可能以一种隐蔽且不易被察觉的方式操作，使得操作人员难以发现问题。这种隐蔽性意味着只有在损害发生后，问题才可能被认识到。

5. **后果**：由于故障或报警没有得到妥善处理，操作员可能无法及时得知系统出现了问题，这可能导致无法预防的损害或事故。

文章中引用的[17]很可能是参考文献或脚注，提供了关于这一主题更深入的分析或案例研究。

总的来说，这段内容强调了PLC编程中需要考虑的一个重要安全方面，即确保所有的故障和报警都能被正确处理和记录，以避免潜在的安全风险。

Fake outcomes: occurs when PLC code skips certain rungs or parameters; e.g. improper usage of MCRs (Master Control Reset) which normally used to disre-
gard non-retentive instructions once enabled.


这段话讨论的是PLC（可编程逻辑控制器）代码中的一个特定类型的漏洞，称为“伪造结果”（Fake outcomes）。这通常发生在PLC程序的逻辑中故意或意外地忽略了某些梯级（rungs）或参数时。

在PLC编程中，"梯级"（rungs）是梯形图（Ladder diagram）中的一个概念，梯形图是IEC 61131标准中定义的一种图形化的编程语言。每个梯级包含一系列的逻辑操作，它们通常从左到右排列，表示控制逻辑的不同部分。当PLC执行梯形图时，它会从左到右评估每个梯级，以确定哪些输出应该被激活。

"跳过某些梯级"（skips certain rungs）意味着在PLC程序执行过程中，某些梯级没有被正确地评估或执行。这可能是因为编程错误或恶意代码故意设计为忽略这些梯级。

MCRs（主控制复位，Master Control Reset）是一种通常用于复位或禁用非保持（non-retentive）指令的机制。非保持指令是指那些不需要保持其状态，一旦条件不再满足就会自动重置的指令。如果MCR被不当使用，它可能会导致某些指令被错误地忽略，即使它们应该被执行。

因此，当PLC代码跳过梯级或不当使用MCR时，可能会导致"伪造结果"，即PLC的输出或行为与预期或逻辑设计不符，这可能会导致设备控制错误，进而可能引发安全问题或操作故障。

Snooping code: a user can utilize certain instructions, such as “ADD ON” instruction, that can be exploited to log or monitor some sensitive data or parameters. Those instructions can be added to any logic code and
go unnoticed. 这一段讲的是什么意思

这段内容讨论的是PLC（可编程逻辑控制器）代码中的“窃听代码”（Snooping code）问题，它指的是PLC程序中可能被滥用来监控或记录敏感数据的特定指令。以下是对这段内容的详细解释：

1. **窃听代码**：这是指PLC程序中可能包含的某些指令，它们可以被用来记录或监视敏感的系统数据或参数。

2. **利用特定指令**：文章中提到的“ADD ON”指令是一个例子，这种指令可以被用来执行数据记录或监视的操作。

3. **滥用风险**：如果攻击者或未授权用户能够访问PLC程序，他们可能会添加这类指令到逻辑代码中，以便在不被察觉的情况下监视或记录敏感操作。

4. **隐蔽性**：这些被添加的指令可能设计得足够隐蔽，以至于它们可以在逻辑代码中存在而不易被发现。

5. **安全风险**：由于这些窃听指令的存在，敏感数据可能会被未授权访问，这可能危害系统的安全性和保密性。

6. **监控和记录**：通过这种方式，攻击者可以监控PLC的运行状态，记录操作数据，甚至可能操纵工业过程。

这段内容强调了PLC编程和操作中需要考虑的安全性问题，即不仅要保护PLC免受外部攻击，还要防止内部人员滥用权限来威胁系统的安全。因此，需要采取适当的安全措施来监控和控制对PLC代码的访问和修改，以确保系统的完整性和安全性。


Overflow: occurs when an instruction or an operand
parameter length of input or output do not match what the PLC is expecting. That usually occurs because of unskilled programmers or when a malicious attack manipulates parameters.

这段内容讨论的是PLC（可编程逻辑控制器）程序中可能发生的“溢出”（Overflow）问题。以下是对这段内容的详细解释：

1. **溢出的定义**：溢出是指当指令或操作数（指令的一个组成部分，可以是数据或变量）的参数长度与PLC预期的不匹配时发生的情况。

2. **发生原因**：
   - **编程技能不足**：由于程序员缺乏经验或技能，可能在编写PLC程序时没有正确设置输入或输出参数的长度。
   - **恶意攻击操纵参数**：攻击者可能故意操纵PLC程序中的参数，导致输入或输出的数据超出PLC能够处理的范围。

3. **后果**：当发生溢出时，PLC可能无法正确处理数据，这可能导致程序错误、系统崩溃或其他意外行为，进而可能引发安全问题或影响工业过程的正常运行。

4. **安全风险**：溢出问题如果被恶意利用，可以成为攻击工业控制系统的一种手段，攻击者可以通过这种方式干扰PLC的正常操作。

这段内容强调了在PLC编程时需要准确设置参数的重要性，以及需要保护PLC程序不受恶意攻击的影响，以确保整个控制系统的稳定性和安全性。


Duplicated instructions: For some instructions, as the one shown in Fig. 8, if they are duplicated in more than one rung, their values will be unpredictable, affecting the logic code and the process controlled by it. Also, that will make it harder to debug the code and find or identify the problem [17].

这段内容讨论的是PLC（可编程逻辑控制器）程序中“重复指令”（Duplicated instructions）的问题。以下是对这段内容的详细解释：

1. **重复指令问题**：当某些指令在PLC的梯形图（Ladder Diagram）中的多个梯级（rung）上重复出现时，可能会导致问题。

2. **影响**：这些重复的指令会使它们的值变得不可预测，因为PLC在执行时可能无法确定应该遵循哪个指令。这会影响逻辑代码的正确执行，进而影响PLC控制的过程。

3. **调试难度**：重复指令还会使得代码调试变得更加困难。当出现问题时，确定是哪个重复指令导致的问题会更加复杂，因为需要分析多个位置的相同指令。

4. **问题识别**：由于指令在多个梯级上重复，这使得查找和识别问题源头变得更加具有挑战性。

5. **图8的引用**：文章中提到的“如图8所示”（For some instructions, as the one shown in Fig. 8）意味着在文档中应该有一个图表（Fig. 8），它展示了这种重复指令的一个具体例子。

这段内容强调了在PLC编程时避免指令重复的重要性，因为这不仅可能导致控制逻辑的混乱，还可能增加维护和故障排除时的工作难度。正确的编程实践可以减少这类问题的发生，提高系统的可靠性和安全性。

Unused tags: defining tags in the controller database that are not used in the logic could increase the level of threats; especially if the tags are not driven by a well-defined ladder logic.

未使用的标签：在控制器数据库中定义的标签如果没有在逻辑中使用，可能会增加威胁等级；尤其是当这些标签没有被明确定义的梯形逻辑所驱动时。





在文章的 "3.2 PLC vulnerabilities" 部分，作者讨论了可编程逻辑控制器（PLC）本身存在的一些安全漏洞。以下是该部分的主要内容：

1. **PLC操作系统的脆弱性**：PLC运行商业操作系统，如VxWorks和OS-9，这些系统像其他已知的操作系统（如Linux或Windows）一样容易受到攻击。PLC没有设计为具有对威胁和攻击的弹性，因为它们资源有限，并且在设计上不安全。例如，PLC操作系统通常以最高权限运行，任务之间几乎没有内存保护。

2. **未限制的上传**：能够访问PLC的访问点允许用户上传任何恶意代码到PLC，操纵当前运行的代码，甚至上传新的固件。PLC通常不检查上传的代码是否来自经过验证的信任源，也没有能力知道上传的代码是否是恶意的。

3. **未锁定模式**：PLC大多数时候是未锁定的，并且没有受到密码保护。这将允许他人访问正在运行的逻辑代码，监控标签，操纵代码，甚至下载一个完全错误或无关的逻辑。

4. **PLC代码可能被恶意软件利用**：恶意软件可以利用PLC代码对同一网络上的其他PLC发起攻击。

5. **PLC固件和软件的更新问题**：PLC的操作系统通常不频繁更新或修补，因为它们的网络是隔离的或有限的，固件不可升级。此外，PLC固件和软件的漏洞报告和解决存在困难，因为PLC可能不直接连接到供应商的网络或互联网。

6. **漏洞报告的缺乏**：由于网络隔离、未记录的问题或难以追踪的威胁，PLC的漏洞没有得到适当的解决和广泛报告。

这一部分强调了PLC在设计和实施时面临的安全挑战，以及需要采取的安全措施来保护这些关键的工业控制系统免受潜在的网络攻击和威胁。


在文章的 "3.3 HMIs and DTUs vulnerabilities" 部分，作者探讨了人机界面（HMIs）和显示终端单元（DTUs）所面临的安全漏洞。以下是该部分的主要内容：

1. **远程访问和网络互联**：随着HMIs和DTUs越来越能够远程访问和与其他网络及设备互联，它们变得更易受攻击，吸引了更多的黑客和威胁。

2. **操作系统的通用性**：像其他计算机一样，HMIs和DTUs运行在通用操作系统上，例如Windows OS、ActiveX、Java等。这使得它们容易受到网络中存在的任何威胁，并且继承了所使用操作系统的所有漏洞。

3. **软件产品的通用性**：HMIs已经成为通用的或现成的软件产品，它们建立在或共享普通计算机或IT系统的架构。这种通用性使得HMIs成为更易受攻击的设备，攻击者可能将它们视为网络上的普通PC或另一个易受攻击的操作系统。

4. **软件攻击**：软件攻击可以利用不安全的网络或感染的设备来操纵软件或窃取机密信息。以下是一些软件攻击的例子：
   - **外部恶意软件**：可以通过互联网、公司网络或用户本地部署，例如将感染的USB插入HMI、服务器或连接到PLC-BS网络的PC。
   - **欺骗攻击**：包括错误的未授权命令发送设备身份，可能启用远程访问并造成软件和硬件的严重损害。
   - **SQL注入**：影响基于Web的HMIs和具有数据库应用程序的服务器，攻击者可以通过在查询中插入意外的SQL语句来控制系统或操纵数据库。

这一部分强调了HMIs和DTUs由于其日益增长的远程访问能力和网络互联性，使得它们成为了攻击者的目标。作者提醒读者，为了确保工业控制系统的安全性，需要对HMIs和DTUs的安全性给予足够的重视，并采取适当的安全措施来保护这些关键接口设备免受潜在的网络攻击和威胁。


在文章的 "3.4 Field devices vulnerabilities" 部分，作者讨论了现场设备（Field devices）的安全漏洞，这些设备是与PLC系统直接交互的硬件组件。以下是该部分的主要内容：

1. **输入/输出的伪造**：现场设备的漏洞主要来自于可能被操纵的硬件状态——输入（如传感器的状态、参数或值）或命令——输出。当物理设备的值被伪造或被发送/接收虚假信号时，就会发生威胁。

2. **对PLC-BS完整性和可靠性的威胁**：通过伪造输入或输出，攻击者可以欺骗PLC，导致不希望的梯形逻辑程序结果，这可能会危及设备、生产力、环境和人类生命。

3. **不修改PLC逻辑代码或固件的威胁**：攻击者可以在不修改任何PLC逻辑代码或固件的情况下，通过破坏相关网络来实现攻击，这种方式难以被察觉。

4. **硬件设备的漏洞**：如果相关的PLC-BS程序被破坏，无论是HMI相关还是PLC相关的程序（如梯形逻辑代码或数据库），硬件设备也可能会受到漏洞的影响。

5. **硬件漏洞的总结**：
   - **伪造输入**：来自被破坏的传感器或输入设备的虚假状态、参数或值。
   - **伪造输出**：来自被破坏的执行器或现场设备的虚假状态、参数或值。
   - **通过破坏PLC、HMI或其他设备的数据完整性来操纵输入和输出值**。
   - **破坏PLC梯形逻辑代码或HMI程序，从而损坏硬件设备**，例如Stuxnet利用西门子软件操纵设备参数，导致关键硬件设备损坏。
   - **通过减慢PLC梯形逻辑代码或HMI程序的运行速度，严重影响生产或锁定生产**。
   - **停用报警和关键消息或警告**，延迟响应时间，使问题更难以被检测。

这一部分强调了现场设备在PLC-BS中的重要性以及它们面临的安全风险，指出了保护这些设备免受攻击的必要性，并解释了这些攻击可能对整个工业控制系统造成的影响。



在文章的 "3.6 Network segmentation vulnerabilities" 部分，作者讨论了工业控制系统（ICS）网络分段的安全漏洞。以下是该部分的主要内容：

1. **网络隔离的误区**：许多公司仍然认为，如果他们的工业网络与互联网隔离或不相连，那么网络就是安全和受保护的。一些人还认为，通过像图3所示的网络分段可以保持PLC网络的安全和保护。他们认为，通过空气隔离（air gapping）的工业网络可以保护所有的PLC和包括HMI在内的相关现场设备。

2. **网络分段的不足**：然而，仅仅通过分段工业控制系统网络并不足以提供充分的安全保障，原因如下：
   - **USB威胁**：恶意攻击可以通过感染的USB设备部署。
   - **继承性威胁**：恶意攻击可以通过连接到同一PLC-BS网络的另一台被感染的计算机或HMI传播。此外，如果PLC位于同一网络中，某些蠕虫可以从一个PLC传播到另一个PLC。
   - **不满的员工**：不满的员工可能会造成重大损害。他们可以破坏代码，感染HMIs或PCs，在梯形逻辑中编写潜伏的恶意代码，甚至向黑客开放某些端口。
   - **不良编程实践**：程序员可能会无意中编写可能会损坏某些机器或造成拒绝服务（DoS）的代码片段，例如无限循环。
   - **隐蔽访问**：一些漏洞可能需要数年时间才会被发现。它们的工作不是造成直接损害，而是为了窃听、收集和窃取敏感信息和数据。

3. **缺乏数据取证**：当攻击发生时，必须进行取证调查以确定攻击的原因和责任。通过分析和逆向工程所需的收集数据，可以更好地理解攻击的行为、元素、技术等。此外，可以通过取证来防止和阻止进一步的类似恶意攻击。

4. **取证的挑战**：然而，在PLC-BS中应用取证方法或工具存在困难，原因包括：
   - **连续性**：PLC-BS持续地从现场设备和I/O获取数据。它们主要是实时设备，不断用新信息更新；如果没有连续的增量备份，追溯以前的数据将会很困难。
   - **易失性**：运行程序和硬件的关键信息位于易失性内存中。例如，PLC没有适当的硬件和软件来记录详尽的代码或固件修改或更新。
   - **快速响应**：由于PLC-BS是实时设备，持续接收更新的新信息，延迟取证响应将使分析和追踪问题变得更加困难。响应越慢，易失性内存中存在的相关数据就越少；会被新数据覆盖。
   - **有效性和可用性**：作为实时系统，PLC-BS更关心数据的有效性、完整性和可用性，而不是安全性、加密或备份。减慢任何运行系统的扫描时间会造成不利问题。因此，使用任何可能减慢PLC-BS的工具或方法都是不可接受的。这使得嵌入任何典型的取证工具变得困难。

这一部分强调了网络分段虽然是一种常见的安全措施，但并不能提供足够的安全保障。同时，指出了取证在PLC-BS安全中的重要作用，以及在实施取证时所面临的挑战。
