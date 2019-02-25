---
title: Filtering IRPs and Fast I/O
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
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Filtering IRPs and Fast I/O


## <span id="ddk_filtering_irps_and_fast_io_if"></span><span id="DDK_FILTERING_IRPS_AND_FAST_IO_IF"></span>


<div class="alert">
<strong>Note</strong>   For optimal reliability and performance, we recommend using <a href="filter-manager-and-minifilter-driver-architecture.md" data-raw-source="[file system minifilter drivers](filter-manager-and-minifilter-driver-architecture.md)">file system minifilter drivers</a> instead of legacy file system filter drivers. Also, legacy file system filter drivers can’t attach to direct access (DAX) volumes. For more about file system minifilter drivers, see <a href="advantages-of-the-filter-manager-model.md" data-raw-source="[Advantages of the Filter Manager Model](advantages-of-the-filter-manager-model.md)">Advantages of the Filter Manager Model</a>. To port your legacy driver to a minifilter driver, see <a href="guidelines-for-porting-legacy-filter-drivers.md" data-raw-source="[Guidelines for Porting Legacy Filter Drivers](guidelines-for-porting-legacy-filter-drivers.md)">Guidelines for Porting Legacy Filter Drivers</a>.
</div>
 

A file system filter driver filters I/O requests for one or more file systems or file system volumes. Each I/O request appears as an I/O request packet (IRP) or fast I/O request. IRPs are I/O system structures that are handled by a driver's IRP dispatch routines. Fast I/O requests are handled by the driver's fast I/O callback routines.

When a filter driver is initialized, its **DriverEntry** routine registers the filter driver's IRP dispatch routines and fast I/O callback routines. Only one set of these routines can be registered for each filter driver.

Some types of IRPs have fast I/O equivalents, and some fast I/O requests have IRP equivalents. However, IRPs handle many types of I/O that fast I/O cannot. Also, certain specialized fast I/O routines are used to preacquire file system resources for the Cache Manager or Memory Manager without creating an IRP. Thus, for the most part, IRPs and fast I/O requests perform separate roles in I/O operations.

This section covers the following topics:

[IRPs Are Different From Fast I/O](irps-are-different-from-fast-i-o.md)

[Types of File System Filter Driver Device Objects](types-of-device-objects-used-by-file-system-filter-drivers.md)

 

 




