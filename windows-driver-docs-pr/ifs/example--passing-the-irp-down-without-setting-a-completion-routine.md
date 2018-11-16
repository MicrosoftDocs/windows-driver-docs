---
title: Example Passing the IRP Down Without Setting a Completion Routine
description: Example Passing the IRP Down Without Setting a Completion Routine
ms.assetid: d18d3ead-2cec-4ea6-ac4c-b809ba985f23
keywords:
- IRP dispatch routines WDK file system , passing IRP down
- passing IRPs down device stack WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Example: Passing the IRP Down Without Setting a Completion Routine


## <span id="ddk_example_passing_the_irp_down_without_setting_a_completion_routine_"></span><span id="DDK_EXAMPLE_PASSING_THE_IRP_DOWN_WITHOUT_SETTING_A_COMPLETION_ROUTINE_"></span>


To pass the IRP down to lower-level drivers without setting a completion routine, a dispatch routine must do the following:

-   Call [**IoSkipCurrentIrpStackLocation**](https://msdn.microsoft.com/library/windows/hardware/ff550355) to remove the current IRP stack location, so that the I/O Manager will not look for a completion routine there when it performs completion processing on the IRP.

-   Call [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336) to pass the IRP down to the next lower-level driver.

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

In these examples, the first parameter in the call to [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336) is a pointer to the next-lower-level filter driver's device object. The second parameter is a pointer to the IRP.

### <span id="Advantages_of_This_Approach"></span><span id="advantages_of_this_approach"></span><span id="ADVANTAGES_OF_THIS_APPROACH"></span>Advantages of This Approach

The technique shown above (calling [**IoSkipCurrentIrpStackLocation**](https://msdn.microsoft.com/library/windows/hardware/ff550355)) is simple and efficient and should be used in all cases where the driver passes the IRP down the driver stack without registering a completion routine.

### <span id="Disadvantages_of_This_Approach"></span><span id="disadvantages_of_this_approach"></span><span id="DISADVANTAGES_OF_THIS_APPROACH"></span>Disadvantages of This Approach

After [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336) is called, the IRP pointer that was passed to **IoCallDriver** is no longer valid and cannot safely be dereferenced. If the driver needs to perform further processing or cleanup after the IRP has been processed by lower-level drivers, it must set a completion routine before sending the IRP down the driver stack. For more information about writing and setting completion routines, see [Using Completion Routines](using-irp-completion-routines.md).

If you call [**IoSkipCurrentIrpStackLocation**](https://msdn.microsoft.com/library/windows/hardware/ff550355) for an IRP, you cannot set a completion routine for it.

 

 




