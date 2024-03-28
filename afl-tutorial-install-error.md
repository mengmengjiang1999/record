# afl-tutorial 安装报错问题记录

20240328

1. 
cannot find libcapstone.so.4
/usr/bin/ld 

我做的尝试大概是看了看make记录，然后在实际执行那个指令的地方手动加了几个软链接，但是发现没有任何用。后面查了查发现这个libcapstone.so.4并不是临时从项目里面某个文件夹里面编译出来的东西，而是一个比较常用的库。所以想到或许应该下载一个https://pkgs.org/download/libcapstone.so.4 到/usr/local/bin


2. 
instrumentation/afl-llvm-common.cc:12:10: fatal error: 'list' file not found
#include <list>
         ^~~~~~
1 error generated.
make[1]: *** [GNUmakefile.llvm:420: instrumentation/afl-llvm-common.o] Error 1
make[1]: Leaving directory '/home/mmj/Project/AFLplusplus'
make: [GNUmakefile:644: distrib] Error 2 (ignored)

解决方式：
clang++ --verbose
发现其实并没有clang，然后
sudo apt install clang
sudo apt install libstdc++-12-dev

然后work了。（虽然报了别的错）

参考：
https://github.com/AFLplusplus/LibAFL/issues/1098


3. 
/usr/bin/ld: final link failed: No space left on device
clang: error: linker command failed with exit code 1 (use -v to see invocation)
这个纯属个人习惯问题（不到磁盘爆炸完全不做清理orz）应该不会再有人遇到吧
（删删删ing
sudo du -h --max-depth=1


4. 
Successfully uninstalled unicornafl-2.1.0
Successfully installed unicorn-2.0.1.post1 unicornafl-2.1.0
[*] If needed, you can (re)install the bindings in `./unicornafl/bindings/python` using `pip install --force .`
[*] Unicornafl bindings installed successfully.
[*] Testing unicornafl python functionality by running a sample test harness
[+] Instrumentation tests passed. 
[+] Make sure to adapt older scripts to `import unicornafl` and use `uc.afl_forkserver_start`
    or `uc.afl_fuzz` to kick off fuzzing.
[+] All set, you can now use Unicorn mode (-U) in afl-fuzz!


总之最后./afl-fuzz -h之后可以输出预期结果了

