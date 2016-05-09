---
title: Filtering IRPs and Fast I/O
author: windows-driver-content
description: Filtering IRPs and Fast I/O
ms.assetid: fad124b0-525d-4ff9-8f2c-3817fc76685c
keywords: ["filter drivers WDK file system , IRP filtering", "file system filter drivers WDK , IRP filtering", "IRPs WDK file system", "filtering IRPs WDK file system", "filtering fast I/O WDK file system", "fast I/O filtering WDK file system", "I/O WDK file systems", "dispatch routines WDK file system", "I/O requests WDK file system"]
---

# Filtering IRPs and Fast I/O


## <span id="ddk_filtering_irps_and_fast_io_if"></span><span id="DDK_FILTERING_IRPS_AND_FAST_IO_IF"></span>


**Note**  For optimal reliability and performance, we recommend using [file system minifilter drivers](filter-manager-and-minifilter-driver-architecture.md) instead of legacy file system filter drivers. Also, legacy file system filter drivers can’t attach to direct access (DAX) volumes. For more about file system minifilter drivers, see [Advantages of the Filter Manager Model](advantages-of-the-filter-manager-model.md). To port your legacy driver to a minifilter driver, see [Guidelines for Porting Legacy Filter Drivers](guidelines-for-porting-legacy-filter-drivers.md).

 

A file system filter driver filters I/O requests for one or more file systems or file system volumes. Each I/O request appears as an I/O request packet (IRP) or fast I/O request. IRPs are I/O system structures that are handled by a driver's IRP dispatch routines. Fast I/O requests are handled by the driver's fast I/O callback routines.

When a filter driver is initialized, its **DriverEntry** routine registers the filter driver's IRP dispatch routines and fast I/O callback routines. Only one set of these routines can be registered for each filter driver.

Some types of IRPs have fast I/O equivalents, and some fast I/O requests have IRP equivalents. However, IRPs handle many types of I/O that fast I/O cannot. Also, certain specialized fast I/O routines are used to preacquire file system resources for the Cache Manager or Memory Manager without creating an IRP. Thus, for the most part, IRPs and fast I/O requests perform separate roles in I/O operations.

This section covers the following topics:

[IRPs Are Different From Fast I/O](irps-are-different-from-fast-i-o.md)

[Types of File System Filter Driver Device Objects](types-of-device-objects-used-by-file-system-filter-drivers.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Filtering%20IRPs%20and%20Fast%20I/O%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


