# CLOAK: PV-aware Wear Leveling and Active Self-protection Mechanisms Against Flip Attacks on Non-Volatile Memories


&#160; &#160; &#160; &#160; CLOAK is a detection and defense mechanism to neutralize Flip Attacks. CLOAK leverages a novel wear leveling algorithm called CLIMBER to dynamically calibrate address mappings so that intensive writes to weak cells are redirected to strong cells.  CLIMBER also conceals weak NVM cells from attackers by randomly mapping cold addresses to weak NVM area. Moreover, CLOAK uses a new metric--hotness deviation to characterize violent fluctuations of write intensity on a memory address in two adjacent intervals, and thus can identify Flip Attacks efficiently. CLOAK then leverages an active self-protection scheme to defend Flip Attacks.

CLOAK Setup,Compiling,Configuration and How to test
------------
**1.External Dependencies**  
&#160; &#160; &#160; &#160; Before install hybrid simulator CLOAK, it's essential that you have already install dependencies listing below.
* gcc(>=4.6)
* numactl-devel
* [libconfig](http://www.hyperrealm.com/libconfig/libconfig-1.5.tar.gz) or libconfig-devel
* kernel-devel
* python(>=2.7)
* PMU Toolkit (When you using Multicore version, it needs to be manually installed and configured) [Intel PMU profiling tools](https://github.com/andikleen/pmu-tools.git)

You can run 'sudo /scripts/install.sh' in order to automatically install some of these dependencies.

**2.Compiling**

* Compiling and Installation

First, Compiling the emulator's module. From the emulator's source code /Regular_version/HME folder, execute make.

```javascript
[root @node1 HME]# cd Regular_version
[root @node1 Regular_version]# cd HME
[root @node1 HME]# make  //to compiling the HME
```

* Update configuration
```javascript
11111
```

