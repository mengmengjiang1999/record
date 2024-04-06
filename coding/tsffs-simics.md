# tsffs

1. 安装过程中报错

- ispm packages install的时候报的那个error，需要加上--trust-insecure-packages指令

ispm packages --install-bundle $HOME/Downloads/simics-6-packages.ispm --non-interactive --trust-insecure-packages

https://askubuntu.com/questions/13065/how-do-i-fix-the-gpg-error-no-pubkey

⬆️参考


2. 文档中的代码有一点点问题

- risc-v-simple中的run.simics代码


```
load-module tsffs
init-tsffs

tsffs.log-level 4
@tsffs.start_on_harness = True
@tsffs.stop_on_harness = True
@tsffs.timeout = 3.0
@tsffs.exceptions = [14]
```
需要修改成这样

3. load-target是什么意思

下面这一段代码会报错：找不到target。

```
load-target "qsp-x86/clear-linux" namespace = qsp machine:hardware:storage:disk1:image = "test.fs.craff"
```

搜索发现：

TSFFS initialized. Configure and use it as @tsffs.
Argument error: Non-existing target 'risc-v-simple/linux'
[/home/mmj/Project/riscv-project-fuzz/risc-v-kernel/project/run.simics:13] error in 'load-target' command
Error - interrupting script.

使用list-targets指令找出了所有target，发现并不存在risc-v-simple这种target。这个target是需要自己安装吗还是？

risc-v-simple的Image已经在正确的路径了，但是并没有被simisc识别为一个target。

但是看文档，我完全看不出来是load-target应该先使用还是list-targets应该先使用。

┌────────────────────────────────────┬────────────────────┐
│               Target               │      Package       │
├────────────────────────────────────┼────────────────────┤
│qsp-x86/clear-linux                 │Quick-Start Platform│
│qsp-x86/clear-linux-2c              │Quick-Start Platform│
│qsp-x86/clear-linux-multi           │Quick-Start Platform│
│qsp-x86/clear-linux-multi-no-network│Quick-Start Platform│
│qsp-x86/uefi-shell                  │Quick-Start Platform│
│qsp-x86/user-provided-linux         │Quick-Start Platform│
└────────────────────────────────────┴────────────────────┘

然后发现riscv相关的target根本没有在里面。查看文档发现，在创建project的时候，有这样一个指令：

```
ispm projects project --create 1000-latest 2096-latest 8112-latest 31337-latest \
  --ignore-existing-files
cd project
```

需要增加2050和2053，这个才是跟riscv相关的package。

```
ispm projects project --create 1000-latest 2096-latest 2050-latest 2053-latest 8112-latest 31337-latest \
  --ignore-existing-files
cd project
```