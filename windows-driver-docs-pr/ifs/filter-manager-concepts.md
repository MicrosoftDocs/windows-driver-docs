---
title: Filter Manager Concepts
description: Filter Manager Concepts
ms.assetid: 5b11671f-02fd-4d0e-8199-c345bbf2591c
keywords: ["filter manager WDK file system minifilter , about filter manager", "altitudes WDK file system minifilter", "filter manager WDK file system minifilter , architecture"]
---

# Filter Manager Concepts


## <span id="ddk_returning_status_from_a_minifilter_driverentry_routine_if"></span><span id="DDK_RETURNING_STATUS_FROM_A_MINIFILTER_DRIVERENTRY_ROUTINE_IF"></span>


The filter manager is installed with Windows, but it becomes active only when a minifilter driver is loaded. The filter manager attaches to the file system stack for a target volume. A minifilter driver attaches to the file system stack indirectly, by registering with the filter manager for the I/O operations the minifilter driver chooses to filter.

A legacy filter driver's position in the file system I/O stack relative to other filter drivers is determined at system startup by its load order group. For example, an antivirus filter driver should be higher in the stack than a replication filter driver, so it can detect viruses and disinfect files before they are replicated to remote servers. Therefore, filter drivers in the FSFilter Anti-Virus load order group are loaded before filter drivers in the FSFilter Replication group. Each load order group has a corresponding system-defined class and class GUID used in the INF file for the filter driver.

Like legacy filter drivers, minifilter drivers attach in a particular order. However, the order of attachment is determined by a unique identifier called an *altitude*. The attachment of a minifilter driver at a particular altitude on a particular volume is called an *instance* of the minifilter driver.

A minifilter driver's altitude ensures that the instance of the minifilter driver is always loaded at the appropriate location relative to other minifilter driver instances, and it determines the order in which the filter manager calls the minifilter driver to handle I/O. Altitudes are allocated and managed by Microsoft.

The following figure shows a simplified I/O stack with the filter manager and three minifilter drivers.

![diagram illustrating a simplified i/o stack with the filter manager and three minifilter drivers](images/filter-manager-architecture-1.gif)

A minifilter driver can filter IRP-based I/O operations as well as fast I/O and file system filter (FSFilter) callback operations. For each of the I/O operations it chooses to filter, a minifilter driver can register a [preoperation callback routine](writing-preoperation-and-postoperation-callback-routines.md), a postoperation callback routine, or both. When handling an I/O operation, the filter manager calls the appropriate callback routine for each minifilter driver that registered for that operation. When that callback routine returns, the filter manager calls the appropriate callback routine for the next minifilter driver that registered for the operation.

For example, assuming all three minifilter drivers in the above figure registered for the same I/O operation, the filter manager would call their preoperation callback routines in order of altitude from highest to lowest (A, B, C), then forward the I/O request to the next-lower driver for further processing. When the filter manager receives the I/O request for completion, it calls each minifilter driver's postoperation callback routines in reverse order, from lowest to highest (C, B, A).

For interoperability with legacy filter drivers, the filter manager can attach filter device objects to a file system I/O stack in more than one location. Each of the filter manager's filter device objects is called a *frame*. From the perspective of a legacy filter driver, each filter manager frame is just another legacy filter driver.

Each filter manager frame represents a range of altitudes. The filter manager can adjust an existing frame or create a new frame to allow minifilter drivers to attach at the correct location.

The filter manager cannot attach a minifilter between two attached legacy filters unless there is already a filter manager frame between them. If a minifilter is intended to be attached above a legacy filter, it can be attached below it, depending on the existence of a second attached legacy filter. A minifilter intended to be attached below a legacy filter could, instead, be attached above that legacy filter.

**Important**  Always verify interoperability of legacy filters with minifilters or consider replacing legacy filters with minifilters. For more information, see [Guidelines for Porting Legacy Filter Drivers](guidelines-for-porting-legacy-filter-drivers.md).

 

If a minifilter driver is unloaded and reloaded, it is reloaded at the same altitude in the same frame from which it was unloaded.

The following figure shows a simplified I/O stack with a two filter manager frames, minifilter driver instances, and a legacy filter driver.

![diagram illustrating a simplified i/o stack with two filter manager frames, minifilter driver instances, and a legacy filter driver](images/filter-manager-architecture-2.gif)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Filter%20Manager%20Concepts%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




