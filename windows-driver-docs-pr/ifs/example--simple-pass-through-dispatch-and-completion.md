---
title: Example Simple Pass-Through Dispatch and Completion
description: Example Simple Pass-Through Dispatch and Completion
keywords:
- IRP completion routines WDK file system , examples
ms.date: 02/23/2023
---

# Example: Simple Pass-Through Dispatch and Completion

> [!NOTE]
> For optimal reliability and performance, use [file system minifilter drivers](./filter-manager-concepts.md) with Filter Manager support instead of legacy file system filter drivers. To port your legacy driver to a minifilter driver, see [Guidelines for Porting Legacy Filter Drivers](guidelines-for-porting-legacy-filter-drivers.md).

To set a completion routine for an IRP and pass the IRP down, a legacy file system filter driver's dispatch routine must do the following actions:

- Call [**IoCopyCurrentIrpStackLocationToNext**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocopycurrentirpstacklocationtonext) to copy the parameters from the current stack location to that of the next-lower-level driver.

- Call [**IoSetCompletionRoutine**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iosetcompletionroutine) to designate a completion routine for the IRP.

- Call [**IoCallDriver**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocalldriver) to pass the IRP down to the next-lower-level driver.

This technique is illustrated in the following code example:

```cpp
IoCopyCurrentIrpStackLocationToNext( Irp ); 
IoSetCompletionRoutine( Irp,                                 // Irp
                        MyLegacyFilterPassThroughCompletion, // CompletionRoutine
                        (PVOID)recordList,                   // Context
                        TRUE,                                // InvokeOnSuccess
                        TRUE,                                // InvokeOnError
                        TRUE);                               // InvokeOnCancel
return IoCallDriver ( NextLowerDriverDeviceObject, Irp ); 
```

In this example, the call to [**IoSetCompletionRoutine**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iosetcompletionroutine) sets a completion routine for an IRP.

The first two parameters in the call to [**IoSetCompletionRoutine**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iosetcompletionroutine) are a pointer to the IRP and the name of the completion routine. The third parameter is a pointer to a driver-defined structure to be passed to the completion routine. This structure contains context information that the completion routine needs when it performs completion processing on the IRP. The context structure must be allocated from nonpaged pool, because the completion routine can be called at IRQL DISPATCH_LEVEL.

The last three parameters passed to [**IoSetCompletionRoutine**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iosetcompletionroutine) are flags that specify whether the completion routine is called when the I/O request succeeds, fails, or is canceled.

If a dispatch routine sets a completion routine and immediately returns after calling [**IoCallDriver**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocalldriver) (as shown in the previous dispatch routine), the corresponding completion routine must check the IRP's PendingReturned flag and, if it's set, call **IoMarkIrpPending**. Then it should return STATUS_SUCCESS, as shown in the following example:

```cpp
if (Irp->PendingReturned) {
    IoMarkIrpPending( Irp );
}
return STATUS_SUCCESS;
```

- Advantages of This Approach

  Setting a completion routine allows the driver to further process the IRP after lower-level drivers have processed it. The completion routine can decide how to process the IRP based on the outcome of the requested I/O operation.

- Disadvantages of This Approach

  Because it runs in an arbitrary thread context at IRQL <= DISPATCH_LEVEL, a completion routine can perform only limited processing on the IRP.
