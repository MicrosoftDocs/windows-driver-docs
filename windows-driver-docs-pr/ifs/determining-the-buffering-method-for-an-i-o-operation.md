---
title: Determining the Buffering Method for an I/O Operation
description: Determining the Buffering Method for an I/O Operation
ms.assetid: 219378d9-a9fa-495a-b016-36595a7efb49
keywords: ["buffers WDK file system minifilter", "preoperation callback routines WDK file system minifilter , buffers", "postoperation callback routines WDK file system minifilter , buffers", "buffered I/O WDK file system", "direct I/O WDK file system", "neither buffered nor direct I/O WDK file system", "data buffers WDK file system minifilter", "I/O WDK file systems"]
---

# Determining the Buffering Method for an I/O Operation


## <span id="ddk_determining_the_buffering_method_for_an_io_operation_if"></span><span id="DDK_DETERMINING_THE_BUFFERING_METHOD_FOR_AN_IO_OPERATION_IF"></span>


Like device drivers, file systems are responsible for transferring data between user-mode applications and a system's devices. The operating system provides the following three methods for accessing data buffers:

-   In *buffered I/O*, the I/O manager allocates a system buffer for the operation from nonpaged pool. The I/O manager copies data from this system buffer into the application's user buffer, and vice versa, in the context of the thread that initiated the I/O operation.

-   In *direct I/O*, the I/O manager probes and locks the user buffer. It then creates a memory descriptor list (MDL) to map the locked buffer. The I/O manager accesses the buffer in the context of the thread that initiated the I/O operation.

-   In *neither buffered nor direct I/O*, the I/O manager does not allocate a system buffer and does not lock or map the user buffer. Instead, it simply passes the buffer's original user-space virtual address to the file system stack. Drivers are responsible for ensuring that they are executing in the context of the initiating thread and that the buffer addresses are valid.

    Minifilter drivers must validate any address in user space before trying to use it. The I/O manager and filter manager do not validate such addresses and do not validate pointers that are embedded in buffers that are passed to minifilter drivers.

All standard Microsoft file systems use neither buffered nor direct I/O for most I/O processing.

For more information about buffering methods, see [Methods for Accessing Data Buffers](https://msdn.microsoft.com/library/windows/hardware/ff554436).

For IRP-based I/O operations, the buffering method used is operation-specific and is determined by the following factors:

-   The type of I/O operation that is being performed

-   The value of the **Flags** member of the [**DEVICE\_OBJECT**](https://msdn.microsoft.com/library/windows/hardware/ff543147) structure for the file system volume

-   For I/O control (IOCTL) and file system control (FSCTL) operations, the value of the *TransferType* parameter that was passed to the CTL\_CODE macro when the IOCTL or FSCTL was defined

Fast I/O operations that have buffers always use neither buffered nor direct I/O.

File system callback operations do not have buffers.

This section includes:

[Operations That Can Be IRP-Based or Fast I/O](operations-that-can-be-irp-based-or-fast-i-o.md)

[IRP-Based I/O Operations That Obey Device Object Flags](irp-based-i-o-operations-that-obey-device-object-flags.md)

[IRP-Based I/O Operations That Always Use Buffered I/O](irp-based-i-o-operations-that-always-use-buffered-i-o.md)

[IRP-Based I/O Operations That Always Use Neither Buffered Nor Direct I/O](irp-based-i-o-operations-that-always-use-neither-buffered-nor-direct-i.md)

[IRP-Based IOCTL and FSCTL Operations](irp-based-ioctl-and-fsctl-operations.md)

[IRP-Based I/O Operations That Have No Buffers](irp-based-i-o-operations-that-have-no-buffers.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Determining%20the%20Buffering%20Method%20for%20an%20I/O%20Operation%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




