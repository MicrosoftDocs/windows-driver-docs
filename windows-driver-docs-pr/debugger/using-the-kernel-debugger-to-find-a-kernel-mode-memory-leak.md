---
title: Using the Kernel Debugger to Find a Kernel-Mode Memory Leak
description: Using the Kernel Debugger to Find a Kernel-Mode Memory Leak
ms.assetid: eeadd505-b887-498d-9369-877156526355
keywords: ["memory leak, kernel-mode, kernel debugger"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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
    ```
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
    ```
    kd> ed nt!poolhittag ' cbA' 
    ```

3.  To verify the current value of **PoolHitTag**, use the [**db (Display Memory)**](d--da--db--dc--dd--dd--df--dp--dq--du--dw--dw--dyb--dyd--display-memor.md) command:
    ```
    kd> db nt!poolhittag L4 
    820f2ba4  41 62 63 20           Abc  
    ```

4.  The debugger will break every time that pool is allocated or freed with the tag **Abc**. Each time the debugger breaks on one of these allocations or free operations, use the [**kb (Display Stack Backtrace)**](k--kb--kc--kd--kp--kp--kv--display-stack-backtrace-.md) debugger command to view the stack trace.

Using this procedure, you can determine which code resident in memory is overallocating pool with the tag **Abc**.

To clear the breakpoint, set **PoolHitTag** to zero:

```
kd> ed nt!poolhittag 0 
```

If there are several different places where memory with this tag is being allocated and these are in an application or driver that you have written, you can alter your source code to use unique tags for each of these allocations.

If you cannot recompile the program but you want to determine which one of several possible locations in the code is causing the leak, you can unassemble the code at each location and use the debugger to edit this code resident in memory so that each instance uses a distinct (and previously unused) pool tag. Then allow the system to run for several minutes or more. After some time has passed, break in again with the debugger and use the [**!poolfind**](-poolfind.md) extension to find all pool allocations associated with each of the new tags.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Using%20the%20Kernel%20Debugger%20to%20Find%20a%20Kernel-Mode%20Memory%20Leak%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




