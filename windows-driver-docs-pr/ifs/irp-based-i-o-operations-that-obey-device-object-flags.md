---
title: IRP-Based I/O Operations That Obey Device Object Flags
author: windows-driver-content
description: IRP-Based I/O Operations That Obey Device Object Flags
ms.assetid: d322aeda-a753-4616-8a35-1a5ae5a37cf2
---

# IRP-Based I/O Operations That Obey Device Object Flags


## <span id="ddk_irp_based_io_operations_that_obey_device_object_flags_if"></span><span id="DDK_IRP_BASED_IO_OPERATIONS_THAT_OBEY_DEVICE_OBJECT_FLAGS_IF"></span>


The buffering method for the following IRP-based I/O operations is determined by the value of the **Flags** member of the [**DEVICE\_OBJECT**](https://msdn.microsoft.com/library/windows/hardware/ff543147) structure for the file system volume:

-   IRP\_MJ\_DIRECTORY\_CONTROL

-   IRP\_MJ\_QUERY\_EA

-   IRP\_MJ\_QUERY\_QUOTA

-   IRP\_MJ\_READ

-   IRP\_MJ\_SET\_EA

-   IRP\_MJ\_SET\_QUOTA

-   IRP\_MJ\_WRITE

The DO\_BUFFERED\_IO and DO\_DIRECT\_IO flags in the **Flags** member are used as follows:

-   If the DO\_BUFFERED\_IO flag is set, the operation uses buffered I/O.

-   If the DO\_DIRECT\_IO flag is set and the DO\_BUFFERED\_IO flag is not set, the operation uses direct I/O.

-   If neither flag is set, the operation uses neither buffered nor direct I/O.

For more information about device object flags, see [**DEVICE\_OBJECT**](https://msdn.microsoft.com/library/windows/hardware/ff543147) and [Initializing a Device Object](https://msdn.microsoft.com/library/windows/hardware/ff547807).

Note that IRP\_MJ\_READ and IRP\_MJ\_WRITE can be IRP-based or fast I/O operations. When they are IRP-based, the buffering method is determined by the device object flags as described above. When these operations are fast I/O, they always use neither buffered nor direct I/O. For more information about I/O operations that can be IRP-based or fast I/O operations, see [Operations That Can Be IRP-Based or Fast I/O](operations-that-can-be-irp-based-or-fast-i-o.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20IRP-Based%20I/O%20Operations%20That%20Obey%20Device%20Object%20Flags%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


