# CLOAK: PV-aware Wear Leveling and Active Self-protection Mechanisms Against Flip Attacks on Non-Volatile Memories


&#160; &#160; &#160; &#160; CLOAK is a detection and defense mechanism to neutralize Flip Attacks. CLOAK leverages a novel wear leveling algorithm called CLIMBER to dynamically calibrate address mappings so that intensive writes to weak cells are redirected to strong cells.  CLIMBER also conceals weak NVM cells from attackers by randomly mapping cold addresses to weak NVM area. Moreover, CLOAK uses a new metric--hotness deviation to characterize violent fluctuations of write intensity on a memory address in two adjacent intervals, and thus can identify Flip Attacks efficiently. CLOAK then leverages an active self-protection scheme to defend Flip Attacks.


