# CodeforcesHelper

[![](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/JTJL/CodeforcesHelper/blob/master/LICENSE) 
[![Twitter](https://img.shields.io/badge/twitter-@JTJLever-green.svg?style=flat)](http://twitter.com/JTJLever)

CodeforcesHelper is a small tool for [codeforces](https://codeforces.com/) contest.

## Generate code template for each problem
You can simplily use this to generate:
```bash
python3 ContestGenerator.py -c 1097 -l c++17
```
use `-c` to specify the contest id and `-l` to specify the language you want to use(C++17 in default).
Also, you can add your own language template into template directory.

## Fetch sample tests from the contest
The script above will automatically fetch all the sample tests from the contest.

##  Generate test scripts for each problem
TODO