---
title: Example 9 Detecting a Pool Memory Leak
description: Example 9 Detecting a Pool Memory Leak
ms.assetid: 3f634593-a024-46d1-9f3d-9d39b28bab03
keywords: ["PoolMon, PoolMon and GFlags"]
---

# Example 9: Detecting a Pool Memory Leak


## <span id="ddk_example_9___detecting_a_pool_memory_leak_dtools"></span><span id="DDK_EXAMPLE_9___DETECTING_A_POOL_MEMORY_LEAK_DTOOLS"></span>


The following example uses GFlags to set the system-wide [Enable pool tagging](enable-pool-tagging.md) flag in the registry. Then, it uses PoolMon (poolmon.exe), a tool in the Windows Driver Kit, to display the size of the memory pools.

PoolMon monitors the bytes in the paged and nonpaged memory pools and sorts them by pool tag. By running PoolMon periodically, you can identify pools that expand continuously over time. This pattern often indicates a memory leak.

**Note**   Pool tagging is permanently enabled in Windows Server 2003 and later versions of Windows. On these systems, the **Enable pool tagging** check box on the **Global Flags** dialog box is dimmed, and commands to enable or disable pool tagging fail.
If pool tagging is not enabled, PoolMon fails and displays the following message: "Query pooltags Failed c0000002."

 

**To detect a pool memory leak**

1.  To enable pool tagging for all processes in versions of Windows earlier than Windows Server 2003, set the system-wide [Enable pool tagging](enable-pool-tagging.md) flag in the registry. The following command line uses the flag abbreviation method, but you can identify the flag by its hexadecimal value or use the **Global Flags** dialog box:
    ```
    gflags /r +ptg 
    ```

2.  Restart the computer to make the registry change effective.

3.  Run PoolMon periodically by using the following command. In this command, the **/b** parameter sorts the pools in descending size order.

    ```
    poolmon /b 
    ```

    In response, PoolMon displays allocations from the memory pools in descending size order , including the number of allocate operations and free operations, and the amount of memory remaining in the pool (in the Bytes column).

    ```
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

    ```
    gflags /r -ptg 
    ```

5.  Restart Windows to make the registry change effective.

**Note**   Use the append symbol (**&gt;&gt;**) to redirect the PoolMon output to a log file. Later, you can examine the log file for pool size trends. For example:

 

```
poolmon.exe /b >> poolmon.log 
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Example%209:%20%20Detecting%20a%20Pool%20Memory%20Leak%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




