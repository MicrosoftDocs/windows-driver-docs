---
title: PoolMon Overview
description: PoolMon Overview
ms.assetid: c540e156-f0ce-4ac2-88e3-2e199b513abe
keywords: ["PoolMon WDK , about PoolMon", "Memory Pool Monitor WDK , about Memory Pool Monitor"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20PoolMon%20Overview%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




