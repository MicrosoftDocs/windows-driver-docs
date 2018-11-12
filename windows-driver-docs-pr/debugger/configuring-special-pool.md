---
title: Configuring Special Pool
description: Configuring Special Pool
ms.assetid: a6c90e88-8d67-47e8-8862-b7585a5d8bec
keywords: ["GFlags, configuring kernel special pool", "kernel special pool", "special pool", "pool tags and special pool"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Configuring Special Pool


## <span id="ddk_configuring_kernel_special_pool_dtools"></span><span id="DDK_CONFIGURING_KERNEL_SPECIAL_POOL_DTOOLS"></span>


The Gflags *Special Pool* feature directs Windows to request memory allocations from a reserved memory pool when the memory is allocated with a specified pool tag or is within a specified size range.

For detailed information about this feature, see [Special Pool](special-pool.md).

In Windows Vista and later versions of Windows, you can configure the Special Pool feature as a system-wide registry setting or as a kernel flags setting that does not require a reboot. In earlier versions of Windows, Special Pool is available only as a registry setting.

In Windows Vista and later versions of Windows, you can also use the command line to request special pool by pool tag. For information, see [**GFlags Commands**](gflags-commands.md).

This section includes the following topics.

[Requesting Special Pool by Pool Tag](requesting-special-pool-by-pool-tag.md)

[Requesting Special Pool by Allocation Size](requesting-special-pool-by-allocation-size.md)

[Canceling Requests for Special Pool](canceling-requests-for-special-pool.md)

[Detecting Overruns and Underruns](detecting-overruns-and-underruns.md)

**Note**   Use *Driver Verifier* to request special pool for allocations by a particular driver. For more information, see the "Special Pool" topic in the "Driver Verifier" section of the Windows Driver Kit (WDK).

 

 

 





