---
title: PoolMon
description: PoolMon
ms.assetid: 3cda6297-0e6f-48d5-b9d9-670ccf102c86
keywords: ["PoolMon WDK", "Pool Monitor WDK", "pool tags WDK PoolMon", "Memory Pool Monitor WDK", "driver testing WDK , PoolMon", "testing drivers WDK , PoolMon", "allocation pool tags WDK PoolMon", "memory allocations WDK PoolMon", "displaying memory allocation data", "memory WDK PoolMon", "Terminal Services sessions WDK PoolMon", "tag files WDK PoolMon", "statistics WDK PoolMon", "status information WDK PoolMon"]
---

# PoolMon


## <span id="ddk_poolmon_tools"></span><span id="DDK_POOLMON_TOOLS"></span>


PoolMon (poolmon.exe), the Memory Pool Monitor, displays data that the operating system collects about memory allocations from the system paged and nonpaged kernel pools, and the memory pools used for Terminal Services sessions. The data is grouped by pool allocation tag.

Driver developers and testers often use PoolMon to detect memory leaks when they create a new driver, change the driver code, or stress the driver. You can also use PoolMon in each stage of testing to view the driver's patterns of allocation and free operations, and to reveal how much pool memory the driver is using at any given time.

The version of PoolMon described in this document is included in the \\Tools\\Other subdirectory of the Windows Driver Kit (WDK).

This topic includes:

[PoolMon Overview](poolmon-overview.md)

[PoolMon Requirements](poolmon-requirements.md)

[PoolMon Commands](poolmon-commands.md)

[PoolMon Display](poolmon-display.md)

[PoolMon Examples](poolmon-examples.md)

To use PoolMon on Microsoft Windows XP and earlier systems, you must enable *pool tagging*. On Windows Server 2003 and later versions of Windows, pool tagging is permanently enabled. For more information, see "Pool Tagging Requirement" in [PoolMon Requirements](poolmon-requirements.md).

PoolMon can display the names of the Windows components and commonly used drivers that assign each pool tag. This feature uses data from pooltag.txt, a file installed with PoolMon and with the Debugging Tools for Windows packages. Occasionally, Microsoft updates this file. To check for updates, go to the [Microsoft support](http://go.microsoft.com/fwlink/p/?linkid=8713) website and search for "pooltag.txt."

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20PoolMon%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




