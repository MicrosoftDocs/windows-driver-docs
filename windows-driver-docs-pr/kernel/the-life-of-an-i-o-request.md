---
title: The Life of an I/O Request
author: windows-driver-content
description: The Life of an I/O Request
MS-HAID:
- 'IRPs\_16db8301-5cf2-4e67-9d90-043cd05aa328.xml'
- 'kernel.the\_life\_of\_an\_i\_o\_request'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 3198e96c-3794-4736-b7e8-d2704abf1aca
keywords: ["IRPs WDK kernel , I/O request process", "I/O requests WDK kernel", "protected subsystems WDK kernel", "subsystem I/O request process WDK kernel", "user I/O requests WDK kernel"]
---

# The Life of an I/O Request


## <a href="" id="ddk-the-life-of-an-i-o-request-kg"></a>


This section describes the path taken by an IRP from creation by the operating system to its completion by the set of drivers responsible for controlling the target device. The section contains the following topics:

[Example I/O Request – An Overview](example-i-o-request---an-overview.md)

[Example I/O Request – The Details](example-i-o-request---the-details.md)

[Driver Thread Context](driver-thread-context.md)

[Points to Consider about User I/O Requests](points-to-consider-about-user-i-o-requests.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20The%20Life%20of%20an%20I/O%20Request%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


