---
title: Example Passing the IRP Down Without Setting a Completion Routine
description: Example Passing the IRP Down Without Setting a Completion Routine
keywords:
- IRP dispatch routines WDK file system , passing IRP down
- passing IRPs down device stack WDK
ms.date: 02/23/2023
---

# Example: Passing the IRP Down Without Setting a Completion Routine

> [!NOTE]
> For optimal reliability and performance, use [file system minifilter drivers](./filter-manager-concepts.md) with Filter Manager support instead of legacy file system filter drivers. To port your legacy driver to a minifilter driver, see [Guidelines for Porting Legacy Filter Drivers](guidelines-for-porting-legacy-filter-drivers.md).

To pass the IRP down to lower-level drivers without setting a completion routine, a dispatch routine must do the following actions:

- Call [**IoSkipCurrentIrpStackLocation**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioskipcurrentirpstacklocation) to remove the current IRP stack location, so that the I/O Manager doesn't look for a completion routine there when it performs completion processing on the IRP.
- Call [**IoCallDriver**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocalldriver) to pass the IRP down to the next lower-level driver.

This technique is illustrated in the following code examples:

```cpp
IoSkipCurrentIrpStackLocation ( Irp ); 
return IoCallDriver ( NextLowerDriverDeviceObject, Irp ); 
```

Or, equivalently:

```cpp
IoSkipCurrentIrpStackLocation ( Irp ); 
status = IoCallDriver ( NextLowerDriverDeviceObject, Irp ); 
/* log or debugprint the status value here */
return status; 
```

In these examples, the first parameter in the call to [**IoCallDriver**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocalldriver) is a pointer to the next-lower-level filter driver's device object. The second parameter is a pointer to the IRP.

## Advantages of This Approach

Calling [**IoSkipCurrentIrpStackLocation**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioskipcurrentirpstacklocation) is simple and efficient and should be used in all cases where the driver passes the IRP down the driver stack without registering a completion routine.

## Disadvantages of This Approach

After [**IoCallDriver**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocalldriver) is called, the IRP pointer that was passed to **IoCallDriver** is no longer valid and can't safely be dereferenced. If the driver needs to perform further processing or cleanup after lower-level drivers have processed the IRP, it must set a completion routine before sending the IRP down the driver stack. For more information about writing and setting completion routines, see [Using Completion Routines](using-irp-completion-routines.md).

If you call [**IoSkipCurrentIrpStackLocation**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioskipcurrentirpstacklocation) for an IRP, you can't set a completion routine for it.
