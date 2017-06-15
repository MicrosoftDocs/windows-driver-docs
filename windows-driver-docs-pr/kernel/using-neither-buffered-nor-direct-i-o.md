---
title: Using Neither Buffered Nor Direct I/O
author: windows-driver-content
description: Using Neither Buffered Nor Direct I/O
MS-HAID:
- 'ioproguser\_c6e8f2ab-7282-4282-b149-63300a7d97d4.xml'
- 'kernel.using\_neither\_buffered\_nor\_direct\_i\_o'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: e85af2e0-e532-47ca-918e-087e7aff859e
keywords: ["buffers WDK I/O , neither buffered nor direct I/O", "data buffers WDK I/O , neither buffered nor direct I/O", "neither buffered nor direct I/O WDK kernel"]
---

# Using Neither Buffered Nor Direct I/O


## <a href="" id="ddk-using-neither-buffered-nor-direct-i-o-kg"></a>


If a driver is using neither buffered nor direct I/O, then the I/O manager passes the original user-space virtual addresses in IRPs that it sends to the driver. To access these buffers safely, the driver must be executing in the context of the calling thread. Typically, therefore, only highest-level drivers, such as FSDs, can use this method for accessing buffers.

An intermediate or lowest-level driver cannot always meet this condition. For example, if a requesting thread waits on the completion of an I/O request or if a higher-level driver is layered over the intermediate or lowest-level driver, then the lower-level driver's routines are unlikely to be called in the context of the requesting thread.

The I/O manager determines that an I/O operation is using neither buffered nor direct I/O as follows:

-   For [**IRP\_MJ\_READ**](https://msdn.microsoft.com/library/windows/hardware/ff550794) and [**IRP\_MJ\_WRITE**](https://msdn.microsoft.com/library/windows/hardware/ff550819) requests, neither DO\_BUFFERED\_IO nor DO\_DIRECT\_IO are set in the **Flags** member of the [**DEVICE\_OBJECT**](https://msdn.microsoft.com/library/windows/hardware/ff543147) structure. For more information, see [Initializing a Device Object](initializing-a-device-object.md).

-   For [**IRP\_MJ\_DEVICE\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550744) and [**IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550766) requests, the IOCTL code's value contains METHOD\_NEITHER as the *TransferType* value in the IOCTL value. For more information, see [Defining I/O Control Codes](defining-i-o-control-codes.md).

When a driver receives an IRP that specifies an I/O operation using neither buffered nor direct I/O, it must do the following:

1.  Check the validity of the user buffer's address range and check whether the appropriate read or write access is permitted, using the [**ProbeForRead**](https://msdn.microsoft.com/library/windows/hardware/ff559876) and [**ProbeForWrite**](https://msdn.microsoft.com/library/windows/hardware/ff559879) support routines. The driver must enclose its accesses to the buffer's address range within a driver-supplied exception handler, so that a user thread cannot change the access rights for the buffer while the driver is accessing memory. If the probe raises an exception, the driver should return an error. The driver must call these routines within the context of the thread that made the I/O request; therefore, only a higher-level driver can perform this task.

2.  Manage buffers and memory operations in one of the following ways:
    -   Carry out its own double-buffering operations, as the I/O manager does for drivers that use buffered I/O. For more information, see [Using Buffered I/O](using-buffered-i-o.md).
    -   Create its own MDLs and lock down the buffer by calling the memory manager's support routines, as the I/O manager does for drivers that use direct I/O. For more information, see [Using Direct I/O](using-direct-i-o.md).
    -   Perform all necessary operations on the user buffer directly in the context of the calling thread. The driver must wrap its access to the buffer within a driver-supplied exception handler, in case a user thread changes either the access rights for the buffer or the data in the buffer while the driver is accessing memory. For more information, see [Handling Exceptions](handling-exceptions.md).

In effect, the driver must choose on a per-IRP basis whether to do buffered I/O, direct I/O, or I/O in the context of the calling thread, and it must handle any exceptions that might occur in a user-mode thread context. The driver must manage its own user buffer accesses, double-buffering operations, and memory mappings, as necessary, instead of letting the I/O manager handle these operations for the driver.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Using%20Neither%20Buffered%20Nor%20Direct%20I/O%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


