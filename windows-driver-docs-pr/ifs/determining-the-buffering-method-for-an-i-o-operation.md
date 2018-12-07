---
title: Determining the Buffering Method for an I/O Operation
description: Determining the Buffering Method for an I/O Operation
ms.assetid: 219378d9-a9fa-495a-b016-36595a7efb49
keywords:
- buffers WDK file system minifilter
- preoperation callback routines WDK file system minifilter , buffers
- postoperation callback routines WDK file system minifilter , buffers
- buffered I/O WDK file system
- direct I/O WDK file system
- neither buffered nor direct I/O WDK file system
- data buffers WDK file system minifilter
- I/O WDK file systems
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 




