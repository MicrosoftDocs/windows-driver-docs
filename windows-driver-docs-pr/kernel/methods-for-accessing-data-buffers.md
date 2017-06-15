---
title: Methods for Accessing Data Buffers
author: windows-driver-content
description: Methods for Accessing Data Buffers
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: f95a0aec-65f9-44c9-8ae5-11bb4d832752
keywords: ["I/O WDK kernel , data buffers", "data buffers WDK I/O", "buffers WDK I/O", "buffers WDK I/O , accessing", "data buffers WDK I/O , accessing", "data transfers WDK kernel , data buffer access", "transferring data WDK kernel , data buffer access"]
---

# Methods for Accessing Data Buffers


One of the primary responsibilities of driver stacks is transferring data between user-mode applications and a system's devices. The operating system provides the following three methods for accessing data buffers:

<a href="" id="buffered-i-o"></a>*Buffered I/O*  
The operating system creates a nonpaged system buffer, equal in size to the application's buffer. For write operations, the I/O manager copies user data into the system buffer before calling the driver stack. For read operations, the I/O manager copies data from the system buffer into the application's buffer after the driver stack completes the requested operation.

For more information, see [Using Buffered I/O](using-buffered-i-o.md).

<a href="" id="direct-i-o"></a>*Direct I/O*  
The operating system locks the application's buffer in memory. It then creates a memory descriptor list (MDL) that identifies the locked memory pages, and passes the MDL to the driver stack. Drivers access the locked pages through the MDL.

For more information, see [Using Direct I/O](using-direct-i-o.md).

<a href="" id="neither-buffered-nor-direct-i-o"></a>*Neither Buffered Nor Direct I/O*  
The operating system passes the application buffer's virtual starting address and size to the driver stack. The buffer is only accessible from drivers that execute in the application's thread context.

For more information, see [Using Neither Buffered Nor Direct I/O](using-neither-buffered-nor-direct-i-o.md).

For [**IRP\_MJ\_READ**](https://msdn.microsoft.com/library/windows/hardware/ff550794) and [**IRP\_MJ\_WRITE**](https://msdn.microsoft.com/library/windows/hardware/ff550819) requests, drivers specify the I/O method by using flags in each [**DEVICE\_OBJECT**](https://msdn.microsoft.com/library/windows/hardware/ff543147) structure. For more information, see [Initializing a Device Object](initializing-a-device-object.md).

For [**IRP\_MJ\_DEVICE\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550744) and [**IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550766) requests, the I/O method is determined by the *TransferType* value that is contained in each IOCTL value. For more information, see [Defining I/O Control Codes](defining-i-o-control-codes.md).

All drivers in a driver stack must use the same buffer access method for each request, except possibly for the highest-level driver (which can use the "neither" method, regardless of the method used by lower drivers).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Methods%20for%20Accessing%20Data%20Buffers%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


