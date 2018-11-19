---
title: Example Simple Pass-Through Dispatch and Completion
description: Example Simple Pass-Through Dispatch and Completion
ms.assetid: dae3a450-37b1-470b-a0f3-4108075e06ac
keywords:
- IRP completion routines WDK file system , examples
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Example: Simple Pass-Through Dispatch and Completion


## <span id="ddk_example_simple_pass_through_dispatch_and_completion_if"></span><span id="DDK_EXAMPLE_SIMPLE_PASS_THROUGH_DISPATCH_AND_COMPLETION_IF"></span>


To set a completion routine for an IRP and pass the IRP down, a dispatch routine must do the following:

-   Call [**IoCopyCurrentIrpStackLocationToNext**](https://msdn.microsoft.com/library/windows/hardware/ff548387) to copy the parameters from the current stack location to that of the next-lower-level driver.

-   Call [**IoSetCompletionRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff549679) to designate a completion routine for the IRP.

-   Call [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336) to pass the IRP down to the next-lower-level driver.

This technique is illustrated in the following code example:

### <span id="Dispatch_Routine"></span><span id="dispatch_routine"></span><span id="DISPATCH_ROUTINE"></span>Dispatch Routine

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

In this example, the call to [**IoSetCompletionRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff549679) sets a completion routine for an IRP.

The first two parameters in the call to [**IoSetCompletionRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff549679) are a pointer to the IRP and the name of the completion routine. The third parameter is a pointer to a driver-defined structure to be passed to the completion routine. This structure contains context information that the completion routine will need when it performs completion processing on the IRP. The context structure must be allocated from nonpaged pool, because the completion routine can be called at IRQL DISPATCH\_LEVEL.

The last three parameters passed to [**IoSetCompletionRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff549679) are flags that specify whether the completion routine is called when the I/O request succeeds, fails, or is canceled.

### <span id="Completion_Routine"></span><span id="completion_routine"></span><span id="COMPLETION_ROUTINE"></span>Completion Routine

If a dispatch routine sets a completion routine and immediately returns after calling [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336) (as shown in the above dispatch routine), the corresponding completion routine must check the IRP's PendingReturned flag and, if it is set, call **IoMarkIrpPending**. Then it should return STATUS\_SUCCESS, as shown in the following example:

```cpp
if (Irp->PendingReturned) {
    IoMarkIrpPending( Irp );
}
return STATUS_SUCCESS;
```

### <span id="Advantages_of_This_Approach"></span><span id="advantages_of_this_approach"></span><span id="ADVANTAGES_OF_THIS_APPROACH"></span>Advantages of This Approach

Setting a completion routine allows the driver to further process the IRP after it has been processed by lower-level drivers. The completion routine can decide how to process the IRP based on the outcome of the requested I/O operation.

### <span id="Disadvantages_of_This_Approach"></span><span id="disadvantages_of_this_approach"></span><span id="DISADVANTAGES_OF_THIS_APPROACH"></span>Disadvantages of This Approach

Because it runs in an arbitrary thread context at IRQL &lt;= DISPATCH\_LEVEL, a completion routine can perform only limited processing on the IRP.

 

 




