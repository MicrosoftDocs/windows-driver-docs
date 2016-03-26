---
title: Framework Object Events
description: Framework Object Events
ms.assetid: 1bccdd47-8ad6-4607-947f-18c5d2e03038
keywords: ["framework objects WDK KMDF , events", "events WDK KMDF", "events WDK KMDF , framework objects"]
---

# Framework Object Events


## <a href="" id="ddk-framework-object-events-df"></a>


Some framework objects can generate events. Framework-based drivers can register to receive notification of all, some, or none of an object's events. To register for an event, the driver provides an event callback function. The framework calls the callback function when the event occurs.

For example, a driver can register an [*EvtIoDefault*](https://msdn.microsoft.com/library/windows/hardware/ff541757) callback function for an I/O queue. The framework will call this callback function each time the framework is ready to remove an I/O request from the I/O queue and deliver it to the driver.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Framework%20Object%20Events%20%20RELEASE:%20%283/25/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




