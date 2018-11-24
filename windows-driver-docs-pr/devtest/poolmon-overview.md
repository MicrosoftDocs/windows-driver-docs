---
title: PoolMon Overview
description: PoolMon Overview
ms.assetid: c540e156-f0ce-4ac2-88e3-2e199b513abe
keywords:
- PoolMon WDK , about PoolMon
- Memory Pool Monitor WDK , about Memory Pool Monitor
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# PoolMon Overview


## <span id="ddk_poolmon_overview_tools"></span><span id="DDK_POOLMON_OVERVIEW_TOOLS"></span>


PoolMon displays the following data about memory allocations. The data is sorted by the allocations' pool tags.

-   The number of allocation operations and free operations (and unfreed memory allocations).

-   The change in the number of allocation operations and free operations between updates.

-   The total size of memory allocations by tag, in bytes used, and the average allocation size.

-   The change in bytes used between updates.

-   The drivers that assign the tag value.

PoolMon also displays general memory information, including total and available memory, page faults, kernel physical memory, committed memory and the commit limit, peak memory, and the size of the paged and nonpaged pools.

Using PoolMon, you can also:

-   Sort and reconfigure the PoolMon display while it is running.

-   Save configured data to a file.

-   Generate a file of the tags used by drivers on the local system (32-bit Windows only).

 

 





