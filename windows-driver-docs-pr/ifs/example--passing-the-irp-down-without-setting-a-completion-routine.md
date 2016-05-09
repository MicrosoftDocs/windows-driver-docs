---
title: Example Passing the IRP Down Without Setting a Completion Routine
description: Example Passing the IRP Down Without Setting a Completion Routine
ms.assetid: d18d3ead-2cec-4ea6-ac4c-b809ba985f23
keywords: ["IRP dispatch routines WDK file system , passing IRP down", "passing IRPs down device stack WDK"]
---

# Example: Passing the IRP Down Without Setting a Completion Routine


## <span id="ddk_example_passing_the_irp_down_without_setting_a_completion_routine_"></span><span id="DDK_EXAMPLE_PASSING_THE_IRP_DOWN_WITHOUT_SETTING_A_COMPLETION_ROUTINE_"></span>


To pass the IRP down to lower-level drivers without setting a completion routine, a dispatch routine must do the following:

-   Call [**IoSkipCurrentIrpStackLocation**](https://msdn.microsoft.com/library/windows/hardware/ff550355) to remove the current IRP stack location, so that the I/O Manager will not look for a completion routine there when it performs completion processing on the IRP.

-   Call [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336) to pass the IRP down to the next lower-level driver.

This technique is illustrated in the following code examples:

```
IoSkipCurrentIrpStackLocation ( Irp ); 
return IoCallDriver ( NextLowerDriverDeviceObject, Irp ); 
```

Or, equivalently:

```
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Example:%20Passing%20the%20IRP%20Down%20Without%20Setting%20a%20Completion%20Routine%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




