---
title: Framework I/O Request Object
description: Framework I/O Request Object
ms.assetid: e48437ee-597d-45b1-9093-8d5921356af5
keywords: ["UMDF objects WDK , I/O request objects", "framework objects WDK UMDF , I/O request objects", "I/O request objects WDK UMDF", "IWDFIoRequest"]
---

# Framework I/O Request Object


\[This topic applies to UMDF 1.*x*.\]

The framework I/O request object is exposed to drivers by the [IWDFIoRequest](https://msdn.microsoft.com/library/windows/hardware/ff558985) interface. It encapsulates the details of an I/O operation. All I/O requests are represented as framework I/O request objects. The reflector notifies the driver host process when the reflector receives an I/O request packet (IRP) as the result of an application I/O operation, such as, a call to the Microsoft Win32 [**CreateFile**](https://msdn.microsoft.com/library/windows/desktop/aa363858) or **ReadFile** function. The framework, in response to the reflector notification, constructs a new request object and puts it in the appropriate I/O queue. The queue configuration and the locking model chosen by the user-mode driver determine when the request is presented to the driver. For more information, see [Configuring Dispatch Mode for an I/O Queue](configuring-dispatch-mode-for-an-i-o-queue.md) and [Specifying a Callback Synchronization Mode](specifying-a-callback-synchronization-mode.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Framework%20I/O%20Request%20Object%20%20RELEASE:%20%283/25/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




