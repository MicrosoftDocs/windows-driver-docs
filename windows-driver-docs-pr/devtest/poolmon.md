---
title: PoolMon - Overview
description: Review an overview of PoolMon, the Memory Pool Monitor, and find links to articles with more information.
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
ms.date: 07/10/2025
---

# PoolMon

PoolMon (`poolmon.exe`), the Memory Pool Monitor, displays data that the operating system collects about memory allocations from the system paged and nonpaged kernel pools, and the memory pools used for Terminal Services sessions. The data is grouped according to the pool allocation tag.

Driver developers and testers often use PoolMon to detect memory leaks when they create a new driver, change the driver code, or stress the driver. You can also use PoolMon in each stage of testing to view the driver's patterns of allocation and free operations, and to reveal how much pool memory the driver is using at any given time.

PoolMon is included in the _\Tools\Other_ subdirectory of the [Windows Driver Kit (WDK)](../download-the-wdk.md).

The following articles provide more information about PoolMon:

- [PoolMon Overview](poolmon-overview.md)

- [PoolMon Requirements](poolmon-requirements.md)

- [PoolMon Commands](poolmon-commands.md)

- [PoolMon Display](poolmon-display.md)

- [PoolMon Examples](poolmon-examples.md)

PoolMon can display the names of the Windows components and commonly used drivers that assign each pool tag. This feature uses data from the _pooltag.txt_ file installed with PoolMon and with the Debugging Tools for Windows packages.