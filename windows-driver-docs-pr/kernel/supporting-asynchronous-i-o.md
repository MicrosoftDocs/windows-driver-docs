---
title: Supporting Asynchronous I/O
author: windows-driver-content
description: Supporting Asynchronous I/O
MS-HAID:
- 'Intro\_0a748ac1-63eb-472f-832b-8909d3631e14.xml'
- 'kernel.supporting\_asynchronous\_i\_o'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: b4baf1a9-6156-4bbf-b4d9-7205924c637f
keywords: ["asynchronous I/O WDK kernel", "I/O WDK kernel , asynchronous mode", "status information WDK I/O requests"]
---

# Supporting Asynchronous I/O


## <a href="" id="ddk-supporting-asynchronous-i-o-kg"></a>


The I/O manager provides asynchronous I/O support so that the originator of an I/O request (usually a user-mode application but sometimes another driver) can continue executing, rather than wait for its I/O request to be completed. Asynchronous I/O support improves both the overall system throughput and the performance of any code that makes an I/O request.

With asynchronous I/O support, kernel-mode drivers do not necessarily process I/O requests in the same order in which they were sent to the I/O manager. The I/O manager, or a higher-level driver, can reorder I/O requests as they are received. A driver can split a large data transfer request into smaller transfer requests. Moreover, a driver can overlap I/O request processing, particularly in a symmetric multiprocessor platform, as mentioned in [Multiprocessor-Safe](multiprocessor-safe.md).

Furthermore, a kernel-mode driver's processing of an individual I/O request is not necessarily serialized. That is, a driver does not necessarily process each IRP to completion before it starts processing the next incoming I/O request.

When a driver receives an IRP, it responds by carrying out as much IRP-specific processing as it can. If the driver supports asynchronous IRP processing, it can send an IRP to the next driver, if necessary, and begin processing the next IRP without waiting for the first one to be completed. The driver can register a "completion routine," which the I/O manager calls when another driver has finished processing an IRP. Drivers provide a status value in the IRP's I/O status block, which other drivers can access to determine the status of an I/O request.

Drivers can maintain state information about their current I/O operations in a special part of their device objects, called a [device extension](device-extensions.md).

For more information, see [Handling IRPs](handling-irps.md) and [Input/Output Techniques](i-o-programming-techniques.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Supporting%20Asynchronous%20I/O%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


