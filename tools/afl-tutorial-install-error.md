# afl-tutorial 安装报错问题记录

20240328

1. 
```
cannot find libcapstone.so.4
/usr/bin/ld 
（之类的）
```

我做的尝试大概是看了看make记录，然后在实际执行那个指令的地方手动加了几个软链接，但是发现没有任何用。后面查了查发现这个libcapstone.so.4并不是临时从项目里面某个文件夹里面编译出来的东西，而是一个比较常用的库。所以想到或许应该下载一个https://pkgs.org/download/libcapstone.so.4 到/usr/local/bin


2. 
```
instrumentation/afl-llvm-common.cc:12:10: fatal error: 'list' file not found
#include <list>
         ^~~~~~
1 error generated.
make[1]: *** [GNUmakefile.llvm:420: instrumentation/afl-llvm-common.o] Error 1
make[1]: Leaving directory '/home/mmj/Project/AFLplusplus'
make: [GNUmakefile:644: distrib] Error 2 (ignored)
```
解决方式：
```
clang++ --verbose
```
发现其实并没有clang，然后
```
sudo apt install clang
sudo apt install libstdc++-12-dev
```

然后work了。（虽然报了别的错）

参考：
https://github.com/AFLplusplus/LibAFL/issues/1098


3. 
```
/usr/bin/ld: final link failed: No space left on device
clang: error: linker command failed with exit code 1 (use -v to see invocation)
```
这个纯属个人习惯问题（不到磁盘爆炸完全不做清理orz）应该不会再有人遇到吧
（删删删ing
```
sudo du -h --max-depth=1
```


4. 
```
Successfully uninstalled unicornafl-2.1.0
Successfully installed unicorn-2.0.1.post1 unicornafl-2.1.0
[*] If needed, you can (re)install the bindings in `./unicornafl/bindings/python` using `pip install --force .`
[*] Unicornafl bindings installed successfully.
[*] Testing unicornafl python functionality by running a sample test harness
[+] Instrumentation tests passed. 
[+] Make sure to adapt older scripts to `import unicornafl` and use `uc.afl_forkserver_start`
    or `uc.afl_fuzz` to kick off fuzzing.
[+] All set, you can now use Unicorn mode (-U) in afl-fuzz!
```

总之最后./afl-fuzz -h之后可以输出预期结果了（虽然看起来还有别的错没解决，但是先这样吧）



# Fuzzer setup

到cargo build那一步会报错

```
   Compiling libafl v0.10.1
error[E0432]: unresolved import `core::simd::SimdOrd`
 --> /home/mmj/.cargo/registry/src/index.crates.io-6f17d22bba15001f/libafl-0.10.1/src/feedbacks/map.rs:8:5
  |
8 | use core::simd::SimdOrd;
  |     ^^^^^^^^^^^^^^^^^^^ no `SimdOrd` in `simd`
  |
help: consider importing one of these items instead
  |
8 | use core::simd::prelude::SimdOrd;
  |     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
8 | use crate::prelude::std::simd::prelude::SimdOrd;
  |     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
8 | use std::simd::prelude::SimdOrd;
```
类似这种的一系列错。这种情况不用看报错信息，只要把

> exercise-1/Cargo.toml

里面改成

```
[package]
name = "exercise-one-solution"
version = "0.1.0"
edition = "2021"
build = "build.rs"

[dependencies]
libafl = "0.11.2"
```

就可以了。


2. 不对好像还是哪里不太可以。不知道为什么

首先第一个问题，既然cargo build和直接执行那几个命令的效果一样，为啥不直接执行那几个命令（虽然我试了一下并不能这么做）然后第二个问题，cargo build之后并没有出现xpdf/install文件夹，这又是为什么？


我知道了。需要先查看xpdf的INSTALL文档

cargo build和实际执行下面这几个命令的效果是一样的：

```
cd fuzzing-101-solutions/exercise-1/xpdf
make clean
rm -rf install 
export LLVM_CONFIG=llvm-config-15
CC=afl-clang-fast CXX=afl-clang-fast++ ./configure --prefix=./install
make
make install
```
（虽然还是不太明白为什么需要cargo build）但是当我们查看xpdf的INSTALL文档我们会发现，在执行make命令之前需要先执行一下：

./configure

此外，xpdf还需要安装至少一个依赖就是Freetype2。


3. 关于cargo build
还是不太懂为什么需要这个cargo build。总之，决定放弃，并直接通过命令行来进行install

这一步说白了就是希望在xpdf/install目录下面安装这个有bug的xpdf版本。照着tutorial的命令行来走就可以。

不过在最后一步install的时候会报这个错：
configure: error: expected an absolute directory name for --prefix: ./install

这种时候只需要把--prefix:后面的路径换成绝对路径就好。

综上，方法是不用再管那个cargo build了，直接在命令行里输入：

```
cd fuzzing-101-solutions/exercise-1/xpdf
make clean
rm -rf install 
export LLVM_CONFIG=llvm-config-15
CC=/home/mmj/Project/AFLplusplus/afl-clang-fast CXX=/home/mmj/Project/AFLplusplus/afl-clang-fast++ ./configure --prefix=/home/mmj/Project/fuzzing-101-solutions/exercise-1/xpdf/install
make
make install
```

注意：因为在安装afl的时候并没有把afl-clang-fast之类的加入环境变量，所以这里指定编译器这些的时候需要手动设置成绝对路径。同理configure --prefix也需要设置成绝对路径

这样做完之后，install文件夹就符合预期了。不过不知道为什么中途会报很多很多很多个warning。


不过warning好像并不影响。另外先通过命令行的方式跑通一次之后，cargo build就是管用的了（好神奇qwq）


4. 关于RUNNING THE FUZZER这一步中BUILD THE FUZZER会报的错

cargo build --release

```
error[E0432]: unresolved import `libafl::bolts::rands`
 --> exercise-1/src/main.rs:1:20
  |
1 | use libafl::bolts::rands::StdRand;
  |                    ^^^^^ could not find `rands` in `bolts`

error[E0432]: unresolved import `libafl::bolts::shmem`
 --> exercise-1/src/main.rs:2:20
  |
2 | use libafl::bolts::shmem::{ShMem, ShMemProvider, StdShMemProvider};
  |                    ^^^^^ could not find `shmem` in `bolts`

error[E0432]: unresolved import `libafl::bolts::tuples`
 --> exercise-1/src/main.rs:3:20
  |
3 | use libafl::bolts::tuples::tuple_list;
  |                    ^^^^^^ could not find `tuples` in `bolts`

error[E0432]: unresolved imports `libafl::bolts::current_nanos`, `libafl::bolts::AsMutSlice`
 --> exercise-1/src/main.rs:4:21
  |
4 | use libafl::bolts::{current_nanos, AsMutSlice};
  |                     ^^^^^^^^^^^^^  ^^^^^^^^^^ no `AsMutSlice` in `bolts`
  |                     |
  |                     no `current_nanos` in `bolts`

```

这种情况是因为libafl这个包进行了一定的版本更新，需要修改cargo.toml为：

- libafl为最新版本
- 增加一个libafr_bolts

```
[package]
name = "exercise-one-solution"
version = "0.1.0"
edition = "2021"
build = "build.rs"

[dependencies]
libafl = "0.11.2"
libafl_bolts ="0.11.2"
```

然后应该就可以了。

另外还需要把代码里面原来用libafl::bolt等的地方换一下

