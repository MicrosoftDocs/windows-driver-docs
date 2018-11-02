---
title: Using the Kernel Debugger to Find a Kernel-Mode Memory Leak
description: Using the Kernel Debugger to Find a Kernel-Mode Memory Leak
ms.assetid: eeadd505-b887-498d-9369-877156526355
keywords: ["memory leak, kernel-mode, kernel debugger"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Using the Kernel Debugger to Find a Kernel-Mode Memory Leak


The kernel debugger determines the precise location of a kernel-mode memory leak.

### <span id="enable_pool_tagging__windows_2000_and_windows_xp_"></span><span id="ENABLE_POOL_TAGGING__WINDOWS_2000_AND_WINDOWS_XP_"></span>Enable Pool Tagging (Windows 2000 and Windows XP)

On Windows 2000 and Windows XP, you must first use [GFlags](gflags.md) to enable pool tagging. GFlags is included in Debugging Tools for Windows. Start GFlags, choose the **System Registry** tab, check the **Enable Pool Tagging** box, and then click **Apply**. You must restart Windows for this setting to take effect.

On Windows Server 2003 and later versions of Windows, pool tagging is always enabled.

### <span id="determining_the_pool_tag_of_the_leak"></span><span id="DETERMINING_THE_POOL_TAG_OF_THE_LEAK"></span>Determining the Pool Tag of the Leak

To determine which pool tag is associated with the leak, it is usually easiest to use the PoolMon tool for this step. For details, see [Using PoolMon to Find Kernel-Mode Memory Leaks](using-poolmon-to-find-a-kernel-mode-memory-leak.md).

Alternatively, you can use the kernel debugger to look for tags associated with large pool allocations. To do so, follow this procedure:

1.  Reload all modules by using the [**.reload (Reload Module)**](-reload--reload-module-.md) command.

2.  Use the [**!poolused**](-poolused.md) extension. Include the flag "4" to sort the output by paged memory use:
    ```dbgcmd
    kd> !poolused 4 
    Sorting by Paged Pool Consumed

    Pool Used:
                NonPaged            Paged     
    Tag    Allocs     Used    Allocs     Used 
    Abc         0        0     36405 33930272 
    Tron        0        0       552  7863232 
    IoN7        0        0     10939   998432 
    Gla5        1      128      2222   924352 
    Ggb         0        0        22   828384 
    ```

3.  Determine which pool tag is associated with the greatest usage of memory. In this example, the driver using the tag "Abc" is using the most memory--almost 34 MB. Therefore, the memory leak is most likely to be in this driver.

### <span id="finding_the_leak"></span><span id="FINDING_THE_LEAK"></span>Finding the Leak

After you have determined the pool tag associated with the leak, follow this procedure to locate the leak itself:

1.  Use the [**ed (Enter Values)**](e--ea--eb--ed--ed--ef--ep--eq--eu--ew--eza--ezu--enter-values-.md) command to modify the value of the global system variable **PoolHitTag**. This global variable causes the debugger to break whenever a pool tag matching its value is used.

2.  Set **PoolHitTag** equal to the tag that you suspect to be the source of the memory leak. The module name "nt" should be specified for faster symbol resolution. The tag value must be entered in little-endian format (that is, backward). Because pool tags are always four characters, this tag is actually A-b-c-space, not merely A-b-c. So use the following command:
    ```dbgcmd
    kd> ed nt!poolhittag ' cbA' 
    ```

3.  To verify the current value of **PoolHitTag**, use the [**db (Display Memory)**](d--da--db--dc--dd--dd--df--dp--dq--du--dw--dw--dyb--dyd--display-memor.md) command:
    ```dbgcmd
    kd> db nt!poolhittag L4 
    820f2ba4  41 62 63 20           Abc  
    ```

4.  The debugger will break every time that pool is allocated or freed with the tag **Abc**. Each time the debugger breaks on one of these allocations or free operations, use the [**kb (Display Stack Backtrace)**](k--kb--kc--kd--kp--kp--kv--display-stack-backtrace-.md) debugger command to view the stack trace.

Using this procedure, you can determine which code resident in memory is overallocating pool with the tag **Abc**.

To clear the breakpoint, set **PoolHitTag** to zero:

```dbgcmd
kd> ed nt!poolhittag 0 
```

If there are several different places where memory with this tag is being allocated and these are in an application or driver that you have written, you can alter your source code to use unique tags for each of these allocations.

If you cannot recompile the program but you want to determine which one of several possible locations in the code is causing the leak, you can unassemble the code at each location and use the debugger to edit this code resident in memory so that each instance uses a distinct (and previously unused) pool tag. Then allow the system to run for several minutes or more. After some time has passed, break in again with the debugger and use the [**!poolfind**](-poolfind.md) extension to find all pool allocations associated with each of the new tags.

 

 





