# exercise3

poetry相关的问题

https://python-poetry.org/docs/basic-usage/#using-poetry-run


```shell
(exercise-3-FmDOITGo-py3.10) mmj@oslab-H170-PRO:~/Project/fuzzing/fuzzing-101-solutions/exercise-3$ which python
/home/mmj/.cache/pypoetry/virtualenvs/exercise-3-FmDOITGo-py3.10/bin/python
(exercise-3-FmDOITGo-py3.10) mmj@oslab-H170-PRO:~/Project/fuzzing/fuzzing-101-solutions/exercise-3$ python create-bootp.py 
Traceback (most recent call last):
  File "/home/mmj/Project/fuzzing/fuzzing-101-solutions/exercise-3/create-bootp.py", line 1, in <module>
    from scapy.all import *
ModuleNotFoundError: No module named 'scapy'
(exercise-3-FmDOITGo-py3.10) mmj@oslab-H170-PRO:~/Project/fuzzing/fuzzing-101-solutions/exercise-3$ which pip
/home/mmj/.cache/pypoetry/virtualenvs/exercise-3-FmDOITGo-py3.10/bin/pip
(exercise-3-FmDOITGo-py3.10) mmj@oslab-H170-PRO:~/Project/fuzzing/fuzzing-101-solutions/exercise-3$ pip install scapy
Collecting scapy
  Using cached scapy-2.5.0-py2.py3-none-any.whl
Installing collected packages: scapy
Successfully installed scapy-2.5.0
(exercise-3-FmDOITGo-py3.10) mmj@oslab-H170-PRO:~/Project/fuzzing/fuzzing-101-solutions/exercise-3$ which pip
/home/mmj/.cache/pypoetry/virtualenvs/exercise-3-FmDOITGo-py3.10/bin/pip
(exercise-3-FmDOITGo-py3.10) mmj@oslab-H170-PRO:~/Project/fuzzing/fuzzing-101-solutions/exercise-3$ python create-bootp.py 
(exercise-3-FmDOITGo-py3.10) mmj@oslab-H170-PRO:~/Project/fuzzing/fuzzing-101-solutions/exercise-3$ 

```

在过程中可能会出现报错：ModuleNotFoundError: No module named 'scapy'

https://python-poetry.org/docs/basic-usage/#using-poetry-run

参考以上文档，这种时候只需要先调用一下poetry shell把命令行调起来，然后再给虚拟环境的poetry安装scapy包，然后再来虚拟环境跑脚本就好了。

