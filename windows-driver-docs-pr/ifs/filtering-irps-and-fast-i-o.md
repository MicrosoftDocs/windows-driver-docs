---
title: Filtering IRPs and Fast I/O
author: windows-driver-content
description: Filtering IRPs and Fast I/O
ms.assetid: fad124b0-525d-4ff9-8f2c-3817fc76685c
keywords:
- filter drivers WDK file system , IRP filtering
- file system filter drivers WDK , IRP filtering
- IRPs WDK file system
- filtering IRPs WDK file system
- filtering fast I/O WDK file system
- fast I/O filtering WDK file system
- I/O WDK file systems
- dispatch routines WDK file system
- I/O requests WDK file system
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Filtering IRPs and Fast I/O


## <span id="ddk_filtering_irps_and_fast_io_if"></span><span id="DDK_FILTERING_IRPS_AND_FAST_IO_IF"></span>


<div class="alert">
<strong>Note</strong>   For optimal reliability and performance, we recommend using [file system minifilter drivers](filter-manager-and-minifilter-driver-architecture.md) instead of legacy file system filter drivers. Also, legacy file system filter drivers can’t attach to direct access (DAX) volumes. For more about file system minifilter drivers, see [Advantages of the Filter Manager Model](advantages-of-the-filter-manager-model.md). To port your legacy driver to a minifilter driver, see [Guidelines for Porting Legacy Filter Drivers](guidelines-for-porting-legacy-filter-drivers.md).
</div>
 

A file system filter driver filters I/O requests for one or more file systems or file system volumes. Each I/O request appears as an I/O request packet (IRP) or fast I/O request. IRPs are I/O system structures that are handled by a driver's IRP dispatch routines. Fast I/O requests are handled by the driver's fast I/O callback routines.

When a filter driver is initialized, its **DriverEntry** routine registers the filter driver's IRP dispatch routines and fast I/O callback routines. Only one set of these routines can be registered for each filter driver.

Some types of IRPs have fast I/O equivalents, and some fast I/O requests have IRP equivalents. However, IRPs handle many types of I/O that fast I/O cannot. Also, certain specialized fast I/O routines are used to preacquire file system resources for the Cache Manager or Memory Manager without creating an IRP. Thus, for the most part, IRPs and fast I/O requests perform separate roles in I/O operations.

This section covers the following topics:

[IRPs Are Different From Fast I/O](irps-are-different-from-fast-i-o.md)

[Types of File System Filter Driver Device Objects](types-of-device-objects-used-by-file-system-filter-drivers.md)

 

 


--------------------


