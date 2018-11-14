---
title: Example 9 Detecting a Pool Memory Leak
description: Example 9 Detecting a Pool Memory Leak
ms.assetid: 3f634593-a024-46d1-9f3d-9d39b28bab03
keywords: ["PoolMon, PoolMon and GFlags"]
ms.author: domars
ms.date: 10/12/2018
ms.localizationpriority: medium
---

# Example 9: Detecting a Pool Memory Leak


## <span id="ddk_example_9___detecting_a_pool_memory_leak_dtools"></span><span id="DDK_EXAMPLE_9___DETECTING_A_POOL_MEMORY_LEAK_DTOOLS"></span>


The following example uses GFlags to set the system-wide [Enable pool tagging](enable-pool-tagging.md) flag in the registry. Then, it uses PoolMon (poolmon.exe), a tool in the Windows Driver Kit, to display the size of the memory pools.

PoolMon monitors the bytes in the paged and nonpaged memory pools and sorts them by pool tag. By running PoolMon periodically, you can identify pools that expand continuously over time. This pattern often indicates a memory leak.

**Note**   Pool tagging is permanently enabled in Windows Server 2003 and later versions of Windows. On these systems, the **Enable pool tagging** check box on the **Global Flags** dialog box is dimmed, and commands to enable or disable pool tagging fail.
If pool tagging is not enabled, PoolMon fails and displays the following message: "Query pooltags Failed c0000002."

 

**To detect a pool memory leak**

1.  To enable pool tagging for all processes in versions of Windows earlier than Windows Server 2003, set the system-wide [Enable pool tagging](enable-pool-tagging.md) flag in the registry. The following command line uses the flag abbreviation method, but you can identify the flag by its hexadecimal value or use the **Global Flags** dialog box:
    ```console
    gflags /r +ptg 
    ```

2.  Restart the computer to make the registry change effective.

3.  Run PoolMon periodically by using the following command. In this command, the **/b** parameter sorts the pools in descending size order.

    ```console
    poolmon /b 
    ```

    In response, PoolMon displays allocations from the memory pools in descending size order , including the number of allocate operations and free operations, and the amount of memory remaining in the pool (in the Bytes column).

    ```console
    Memory: 16224K Avail: 4564K PageFlts: 31 InRam Krnl: 684K P: 680K
     Commit: 24140K Limit: 24952K Peak: 24932K  Pool N: 744K P: 2180K

     Tag  Type    Allocs          Frees         Diff   Bytes      Per Alloc
    -----------------------------------------------------------------------

     CM   Paged    1283 (   0)    1002 (   0)    281 1377312 (     0) 4901
    Strg  Paged   10385 (  10)    6658 (   4)   3727  317952 (   512)   85
     Fat  Paged    6662 (   8)    4971 (   6)   1691  174560 (   128)  103
    MmSt  Paged     614 (   0)     441 (   0)    173   83456 (     0)  482
    ```

    If the value in the **Bytes** column for an allocation expands continuously for no obvious reason, there might be a memory leak in that pool.

4.  Clear the **Enable pool tagging** flag.

    The following command line uses the flag abbreviation method, but you can identify the flag by its hexadecimal value or use the **Global Flags** dialog box:

    ```console
    gflags /r -ptg 
    ```

5.  Restart Windows to make the registry change effective.

**Note**   Use the append symbol (**&gt;&gt;**) to redirect the PoolMon output to a log file. Later, you can examine the log file for pool size trends. For example:

 

```console
poolmon.exe /b >> poolmon.log 
```

 

 





