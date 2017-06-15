---
title: Packet-Driven I/O with Reusable IRPs
author: windows-driver-content
description: Packet-Driven I/O with Reusable IRPs
MS-HAID:
- 'Intro\_3a40b890-cba9-4744-98e2-7fbe99a33861.xml'
- 'kernel.packet\_driven\_i\_o\_with\_reusable\_irps'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: ff315b61-9fa3-4a20-bc3e-82db0ea3cde7
keywords: ["I/O stack locations WDK kernel", "packet-driven I/O WDK kernel", "reusing IRPs WDK kernel", "headers WDK kernel", "I/O manager communication WDK kernel", "I/O status blocks WDK kernel", "status blocks WDK kernel", "stack locations WDK kernel", "IRPs WDK kernel , reusing"]
---

# Packet-Driven I/O with Reusable IRPs


## <a href="" id="ddk-packet-driven-i-o-with-reusable-irps-kg"></a>


The I/O manager, Plug and Play manager, and power manager use *I/O request packets* (IRPs) to communicate with kernel-mode drivers, and to allow drivers to communicate with each other.

The I/O manager performs the following steps:

-   Accepts I/O requests, which usually originate from user-mode applications.

-   Creates IRPs to represent the I/O requests.

-   Routes the IRPs to the appropriate drivers.

-   Tracks the IRPs until they are completed.

-   Returns the status to the original requester of each I/O operation.

An IRP might be routed to more than one driver. For example, a request to open a file on a disk might go first to a file system driver, through an intermediate mirror driver, and ultimately to a disk driver and, possibly, to a PnP hardware bus driver. This set of drivers is known as a *driver stack*.

Therefore, each IRP has a *fixed part*, plus one driver-specific *I/O stack location* for each driver that controls the device:

-   In the fixed part (or *header*), the I/O manager maintains information about the original request, such as the caller's thread ID and parameters, the address of the device object on which a file is open, and so forth. The fixed part also contains an *I/O status block*, in which drivers set information about the status of the requested I/O operation.

-   In the highest-level driver's I/O stack location, the I/O manager, Plug and Play manager, or power manager sets driver-specific parameters, such as the function code of the requested operation and the context that the corresponding driver uses to determine what it should do. In turn, each driver sets up the I/O stack location of the next-lower driver in the driver stack.

As each driver processes an IRP, it can access its I/O stack location in the IRP, thereby reusing the IRP at each stage of the driver's operations. In addition, higher-level drivers can create (or reuse) IRPs to send requests down to even lower-level drivers.

For a detailed discussion of IRPs, see [Handling IRPs](handling-irps.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Packet-Driven%20I/O%20with%20Reusable%20IRPs%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


