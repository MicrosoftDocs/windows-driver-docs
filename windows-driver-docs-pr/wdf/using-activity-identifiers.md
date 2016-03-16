---
title: Using Activity Identifiers
description: Using Activity Identifiers
ms.assetid: 2B70953F-5192-4654-9506-6A84373D20B4
---

# Using Activity Identifiers


In framework versions 1.11 and later, UMDF drivers can set and retrieve activity identifiers (IDs). Activity IDs allow you to associate multiple I/O requests, so that you can track them using Event Tracing for Windows (ETW) tracing. This topic describes some possible scenarios in which the driver might use activity IDs.

## Associating New Requests with an Existing Request


In your driver's I/O dispatch callback function, you might create multiple framework I/O requests as a result of an incoming request. The driver obtains the activity ID from the original request and sets it in the new requests by calling [**WdfRequestRetrieveActivityId**](https://msdn.microsoft.com/library/windows/hardware/dn265621) and [**WdfRequestSetActivityId**](https://msdn.microsoft.com/library/windows/hardware/dn265622).

For a code example, see [**WdfRequestRetrieveActivityId**](https://msdn.microsoft.com/library/windows/hardware/dn265621).

## Associating New Requests with an Existing Thread


A driver might create a new I/O request in a thread other than the I/O dispatch thread, or in a work item. You can set the activity ID for such a request from any corresponding request, or by using the activity ID associated with the I/O dispatch thread. The driver can retrieve the activity ID associated with the current thread by calling [**EventActivityIdControl**](https://msdn.microsoft.com/library/windows/desktop/aa363720) and then calling [**WdfRequestSetActivityId**](https://msdn.microsoft.com/library/windows/hardware/dn265622) to set the identifier for each new I/O request.

If the driver calls the Win32 API to send an I/O request, it can retrieve the activity ID from the original request and propagate it to the thread. The I/O manager then applies the activity ID that is associated with the thread to any I/O request packets (IRPs) that it generates in response to the request.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Using%20Activity%20Identifiers%20%20RELEASE:%20%283/16/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




