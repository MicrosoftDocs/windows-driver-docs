---
title: Methods for Accessing Data Buffers
description: Methods for Accessing Data Buffers
ms.assetid: f95a0aec-65f9-44c9-8ae5-11bb4d832752
keywords: ["I/O WDK kernel , data buffers", "data buffers WDK I/O", "buffers WDK I/O", "buffers WDK I/O , accessing", "data buffers WDK I/O , accessing", "data transfers WDK kernel , data buffer access", "transferring data WDK kernel , data buffer access"]
ms.date: 06/16/2017
ms.localizationpriority: medium
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

 

 




