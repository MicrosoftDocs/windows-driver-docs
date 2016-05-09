---
title: Using IRP Completion Routines
description: Using IRP Completion Routines
ms.assetid: 82b9ba2b-17db-40e5-be3f-fd77cd986781
keywords: ["filter drivers WDK file system , IRP completion routines", "file system filter drivers WDK , IRP completion routines", "IRP completion routines WDK file system", "IRPs WDK file system", "completing I/O requests WDK file system", "IRP completion routines WDK file system , about IRP completion routines"]
---

# Using IRP Completion Routines


## <span id="ddk_using_irp_completion_routines_if"></span><span id="DDK_USING_IRP_COMPLETION_ROUTINES_IF"></span>


**Note**  For optimal reliability and performance, we recommend using [file system minifilter drivers](filter-manager-and-minifilter-driver-architecture.md) instead of legacy file system filter drivers. Also, legacy file system filter drivers can’t attach to direct access (DAX) volumes. For more about file system minifilter drivers, see [Advantages of the Filter Manager Model](advantages-of-the-filter-manager-model.md). To port your legacy driver to a minifilter driver, see [Guidelines for Porting Legacy Filter Drivers](guidelines-for-porting-legacy-filter-drivers.md).

 

File system filter drivers use completion routines that are similar to those used by device drivers. A *completion routine* performs completion processing on an IRP. Any driver routine that passes an IRP down to the next-lower-level driver can optionally register a completion routine for the IRP by calling [**IoSetCompletionRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff549679) before calling [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336).

Every IRP completion routine is defined as follows:

```
NTSTATUS 
(*PIO_COMPLETION_ROUTINE) ( 
    IN PDEVICE_OBJECT DeviceObject, 
    IN PIRP Irp, 
    IN PVOID Context 
    ); 
```

Completion routines are called at IRQL &lt;= DISPATCH\_LEVEL, in an arbitrary thread context.

Because they can be called at IRQL DISPATCH\_LEVEL, completion routines cannot call kernel-mode routines that must be called at a lower IRQL, such as [**IoDeleteDevice**](https://msdn.microsoft.com/library/windows/hardware/ff549083). For the same reason, any data structures that are used in a completion routine must be allocated from nonpaged pool.

This section discusses the following topics:

[How Completion Processing Is Performed](how-completion-processing-is-performed.md)

[Checking the PendingReturned Flag](checking-the-pendingreturned-flag.md)

[Returning Status from Completion Routines](returning-status-from-completion-routines.md)

[Example: Simple Pass-Through Dispatch and Completion](example--simple-pass-through-dispatch-and-completion.md)

[Constraints on Completion Routines](constraints-on-completion-routines.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Using%20IRP%20Completion%20Routines%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




