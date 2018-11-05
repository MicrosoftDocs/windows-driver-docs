---
title: PoolMon
description: PoolMon
ms.assetid: 3cda6297-0e6f-48d5-b9d9-670ccf102c86
keywords:
- PoolMon WDK
- Pool Monitor WDK
- pool tags WDK PoolMon
- Memory Pool Monitor WDK
- driver testing WDK , PoolMon
- testing drivers WDK , PoolMon
- allocation pool tags WDK PoolMon
- memory allocations WDK PoolMon
- displaying memory allocation data
- memory WDK PoolMon
- Terminal Services sessions WDK PoolMon
- tag files WDK PoolMon
- statistics WDK PoolMon
- status information WDK PoolMon
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# PoolMon


## <span id="ddk_poolmon_tools"></span><span id="DDK_POOLMON_TOOLS"></span>


PoolMon (poolmon.exe), the Memory Pool Monitor, displays data that the operating system collects about memory allocations from the system paged and nonpaged kernel pools, and the memory pools used for Terminal Services sessions. The data is grouped by pool allocation tag.

Driver developers and testers often use PoolMon to detect memory leaks when they create a new driver, change the driver code, or stress the driver. You can also use PoolMon in each stage of testing to view the driver's patterns of allocation and free operations, and to reveal how much pool memory the driver is using at any given time.

The version of PoolMon described in this document is included in the \\Tools\\Other subdirectory of the [Windows Driver Kit (WDK)](https://go.microsoft.com/fwlink/p/?linkid=846744).

This topic includes:

[PoolMon Overview](poolmon-overview.md)

[PoolMon Requirements](poolmon-requirements.md)

[PoolMon Commands](poolmon-commands.md)

[PoolMon Display](poolmon-display.md)

[PoolMon Examples](poolmon-examples.md)

To use PoolMon on Microsoft Windows XP and earlier systems, you must enable *pool tagging*. On Windows Server 2003 and later versions of Windows, pool tagging is permanently enabled. For more information, see "Pool Tagging Requirement" in [PoolMon Requirements](poolmon-requirements.md).

PoolMon can display the names of the Windows components and commonly used drivers that assign each pool tag. This feature uses data from pooltag.txt, a file installed with PoolMon and with the Debugging Tools for Windows packages. Occasionally, Microsoft updates this file. To check for updates, go to the [Microsoft support](http://go.microsoft.com/fwlink/p/?linkid=8713) website and search for "pooltag.txt."

 

 





