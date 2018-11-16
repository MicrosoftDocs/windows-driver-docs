---
title: Network Redirector Design and Performance
description: Network Redirector Design and Performance
ms.assetid: 60ee4548-f81c-4d10-91ef-0e31e2837268
keywords:
- network redirectors WDK , performance
- redirector drivers WDK , performance
- performance WDK network redirectors
- run-to-the-wire approach WDK network redirectors
- bandwidth WDK network redirectors
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Network Redirector Design and Performance


## <span id="ddk_network_redirector_design_and_performance_if"></span><span id="DDK_NETWORK_REDIRECTOR_DESIGN_AND_PERFORMANCE_IF"></span>


There are two different paths to achieving high performance in a network redirector. The first approach stresses getting quickly to the network, above all else. The second approach tries to use sophisticated techniques for minimizing network operations; these operations are often time consuming and use up scarce network resources (available bandwidth, for example). Developers generally turn to the second approach when they are unsuccessful at the first.

While never discounting the benefit of short code paths, the "run-to-the-wire" approach provides better performance only when system operation does not encounter some fundamental bottleneck. For example, consider a 10 megabit Ethernet network where the actual transfer rate is limited to 1.25 MB/second. While this is faster than some disks, it is still considerably slower than memory access speeds. For this reason, a system that provides in-memory caching of data that is accessed frequently will provide better performance, in many cases, than one that does not. Conversely, performance may suffer if the network redirector on the client insists on trying to cache in unfavorable situations. For example, if the cache manager relies on the page granularity of the x86-based hardware, then this may mean that a full 4-KB block would be read and written in response to each 32-byte write that is initiated by the application. Clearly, to get the best performance, a network redirector must implement sophisticated cache management strategies, but must also be equally prepared to determine dynamically whether to use them. And, if caching is disabled, a network redirector must be prepared to run for the wire.

A second example is provided in the case of a CPU-saturated server. The performance of the remote file system may be significantly hampered if measures are not taken to relieve congestion at the server. For example, a server under saturation conditions may have a greater likelihood for dropping packets than an unloaded server. The client network redirector would be well advised to pace the packets sent in such a way as to reduce the probability of dropped packets. Even better, the redirector could take measures to attempt to combine several operations into a single packet. Combining operations so that the server gets more operations per packet is a win in the saturated server case.

Performance is also reduced when a system uses a networking mode that is inappropriate for the type of traffic and the likely network conditions. Experience suggests a possible correlation between using a datagram-based mode and having better performance for small I/O requests. It is not clear whether this improvement is across-the-board or whether it only applies in those scenarios where the probability of datagram delivery is very high. But the available data suggests that implementation of a "connectionless" mode is certainly worthwhile in addition to a connection-oriented mode. The ideal would be a network redirector where both modes would be supported by the network protocol and available for use, so the redirector could dynamically select how the traffic should be carried.

Finally, performance may be enhanced if appropriate data obtained during operations is available for making smart decisions. There are numerous examples of this in Windows. For example, Cache Manager keeps a short history of read commands and tracks cache hits and misses, which is used to guide decisions on read-ahead scheduling. A second example might be the use of "environmental information" for making decisions. There might be information available in the file name, the share name, or from a user or administrator that could greatly increase performance. For example, response can sometimes be tuned to improve performance by just changing cache size parameters to capture the data file being used. This "environmental knowledge" of access patterns for certain scenarios could potentially be used to suggest dynamic changes (hints) for improving performance.

 

 




