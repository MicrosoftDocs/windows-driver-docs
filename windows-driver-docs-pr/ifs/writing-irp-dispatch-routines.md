---
title: Writing IRP Dispatch Routines
description: Writing IRP Dispatch Routines
keywords:
- filter drivers WDK file system , IRP dispatch routines
- file system filter drivers WDK , IRP dispatch routines
- dispatch routines WDK file system
- IRP dispatch routines WDK file system
- writing IRP dispatch routines
- IRP dispatch routines WDK file system , about writing IRP dispatch routines
- IRPs WDK file system
ms.date: 04/20/2017
---

# Writing IRP Dispatch Routines

> [!NOTE]
> For optimal reliability and performance, use [file system minifilter drivers](./filter-manager-concepts.md) with Filter Manager support instead of legacy file system filter drivers. To port your legacy driver to a minifilter driver, see [Guidelines for Porting Legacy Filter Drivers](guidelines-for-porting-legacy-filter-drivers.md).

File system filter drivers use dispatch routines that are similar to those used in device drivers. A *dispatch routine* handles one or more types of IRPs. (The *type* of an IRP is determined by its major function code.) The driver's [DriverEntry](initializing-a-file-system-filter-driver.md) routine *registers* dispatch routine entry points by storing them in the driver object's dispatch table. When an IRP is sent to the driver, the I/O subsystem calls the appropriate dispatch routine based on the IRP's major function code.

Every IRP dispatch routine is defined as follows:

```cpp
NTSTATUS
(*PDRIVER_DISPATCH) (
    IN PDEVICE_OBJECT DeviceObject,
    IN PIRP Irp
    );
```

File system filter driver dispatch routines are most often called at IRQL PASSIVE_LEVEL, in the context of the thread that originated the I/O request, which is commonly a user-mode application thread. However, there are some exceptions to this rule. For example, page faults cause read and write dispatch routines to be called at IRQL APC_LEVEL. These exceptions are summarized in a table in [Dispatch Routine IRQL and Thread Context](dispatch-routine-irql-and-thread-context.md). Unfortunately, it is not currently possible to prevent drivers in the filter chain from calling [**IoCallDriver**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocalldriver) at IRQL > PASSIVE_LEVEL (for example, by failing to release a spinlock or fast mutex). Nevertheless, it is strongly recommended that filter dispatch routines always call **IoCallDriver** at the same IRQL at which they were called.

Dispatch routines can be made pageable, provided that they meet the criteria described in the [Making Drivers Pageable](../kernel/making-drivers-pageable.md) section of the Kernel-Mode Driver Architecture Design Guide.

If a file system filter driver has a control device object (CDO), its dispatch routines must be able to detect and handle cases where the IRP's target device object is the CDO rather than a volume device object (VDO) for a mounted volume. For more information about the CDO, see [The Filter Driver's Control Device Object](the-filter-driver-s-control-device-object.md).

This section discusses the following topics:

[Completing the IRP](completing-the-irp.md)

[Passing the IRP Down to Lower-Level Drivers](passing-the-irp-down-to-lower-level-drivers.md)

[Returning Status from Dispatch Routines](returning-status-from-dispatch-routines.md)

[Example: Passing the IRP Down Without Setting a Completion Routine](example--passing-the-irp-down-without-setting-a-completion-routine.md)

[Constraints on Dispatch Routines](constraints-on-dispatch-routines.md)

[Dispatch Routine IRQL and Thread Context](dispatch-routine-irql-and-thread-context.md)
