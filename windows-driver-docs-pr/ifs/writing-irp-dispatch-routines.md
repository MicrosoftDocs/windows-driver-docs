---
title: Writing IRP Dispatch Routines
description: Writing IRP Dispatch Routines
ms.assetid: 8ce88932-cba6-4261-a938-d38133c20355
keywords: ["filter drivers WDK file system , IRP dispatch routines", "file system filter drivers WDK , IRP dispatch routines", "dispatch routines WDK file system", "IRP dispatch routines WDK file system", "writing IRP dispatch routines", "IRP dispatch routines WDK file system , about writing IRP dispatch routines", "IRPs WDK file system"]
---

# Writing IRP Dispatch Routines


## <span id="ddk_writing_irp_dispatch_routines_if"></span><span id="DDK_WRITING_IRP_DISPATCH_ROUTINES_IF"></span>


**Note**  For optimal reliability and performance, we recommend using [file system minifilter drivers](filter-manager-and-minifilter-driver-architecture.md) instead of legacy file system filter drivers. Also, legacy file system filter drivers can’t attach to direct access (DAX) volumes. For more about file system minifilter drivers, see [Advantages of the Filter Manager Model](advantages-of-the-filter-manager-model.md). To port your legacy driver to a minifilter driver, see [Guidelines for Porting Legacy Filter Drivers](guidelines-for-porting-legacy-filter-drivers.md).

 

File system filter drivers use dispatch routines that are similar to those used in device drivers. A *dispatch routine* handles one or more types of IRPs. (The *type* of an IRP is determined by its major function code.) The driver's [DriverEntry](initializing-a-file-system-filter-driver.md) routine *registers* dispatch routine entry points by storing them in the driver object's dispatch table. When an IRP is sent to the driver, the I/O subsystem calls the appropriate dispatch routine based on the IRP's major function code.

Every IRP dispatch routine is defined as follows:

```
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Writing%20IRP%20Dispatch%20Routines%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




