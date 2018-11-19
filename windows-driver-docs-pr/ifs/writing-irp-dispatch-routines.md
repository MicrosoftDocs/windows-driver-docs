---
title: Writing IRP Dispatch Routines
description: Writing IRP Dispatch Routines
ms.assetid: 8ce88932-cba6-4261-a938-d38133c20355
keywords:
- filter drivers WDK file system , IRP dispatch routines
- file system filter drivers WDK , IRP dispatch routines
- dispatch routines WDK file system
- IRP dispatch routines WDK file system
- writing IRP dispatch routines
- IRP dispatch routines WDK file system , about writing IRP dispatch routines
- IRPs WDK file system
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Writing IRP Dispatch Routines


## <span id="ddk_writing_irp_dispatch_routines_if"></span><span id="DDK_WRITING_IRP_DISPATCH_ROUTINES_IF"></span>


<div class="alert">
<strong>Note</strong>   For optimal reliability and performance, we recommend using <a href="filter-manager-and-minifilter-driver-architecture.md" data-raw-source="[file system minifilter drivers](filter-manager-and-minifilter-driver-architecture.md)">file system minifilter drivers</a> instead of legacy file system filter drivers. Also, legacy file system filter drivers can’t attach to direct access (DAX) volumes. For more about file system minifilter drivers, see <a href="advantages-of-the-filter-manager-model.md" data-raw-source="[Advantages of the Filter Manager Model](advantages-of-the-filter-manager-model.md)">Advantages of the Filter Manager Model</a>. To port your legacy driver to a minifilter driver, see <a href="guidelines-for-porting-legacy-filter-drivers.md" data-raw-source="[Guidelines for Porting Legacy Filter Drivers](guidelines-for-porting-legacy-filter-drivers.md)">Guidelines for Porting Legacy Filter Drivers</a>.
</div>
 

File system filter drivers use dispatch routines that are similar to those used in device drivers. A *dispatch routine* handles one or more types of IRPs. (The *type* of an IRP is determined by its major function code.) The driver's [DriverEntry](initializing-a-file-system-filter-driver.md) routine *registers* dispatch routine entry points by storing them in the driver object's dispatch table. When an IRP is sent to the driver, the I/O subsystem calls the appropriate dispatch routine based on the IRP's major function code.

Every IRP dispatch routine is defined as follows:

```cpp
NTSTATUS 
(*PDRIVER_DISPATCH) ( 
    IN PDEVICE_OBJECT DeviceObject, 
    IN PIRP Irp 
    ); 
```

File system filter driver dispatch routines are most often called at IRQL PASSIVE\_LEVEL, in the context of the thread that originated the I/O request, which is commonly a user-mode application thread. However, there are some exceptions to this rule. For example, page faults cause read and write dispatch routines to be called at IRQL APC\_LEVEL. These exceptions are summarized in a table in [Dispatch Routine IRQL and Thread Context](dispatch-routine-irql-and-thread-context.md). Unfortunately, it is not currently possible to prevent drivers in the filter chain from calling [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336) at IRQL &gt; PASSIVE\_LEVEL (for example, by failing to release a spinlock or fast mutex). Nevertheless, it is strongly recommended that filter dispatch routines always call **IoCallDriver** at the same IRQL at which they were called.

Dispatch routines can be made pageable, provided that they meet the criteria described in the [Making Drivers Pageable](https://msdn.microsoft.com/library/windows/hardware/ff554346) section of the Kernel-Mode Driver Architecture Design Guide.

If a file system filter driver has a control device object (CDO), its dispatch routines must be able to detect and handle cases where the IRP's target device object is the CDO rather than a volume device object (VDO) for a mounted volume. For more information about the CDO, see [The Filter Driver's Control Device Object](the-filter-driver-s-control-device-object.md).

This section discusses the following topics:

[Completing the IRP](completing-the-irp.md)

[Passing the IRP Down to Lower-Level Drivers](passing-the-irp-down-to-lower-level-drivers.md)

[Returning Status from Dispatch Routines](returning-status-from-dispatch-routines.md)

[Example: Passing the IRP Down Without Setting a Completion Routine](example--passing-the-irp-down-without-setting-a-completion-routine.md)

[Constraints on Dispatch Routines](constraints-on-dispatch-routines.md)

[Dispatch Routine IRQL and Thread Context](dispatch-routine-irql-and-thread-context.md)

 

 




